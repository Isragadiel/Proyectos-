package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class ProductPage {

    private WebDriver driver;
    private WebDriverWait wait;

    // Locators de la página de producto
    private By precioProducto = By.cssSelector(".js-price-display");
    private By botonAgregar = By.cssSelector("[data-component='product.add-to-cart']");
    private By contadorCarrito = By.cssSelector(".js-cart-widget-amount");
    private By precioTotalCarrito = By.cssSelector("[data-component='cart.total']");

    public ProductPage(WebDriver driver, WebDriverWait wait) {
        this.driver = driver;
        this.wait = wait;
    }

    // Verifica si el precio está visible
    public boolean precioEsVisible() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(precioProducto));
        return driver.findElement(precioProducto).isDisplayed();
    }

    // Verifica si el botón agregar está visible
    public boolean botonAgregarVisible() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(botonAgregar));
        return driver.findElement(botonAgregar).isDisplayed();
    }

    // Obtiene el texto del precio del producto
    public String obtenerPrecio() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(precioProducto));
        return driver.findElement(precioProducto).getText();
    }

    // Hace click en agregar al carrito
    public void clickAgregarCarrito() {
        wait.until(ExpectedConditions.elementToBeClickable(botonAgregar));
        driver.findElement(botonAgregar).click();
    }

    // Espera redirección al carrito
    public void esperarRedireccionCarrito() {
        wait.until(ExpectedConditions.urlContains("/comprar"));
    }

    // Obtiene el número de productos en el carrito
    public String obtenerCantidadCarrito() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(contadorCarrito));
        return driver.findElement(contadorCarrito).getText();
    }

    // Obtiene el total mostrado en el carrito
    public String obtenerTotalCarrito() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(precioTotalCarrito));
        return driver.findElement(precioTotalCarrito).getText();
    }
}

