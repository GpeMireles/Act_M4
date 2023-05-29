# Act_M4
 Actividad de Midterm
 
 Link al video demostrativo: https://drive.google.com/file/d/185p5N3m8_dV7pk1bnkUWu-fpLJ0olts-/view?usp=share_link

## Investigación CORS:

CORS (Cross-Origin Resource Sharing) es un mecanismo de seguridad utilizado por los navegadores web para controlar las solicitudes de recursos realizadas desde un origen a otro origen diferente. Dado a que impone políticas de seguridad para proteger las solicitudes de orígenes, esta afecta a las aplicaciones web.

Cuando una aplicación web realiza una solicitud HTTP a un recurso en un origen diferente, el navegador aplica las políticas de mismo origen para evitar posibles ataques de seguridad. Sin embargo, CORS permite flexibilizar estas políticas estableciendo condiciones bajo las cuales se permiten las solicitudes entre orígenes.

La falta de configuración adecuada de CORS puede causar problemas en una aplicación web. Si el servidor no permite solicitudes desde otros orígenes, el navegador bloqueará esas solicitudes y la aplicación no podrá acceder a los recursos necesarios.
Por otro lado, una configuración excesivamente permisiva de CORS puede representar un riesgo de seguridad al permitir solicitudes no deseadas desde orígenes maliciosos.

En resumen, manejando bien la configuración CORS se puede proteger una aplicación restringiendo a los orígenes maliciosos pero permitiendo el acceso a los recursos requeridos.
