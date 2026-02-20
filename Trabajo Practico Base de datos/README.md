Sistema de Gestión de Pacientes e Historias Clínicas
Este proyecto consiste en el diseño e implementación de una base de datos robusta para la gestión de pacientes, historias clínicas, intervenciones médicas y profesionales de la salud. El sistema ha sido normalizado hasta la Tercera Forma Normal (3NF) para garantizar la integridad de los datos y minimizar la redundancia.
+1

👥 Autores (Comisión 14)

Pablo Garay 


Israel Garcia Moscoso 


Jose Darío Gimenez 


Juan Esteban Gelos 

📋 Características Principales

Modelado Completo: Incluye gestión de pacientes, obras sociales, profesionales con especialidades, domicilios y registros detallados de intervenciones con medicamentos.
+2


Integridad y Seguridad: Implementación de claves primarias compuestas, claves foráneas con reglas de borrado y validaciones mediante triggers.


Eliminación Lógica: Todas las tablas principales cuentan con un sistema de borrado lógico para preservar el historial de los datos.


Privacidad (Sanitización): Vistas diseñadas para exponer información no sensible, ocultando datos PII (Información de Identificación Personal) como DNI o teléfonos.

📂 Estructura del Repositorio
Los archivos están organizados para ser ejecutados de forma secuencial:


01_esquema.sql: Creación de la base de datos pacienteHistoriaClinica y sus tablas fundamentales.


02_catalogo.sql: Carga de datos maestros (provincias, especialidades, obras sociales y medicamentos).


03_carga_masiva.sql: Procedimientos para la generación y carga masiva de datos ficticios (localidades, teléfonos, etc.).


05_consultas.sql: Reportes avanzados, incluyendo estadísticas por obra social y análisis de medicamentos.
+1


06_vistas.sql: Vistas de resumen de pacientes y estadísticas de rendimiento por profesional.


07_seguridad.sql: Implementación de vistas "sanitizadas" y procedimientos protegidos contra inyección SQL.


09_concurrencia_guiada.sql: Simulaciones de bloqueos, resolución de deadlocks y pruebas de niveles de aislamiento de transacciones.


Diagrama ER.pdf: Representación gráfica del modelo entidad-relación del sistema.
+1

🛠️ Requisitos e Instalación
Disponer de un motor de base de datos MySQL o compatible.

Ejecutar los scripts en el orden numérico indicado en la sección anterior para asegurar que las dependencias se creen correctamente.

🎥 Documentación Adicional

Video explicativo: Ver en YouTube 


Informe Final: Disponible en el PDF adjunto, detallando el proceso de modelado y las pruebas de concurrencia realizadas.