<<<<<<< HEAD
=======
# Calculadora de Consola en Python

Aplicación de consola desarrollada en Python que permite realizar operaciones matemáticas básicas de forma segura, controlada y con manejo de errores.

Este proyecto fue desarrollado siguiendo metodología Scrum (sprints cortos) y control de versiones con Git.

---

## Objetivo

Desarrollar una aplicación de consola en Python que funcione como una calculadora básica, permitiendo al usuario realizar operaciones matemáticas simples sin que el sistema falle ante errores de entrada.

---

## Alcance Funcional (MVP)

La aplicación permite:

- Sumar
- Restar
- Multiplicar
- Dividir
- Salir del programa

### Validaciones implementadas

- Verificación de que los valores ingresados sean números (`try / except`)
- Validación de división por cero
- Validación de opción de menú
- El programa nunca se rompe por errores del usuario
- Permite múltiples operaciones hasta que el usuario decida salir

---

## Requisitos Técnicos

- Lenguaje: **Python**
- Uso obligatorio de:
  - `if / elif / else`
  - `try / except`
- Código organizado en funciones
- Archivo principal: `main.py`
- Mensajes claros en consola

---

## Estructura del Proyecto

```
calculadora/
│── main.py
│── README.md
```

---

## Metodología Scrum

El proyecto se desarrolló en sprints cortos:

### Sprint 1
- Mostrar menú
- Implementar suma y resta
- Manejo básico de errores

### Sprint 2
- Agregar multiplicación y división
- Validación de división por cero
- Organización en funciones

### Sprint 3
- Mejoras en experiencia de usuario
- Validaciones más robustas
- Limpieza y refactorización

---

## Flujo de Trabajo con Git

Estructura de ramas utilizada:

- `main`
- `develop`
- `feature/menu`
- `feature/Procesos`
- `feature/validaciones`

Prácticas aplicadas:

- `git checkout -b`
- `git merge`
- Resolución de conflictos simples
- Commits claros y descriptivos

Ejemplo de buen commit:

```
feat: agregar validación de división por cero
```

---

## Historia de Usuario

**Como usuario**  
Quiero realizar operaciones matemáticas básicas  
Para obtener resultados sin que el sistema falle ante errores  

---

## Criterios de Aceptación

- El programa nunca debe cerrarse por un error de entrada.
- Debe seguir ejecutándose hasta que el usuario elija salir.
- Debe mostrar mensajes claros y entendibles.
- El código debe estar organizado en funciones.

---

## Mejoras Opcionales

- Contador de operaciones realizadas
- Historial simple de operaciones
- Confirmación antes de salir
- Refactorización adicional

---

## Autores

- Jesus Lucena.
- Aura Alean.
- Nicholas De la Rosa.
- Jhon Salgado.
- Yasir Quintero.

Proyecto académico / práctica profesional
>>>>>>> bb17a3e26c06c2bffb68e5137561d0828ac0e83d
