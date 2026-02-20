Automatización de Pruebas: E-commerce "Kazuma" 🚀
📋 Descripción
Este proyecto contiene una suite de pruebas automatizadas para el sitio web Kazuma. Se enfocan en validar los flujos críticos de navegación, búsqueda de productos y el proceso de agregado al carrito de compras, asegurando la integridad de las funciones principales de la tienda.

🛠️ Tecnologías y Herramientas
Lenguaje: Java

Framework de Testing: TestNG

Herramienta de Automatización: Selenium WebDriver

Patrón de Diseño: Page Object Model (POM)

Gestión de Drivers: WebDriverManager

Manejador de Dependencias: Maven (o Gradle según tu configuración)

🏗️ Arquitectura del Proyecto
El proyecto está organizado siguiendo el patrón POM, lo que facilita el mantenimiento y la reutilización del código:

base.BaseTest: Configuración central del Driver, esperas explícitas (WebDriverWait) y ciclos de vida de los tests (@BeforeMethod, @AfterMethod).

pages: Contiene las clases que representan las páginas del sitio, encapsulando los locators y las acciones.

HomePage: Interacciones con el buscador y resultados.

ProductPage: Validaciones de precio, detalles y acciones del carrito.

tests.HomeTest: Clase donde residen los casos de prueba y las aserciones (Assert).

🧪 Casos de Prueba Automatizados
La suite incluye los siguientes tests:

Validación de Búsqueda: Verifica que el buscador redirija correctamente a la página de resultados.

Validación de Resultados: Asegura que la búsqueda devuelva al menos un producto funcional.

Navegación a Producto: Comprueba que al hacer click en un item se acceda correctamente a su PDP (Product Detail Page).

Validación de Detalles: Verifica la visibilidad de elementos críticos como el precio y el botón de compra.

Flujo Completo de Carrito: Simula la búsqueda, selección y agregado al carrito, validando que el contador y el total coincidan con el producto seleccionado.

🚀 Ejecución
Para correr las pruebas:

Clona el repositorio.

Asegúrate de tener instalado JDK 11+ y Maven.

Ejecuta los tests desde tu IDE (IntelliJ/Eclipse) o mediante la terminal:

Bash
mvn test
📈 Beneficios de esta Automatización
Reutilización: Los métodos creados en las clases Page pueden usarse para nuevos escenarios de prueba.

Robustez: El uso de WebDriverWait evita errores de sincronización (falsos negativos).

Escalabilidad: Gracias a BaseTest, agregar nuevas clases de prueba no requiere configurar el navegador nuevamente.

👤 Autor
Israel Garcia

QA Automation Engineer (Student)