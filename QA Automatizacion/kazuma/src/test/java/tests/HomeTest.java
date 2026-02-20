package tests;

import base.BaseTest;
import org.testng.Assert;
import org.testng.annotations.Test;
import pages.HomePage;
import pages.ProductPage;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class HomeTest extends BaseTest {

    // Test simple de validación de título

    public void validarTituloHome() {

        // Obtiene el título actual
        String titulo = driver.getTitle();

        // Compara contra el esperado
        Assert.assertEquals(titulo, "KAZUMA");
    }

    // Valida que la búsqueda redirija correctamente
    @Test
    public void validarBusquedaProducto() {

        HomePage home = new HomePage(driver, wait);

        home.buscarProducto("remera");

        // Espera que la URL contenga "search"
        wait.until(ExpectedConditions.urlContains("search"));

        Assert.assertTrue(driver.getCurrentUrl().contains("search"));
    }

    // Valida que existan resultados
    @Test
    public void validarResultados() {

        HomePage home = new HomePage(driver, wait);

        home.buscarProducto("remera");
        home.esperarResultados();

        Assert.assertTrue(home.obtenerCantidadProductos() > 0,
                "No se encontraron productos");
    }

    // Valida que al hacer click se ingrese a página de producto
    @Test
    public void validarIngresoPaginaDeProducto() {

        HomePage home = new HomePage(driver, wait);

        home.buscarProducto("remera");
        home.esperarResultados();
        home.clickPrimerProducto();

        Assert.assertFalse(driver.getCurrentUrl().contains("search"));
    }

    // Valida que el detalle del producto tenga precio y botón
    @Test
    public void validarDetalleProducto() {

        HomePage home = new HomePage(driver, wait);

        home.buscarProducto("remera");
        home.esperarResultados();
        home.clickPrimerProducto();

        ProductPage productPage = new ProductPage(driver, wait);

        Assert.assertTrue(productPage.precioEsVisible());
        Assert.assertTrue(productPage.botonAgregarVisible());
    }

    // Flujo completo agregar al carrito
    @Test
    public void validarAgregarAlCarrito() {

        HomePage home = new HomePage(driver, wait);

        home.buscarProducto("remera");
        home.esperarResultados();
        home.clickPrimerProducto();

        ProductPage productPage = new ProductPage(driver, wait);

        String precioGuardado = productPage.obtenerPrecio();

        productPage.clickAgregarCarrito();
        productPage.esperarRedireccionCarrito();

        Assert.assertEquals(productPage.obtenerCantidadCarrito(), "1");

        Assert.assertEquals(productPage.obtenerTotalCarrito(), precioGuardado);
    }
}


