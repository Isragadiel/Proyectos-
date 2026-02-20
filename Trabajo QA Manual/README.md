README: Proyecto de Testing Manual - E-commerce "Kazuma"

📋 IntroducciónEste proyecto detalla el ciclo de calidad aplicado al sitio Kazuma. Se realizó un análisis exhaustivo de las funcionalidades principales de la plataforma, utilizando técnicas de caja negra para validar el comportamiento del sistema frente a los requisitos del negocio.

🛠️ Metodología aplicada
Análisis de Requisitos: Creación de 7 Historias de Usuario (HU) con formato Gherkin.

Diseño de Pruebas: Elaboración de 12 Casos de Prueba (TC), incluyendo flujos positivos y negativos.

Pruebas de Compatibilidad: Ejecución en entornos Desktop (Windows/Chrome) y Mobile (Android/Viewport 743x906).

Gestión de Defectos: Documentación técnica de bugs con niveles de severidad y prioridad.

📊 Resumen de Ejecución y Métricas

Categoría                      Detalle
Casos de Prueba Planificados    12
Casos de Prueba Ejecutados      12 (100%)
Estado en Desktop (PC)          100% Pass - Todas las funciones operan correctamente.

Estado en Mobile/Tablet         Fail - Se detectaron bloqueadores de interfaz.
Total de Bugs Reportados        5


🔍 Nota Técnica sobre los Resultados

Es importante destacar que los 12 Casos de Prueba resultaron Exitosos en el entorno de escritorio, validando que la lógica de negocio (registro, login, carrito) funciona correctamente. Sin embargo, mediante Testing Exploratorio y pruebas de responsividad, se detectaron fallos críticos de UI que bloquean estos mismos flujos en dispositivos móviles.

🐞 Reporte de Bugs Críticos
Se identificaron 5 defectos, siendo el más relevante el que afecta la conversión móvil:

Bug #5 [CRÍTICO]: El botón de Login es inexistente en resoluciones de 743x906 o menores.

Impacto: El usuario de celular no puede identificarse, aunque el sistema de login funcione internamente.

Bug #1 [ALTA]: Desaparición de la barra de navegación en pantalla completa (Desktop).

Bug #4 [ALTA]: Enlace roto (Error 404) en la sección de reseñas de productos.

Bug #2 y #3 [MEDIA]: Superposición de elementos visuales en el menú y pop-ups.

📂 Contenido de la Entrega

El trabajo se compone de los siguientes archivos:

testing.xlsx:

Pestaña HU: Definición de objetivos de usuario.

Pestaña Especificaciones CP: Pasos detallados y resultados (incluye los 5 casos negativos de login).

Pestaña Matriz de Trazabilidad (RTM): Verificación de cobertura de todas las HU.

Pestaña Reporte de Bugs: Detalle técnico de los fallos encontrados.

Trabajo testing manual.pdf: Informe con la identidad de la marca, análisis de elementos UI y evidencias gráficas de las pruebas.

💡 Conclusión y Recomendación

El sistema es funcionalmente sólido en su arquitectura (backend), pero presenta riesgos críticos en su capa de presentación (frontend).

Recomendación de QA: Se recomienda posponer el lanzamiento de la versión móvil hasta corregir el Bug #5, ya que la ausencia del botón de ingreso impide el flujo completo de compra para usuarios registrados, afectando directamente la rentabilidad del sitio.

👤 Información del Estudiante

Nombre: Israel Garcia

Materia: Testing Manual / QA