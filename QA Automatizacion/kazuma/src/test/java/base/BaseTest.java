package base;

// WebDriverManager descarga automáticamente el driver correcto
import io.github.bonigarcia.wdm.WebDriverManager;

// Clases principales de Selenium
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

// Clase para manejar esperas explícitas
import org.openqa.selenium.support.ui.WebDriverWait;

// Anotaciones de TestNG
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;

import java.time.Duration;

public class BaseTest {

    // WebDriver será usado por todas las clases que hereden de BaseTest
    protected WebDriver driver;

    // Wait explícito reutilizable
    protected WebDriverWait wait;

    // Se ejecuta antes de cada @Test
    @BeforeMethod
    public void setUp() {

        // Descarga y configura automáticamente el ChromeDriver
        WebDriverManager.chromedriver().setup();

        // Opciones del navegador
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");

        // Inicializamos el navegador
        driver = new ChromeDriver(options);

        // Maximiza la ventana
        driver.manage().window().maximize();

        // Creamos un wait explícito de 10 segundos
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        // Navegamos a la página base
        driver.get("https://kazuma.com.ar/");
    }

    // Se ejecuta después de cada @Test
    @AfterMethod
    public void tearDown() {

        // Cerramos el navegador si existe
        if (driver != null) {
            driver.quit();
        }
    }
}


