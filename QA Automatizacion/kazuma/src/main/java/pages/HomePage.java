package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class HomePage {

    private WebDriver driver;
    private WebDriverWait wait;

    // Locators (patrón Page Object)
    private By campoBusqueda = By.name("q");
    private By resultadosProductos = By.cssSelector(".js-item-product");
    private By botonMenu = By.cssSelector("[data-component='menu-button']");

    // Constructor recibe driver y wait desde BaseTest
    public HomePage(WebDriver driver, WebDriverWait wait) {
        this.driver = driver;
        this.wait = wait;
    }

    // Método para buscar un producto
    public void buscarProducto(String producto) {

        // Espera que el campo sea visible antes de interactuar
        wait.until(ExpectedConditions.visibilityOfElementLocated(campoBusqueda));

        // Escribe el texto
        driver.findElement(campoBusqueda).sendKeys(producto);

        // Presiona enter (submit del formulario)
        driver.findElement(campoBusqueda).submit();
    }

    // Espera hasta que aparezcan los resultados
    public void esperarResultados() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(resultadosProductos));
    }

    // Devuelve la cantidad de productos encontrados
    public int obtenerCantidadProductos() {
        return driver.findElements(resultadosProductos).size();
    }

    // Hace click en el primer producto de la lista
    public void clickPrimerProducto() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(resultadosProductos));
        driver.findElements(resultadosProductos).get(0).click();
    }

    // Abre el menú hamburguesa
    public void abrirMenu() {
        wait.until(ExpectedConditions.elementToBeClickable(botonMenu));
        driver.findElement(botonMenu).click();
    }
}

