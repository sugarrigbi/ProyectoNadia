<div align="center">

<!--
RECOMENDACIÓN:
Crea una carpeta llamada assets en la raíz del repositorio
y guarda allí tu banner con el nombre banner.png.
-->

<img src="./assets/banner.png" alt="Kevin Anzola | Backend Developer" width="100%">

# Kevin Anzola

### Backend Developer · Python · Flask · AWS · Docker

Desarrollador de software enfocado en la construcción de **APIs REST, aplicaciones backend, microservicios y soluciones desplegadas en la nube**.

Mi experiencia práctica incluye Python, Flask, MySQL, Redis, Docker, Linux, AWS y desarrollo móvil con React Native.

Actualmente curso **Tecnología en Desarrollo de Software** en la Fundación Universitaria San Mateo.

<br>

[![GitHub](https://img.shields.io/badge/GitHub-KevinAnzola-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/KevinAnzola)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Kevin_Anzola-0A66C2?style=for-the-badge\&logo=linkedin\&logoColor=white)](TU_LINK_DE_LINKEDIN)
[![Email](https://img.shields.io/badge/Email-Contáctame-EA4335?style=for-the-badge\&logo=gmail\&logoColor=white)](mailto:TU_CORREO)

</div>

---

## Sobre mí

Soy desarrollador de software con interés principal en el desarrollo backend, la arquitectura de aplicaciones y la infraestructura cloud.

He trabajado en proyectos que integran:

* APIs REST desarrolladas con Flask
* Arquitectura basada en microservicios
* Bases de datos MySQL
* Redis para almacenamiento en caché y comunicación
* Contenedores con Docker y Docker Compose
* Servidores Linux
* Despliegues en AWS EC2 y AWS RDS
* Configuración de Nginx y certificados SSL
* Aplicaciones web, móviles y de escritorio
* Integración con APIs y servicios externos

Este repositorio reúne proyectos académicos y personales desarrollados durante diferentes etapas de mi formación.

Cada carpeta representa parte de mi evolución, desde ejercicios de lógica y aplicaciones de escritorio hasta sistemas completos desplegados en la nube.

---

# Proyecto principal

<div align="center">

## GaiaLink

### Sistema de gestión basado en microservicios

[![Ver proyecto](https://img.shields.io/badge/Explorar-GaiaLink-2EA44F?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/KevinAnzola/Ingenieria_Sistemas/tree/main/Proyecto_GaiaLink)

</div>

GaiaLink es el proyecto que mejor representa mis habilidades actuales como desarrollador.

Es un sistema desarrollado con una arquitectura distribuida, compuesto por distintos servicios encargados de gestionar usuarios, autenticación, casos, notificaciones, persistencia de datos y procesos internos.

El proyecto integra backend, frontend, bases de datos, almacenamiento en caché, despliegue en AWS, contenedores Docker y configuración de infraestructura.

<div align="center">

<!-- Reemplaza esta imagen por una captura real de GaiaLink -->

<img src="./assets/gaialink-dashboard.png" alt="Dashboard de GaiaLink" width="90%">

</div>

## Stack principal de GaiaLink

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge\&logo=flask\&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge\&logo=redis\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge\&logo=amazonwebservices\&logoColor=FF9900)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge\&logo=nginx\&logoColor=white)

</div>

## Características técnicas

* Arquitectura basada en microservicios
* APIs REST desarrolladas con Flask
* Separación de responsabilidades por servicio
* Autenticación y gestión de usuarios
* Gestión de casos y procesos internos
* Persistencia de datos con MySQL
* Uso de Redis
* Variables de entorno para configuraciones sensibles
* Contenerización con Docker
* Orquestación con Docker Compose
* Despliegue en AWS EC2
* Base de datos alojada en AWS RDS
* Proxy inverso con Nginx
* Configuración de dominio y certificados SSL
* Comunicación entre servicios
* Integración entre frontend y backend
* Servicio de notificaciones
* Configuración para entornos públicos y privados

## Arquitectura general

```text
                         ┌─────────────────────────┐
                         │      Cliente web        │
                         │   HTML · CSS · JS       │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │          Nginx          │
                         │ Proxy inverso · HTTPS   │
                         └────────────┬────────────┘
                                      │
                                      ▼
                    ┌───────────────────────────────────┐
                    │       Microservicios Flask       │
                    │            APIs REST             │
                    └───────┬───────────────┬───────────┘
                            │               │
              ┌─────────────┘               └─────────────┐
              ▼                                           ▼
┌──────────────────────────┐                ┌──────────────────────────┐
│          MySQL           │                │          Redis           │
│ Persistencia relacional  │                │ Caché y comunicación     │
└────────────┬─────────────┘                └──────────────────────────┘
             │
             ▼
┌──────────────────────────┐
│       AWS EC2 / RDS      │
│ Infraestructura cloud    │
└──────────────────────────┘
```

## Lo que demuestra este proyecto

GaiaLink evidencia experiencia práctica en:

* Diseño de aplicaciones backend
* Creación e integración de APIs REST
* Organización de servicios independientes
* Modelado y administración de bases de datos
* Comunicación entre contenedores
* Configuración de servidores Linux
* Despliegue de aplicaciones en AWS
* Uso de proxy inverso
* Administración de variables de entorno
* Diagnóstico de errores de infraestructura y red
* Integración de múltiples tecnologías en una sola solución

## Repositorio

**GaiaLink:**

https://github.com/KevinAnzola/Ingenieria_Sistemas/tree/main/Proyecto_GaiaLink

---

# Proyectos destacados

<table>
<tr>
<td width="50%" valign="top">

## Discord Webhook Manager

Aplicación de escritorio desarrollada en Python para administrar webhooks de Discord mediante una interfaz gráfica.

### Funcionalidades

* Envío de mensajes
* Creación de embeds
* Edición de mensajes
* Envío de archivos
* Gestión de hilos
* Comunicación asíncrona
* Integración con la API de Discord

### Tecnologías

`Python` `CustomTkinter` `aiohttp` `Discord API`

### Proyecto

[`Ver carpeta Discord`](./Discord)

</td>
<td width="50%" valign="top">

## Infraestructura AWS

Proyecto enfocado en configuración de infraestructura cloud y despliegue de aplicaciones.

### Trabajo realizado

* Instancias EC2 públicas y privadas
* Bases de datos RDS
* Administración de Linux
* Configuración de seguridad
* Docker y Docker Compose
* Nginx
* Certificados SSL
* Comunicación entre servicios

### Tecnologías

`AWS` `EC2` `RDS` `Linux` `Docker` `Nginx`

### Proyecto

[`Ver Proyecto_AWS`](./Proyecto_AWS)

</td>
</tr>

<tr>
<td width="50%" valign="top">

## GaiaLink Mobile

Exploración móvil del sistema GaiaLink desarrollada con React Native y Expo.

### Objetivos

* Crear una experiencia móvil
* Consumir servicios backend
* Diseñar interfaces adaptadas
* Integrar la aplicación con GaiaLink

### Tecnologías

`React Native` `Expo` `JavaScript`

### Proyecto

[`Ver GaiaLink Mobile`](./Proyecto_Movil/GaiaLink)

</td>
<td width="50%" valign="top">

## GaiaLink Desktop

Primera versión de GaiaLink desarrollada como aplicación de escritorio.

Este proyecto fue la base conceptual antes de la migración hacia Flask, web y microservicios.

### Tecnologías

`Python` `Tkinter`

### Proyecto

[`Ver Proyecto_Python`](./Proyecto_Python)

</td>
</tr>
</table>

---

# Otros proyectos

## Landing page interactiva

Landing page desarrollada para practicar interfaces web, animaciones y JavaScript.

### Funcionalidades

* Diseño responsive
* Animaciones con AOS
* Cuenta regresiva
* Interacciones visuales
* Manipulación del DOM

### Tecnologías

`HTML5` `CSS3` `JavaScript`

[`Ver Proyecto_Laura`](./Proyecto_Laura)

---

## Ejercicios en C#

Colección de ejercicios relacionados con lógica de programación, listas, diccionarios, colecciones y fundamentos de programación orientada a objetos.

### Tecnologías

`C#` `.NET`

[`Ver ejercicios en C#`](./C%23/app)

---

## Proyectos anteriores

Colección de talleres, prácticas y entregas realizadas durante diferentes etapas de mi formación.

Estos proyectos reflejan el proceso de aprendizaje y la evolución de mis habilidades.

[`Ver Proyectos_Anteriores`](./Proyectos_Anteriores)

---

# Tecnologías

<div align="center">

<img src="https://skillicons.dev/icons?i=python,flask,js,html,css,react,mysql,redis,aws,docker,nginx,linux,git,github,vscode&perline=8" alt="Stack tecnológico de Kevin Anzola">

</div>

<br>

<table>
<tr>
<td width="25%" valign="top">

### Backend

* Python
* Flask
* APIs REST
* Microservicios
* aiohttp
* Autenticación
* Integración de APIs

</td>
<td width="25%" valign="top">

### Frontend

* HTML5
* CSS3
* JavaScript
* React Native
* Expo
* Interfaces responsive

</td>
<td width="25%" valign="top">

### Datos

* MySQL
* Redis
* SQL
* Modelado relacional
* Operaciones CRUD
* Persistencia

</td>
<td width="25%" valign="top">

### Cloud y DevOps

* AWS EC2
* AWS RDS
* Docker
* Docker Compose
* Nginx
* Linux
* Git y GitHub

</td>
</tr>
</table>

---

# Competencias técnicas

## Desarrollo backend

* Desarrollo de APIs REST
* Organización de aplicaciones Flask
* Separación de responsabilidades
* Integración entre servicios
* Manejo de peticiones HTTP
* Procesamiento y validación de datos
* Manejo de errores
* Gestión de configuraciones
* Uso de variables de entorno

## Bases de datos

* Diseño de bases de datos relacionales
* Creación y modificación de esquemas
* Relaciones entre tablas
* Consultas SQL
* Operaciones CRUD
* Integración de MySQL con aplicaciones backend
* Uso de Redis para caché y comunicación

## Infraestructura y despliegue

* Administración básica de servidores Linux
* Despliegue de aplicaciones en AWS EC2
* Integración con AWS RDS
* Creación de imágenes Docker
* Configuración de contenedores
* Uso de Docker Compose
* Configuración de Nginx
* Configuración de certificados SSL
* Gestión de dominios
* Diagnóstico de problemas de red

## Herramientas

* Git
* GitHub
* Visual Studio Code
* Docker
* Linux
* Terminal
* Postman
* MySQL Workbench
* Control de versiones

---

# Experiencia práctica

Además de los proyectos académicos, cuento con experiencia en soporte técnico IT, resolución de incidencias y atención de solicitudes mediante herramientas de gestión de tickets.

Esta experiencia me ha permitido fortalecer habilidades como:

* Diagnóstico de problemas
* Comunicación con usuarios
* Resolución de incidencias
* Documentación técnica
* Organización de tareas
* Trabajo bajo procedimientos
* Soporte de sistemas Windows y Linux
* Análisis y seguimiento de solicitudes

---

# Formación

## Fundación Universitaria San Mateo

### Tecnología en Desarrollo de Software

Formación orientada al desarrollo de aplicaciones, programación, bases de datos, infraestructura, análisis de sistemas y construcción de soluciones tecnológicas.

## Formación complementaria

* AWS Academy Cloud Foundations
* Fundamentos de Scrum
* Formación complementaria en inglés
* Aprendizaje continuo mediante proyectos prácticos

---

# Mi evolución

```text
Fundamentos de programación
            │
            ▼
Programación orientada a objetos
            │
            ▼
Aplicaciones de escritorio con Python
            │
            ▼
Desarrollo web con HTML, CSS y JavaScript
            │
            ▼
Backend con Python y Flask
            │
            ▼
APIs REST y bases de datos
            │
            ▼
Microservicios, Docker y Redis
            │
            ▼
Linux, Nginx y AWS
            │
            ▼
Desarrollo móvil con React Native
```

---

# Actualmente

* Mejorando la arquitectura y funcionalidades de GaiaLink
* Fortaleciendo mis conocimientos en Python y Flask
* Trabajando con Docker y servicios de AWS
* Profundizando en diseño de APIs y arquitectura de software
* Explorando desarrollo móvil con React Native
* Mejorando la documentación y organización de mis proyectos
* Aplicando buenas prácticas de seguridad y configuración

---

# Próximos objetivos

* [x] Desarrollo backend con Python
* [x] APIs REST con Flask
* [x] MySQL
* [x] Redis
* [x] Docker
* [x] Docker Compose
* [x] AWS EC2
* [x] AWS RDS
* [x] Nginx
* [x] React Native y Expo
* [ ] Pruebas automatizadas
* [ ] Integración continua
* [ ] GitHub Actions
* [ ] Terraform
* [ ] Kubernetes
* [ ] Observabilidad y monitoreo
* [ ] Arquitecturas orientadas a eventos

---

# Estadísticas de GitHub

<div align="center">

<img height="175" src="https://github-readme-stats.vercel.app/api?username=KevinAnzola&show_icons=true&theme=github_dark&hide_border=true&rank_icon=github" alt="Estadísticas de GitHub de Kevin Anzola">

<img height="175" src="https://github-readme-stats.vercel.app/api/top-langs/?username=KevinAnzola&layout=compact&theme=github_dark&hide_border=true&langs_count=8" alt="Lenguajes más utilizados por Kevin Anzola">

</div>

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com/?user=KevinAnzola&theme=github-dark-blue&hide_border=true" alt="Racha de contribuciones de Kevin Anzola">

</div>

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=KevinAnzola&theme=github-compact&hide_border=true" alt="Actividad de GitHub de Kevin Anzola">

</div>

---

# Qué puedo aportar

* Conocimientos prácticos de desarrollo backend
* Capacidad para construir APIs REST
* Experiencia integrando bases de datos
* Conocimientos de Docker y AWS
* Capacidad para aprender nuevas tecnologías
* Experiencia resolviendo errores técnicos
* Conocimientos de soporte IT
* Adaptabilidad para trabajar en desarrollo e infraestructura
* Compromiso con la mejora continua
* Interés en construir soluciones mantenibles y útiles

---

# Busco oportunidades

Estoy interesado en oportunidades como:

* Desarrollador Backend Junior
* Desarrollador Python Junior
* Desarrollador de Software Junior
* Desarrollador Flask
* Soporte Técnico IT
* Analista de Soporte
* Soporte de Aplicaciones
* DevOps Trainee
* Cloud Support Trainee

Busco formar parte de un equipo donde pueda aportar mis conocimientos, aprender de desarrolladores con más experiencia y continuar creciendo profesionalmente.

---

# Contacto

<div align="center">

### ¿Quieres conocer más sobre mi trabajo?

[![GitHub](https://img.shields.io/badge/GitHub-KevinAnzola-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/KevinAnzola)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Contáctame-0A66C2?style=for-the-badge\&logo=linkedin\&logoColor=white)](TU_LINK_DE_LINKEDIN)

[![Email](https://img.shields.io/badge/Email-Escríbeme-EA4335?style=for-the-badge\&logo=gmail\&logoColor=white)](mailto:TU_CORREO)

<br>

### Proyecto principal

[![GaiaLink](https://img.shields.io/badge/Explorar-GaiaLink-2EA44F?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/KevinAnzola/Ingenieria_Sistemas/tree/main/Proyecto_GaiaLink)

</div>

---

<div align="center">

## Gracias por visitar mi repositorio

Este repositorio representa mi evolución, mi experiencia práctica y mi compromiso con el desarrollo de software.

Desarrollado por **Kevin Anzola**

</div>
