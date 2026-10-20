# Plan de Aprendizaje Git, GitHub y VS Code

**Última sesión completada:** 18/10/2026

**Estado actual:** Nivel 5 completado.

---

# Nivel 1: Fundamentos de Git

## Completado

✅ ¿Qué es Git?

✅ ¿Qué es GitHub?

✅ Configuración inicial de Git

✅ Configuración de usuario (user.name, user.email)

✅ Crear repositorios con `git init`

✅ Conexión entre VS Code y Git

✅ `git add`

✅ `git commit`

✅ `git push`

✅ Primer repositorio en GitHub

✅ Sincronización local → remoto

---

# Nivel 2: Trabajar con repositorios remotos

## Completado

✅ `git clone`

✅ `git pull`

✅ Repositorio local vs remoto

✅ Interpretación básica de `git status`

✅ Sincronización con GitHub

---

# Nivel 3: Ramas (Branches)

## Completado

✅ ¿Qué es una rama?

✅ `git branch`

✅ `git checkout`

✅ Creación de ramas

✅ Fusión de ramas (`merge`)

✅ Flujo de trabajo paralelo

✅ Concepto de desarrollo aislado

---

# Nivel 4: Git en VS Code

## Completado

✅ Source Control

✅ Git Graph

✅ GitLens

✅ Navegación por historial

✅ Visualización gráfica de commits

✅ Integración Git-GitHub desde VS Code

---

# Nivel 5: Exclusión de archivos y gestión básica de credenciales

## Completado

✅ Creación de `.gitignore`

✅ Archivos ignorados por Git

✅ Archivos rastreados por Git

✅ Diferencia entre archivos locales y archivos versionados

✅ Gestión básica de credenciales

✅ Creación de `.env`

✅ Creación de `.env.example`

✅ Uso de `python-dotenv`

✅ Lectura de variables de entorno

✅ Uso de `git ls-files`

✅ Verificación de archivos rastreados

✅ Buenas prácticas para proyectos Python

✅ Comprensión de riesgos de exponer API Keys

✅ Buenas prácticas para OpenAI, Gemini y otras APIs

---

# Próxima sesión

# Nivel 6A: Flujo diario de trabajo con Git

## Objetivo

Comprender el ciclo de trabajo que se utiliza todos los días en proyectos reales.

## Temas pendientes

⬜ Modificar archivos existentes

⬜ Interpretar cambios con `git status`

⬜ Analizar cambios con `git diff`

⬜ Añadir cambios con `git add`

⬜ Crear commits incrementales

⬜ Buenas prácticas para mensajes de commit

⬜ Consultar historial con `git log`

⬜ Leer commits con `git show`

⬜ Comprender el ciclo completo:

```text
Modificar
     ↓
git diff
     ↓
git add
     ↓
git commit
     ↓
git push
```

## Ejercicios

```bash
git diff
git add
git commit
git log --oneline
git show
```

---

# Nivel 6B: Resolución de conflictos

## Objetivo

Resolver conflictos de forma segura.

## Temas pendientes

⬜ ¿Qué es un conflicto?

⬜ Cómo se produce un conflicto

⬜ Cómo detectarlo

⬜ Resolución manual

⬜ Resolución usando VS Code

⬜ Buenas prácticas de colaboración

## Ejercicios

⬜ Crear conflicto controlado

⬜ Resolver conflicto manual

⬜ Resolver conflicto desde VS Code

⬜ Completar merge exitoso

---

# Nivel 7: Pull Requests (PR)

## Objetivo

Trabajar como en equipos profesionales.

## Temas pendientes

⬜ Crear ramas para funcionalidades

⬜ Publicar ramas en GitHub

⬜ Crear Pull Requests

⬜ Revisar cambios

⬜ Aprobar cambios

⬜ Merge de Pull Requests

⬜ Flujo profesional de colaboración

## Comandos clave

```bash
git checkout -b nueva_funcionalidad

git push -u origin nueva_funcionalidad
```

---

# Nivel 8: GitHub Pages y visualización de resultados

## Objetivo

Publicar páginas web directamente desde GitHub para mostrar proyectos, investigaciones y resultados de modelos.

## Temas pendientes

⬜ ¿Qué es GitHub Pages?

⬜ Activar GitHub Pages

⬜ Publicar una página HTML básica

⬜ Publicar documentación de proyectos

⬜ Crear un portafolio profesional

⬜ Mostrar imágenes y gráficos

⬜ Uso de Markdown para páginas web

⬜ Introducción a Jekyll

⬜ Organización de sitios públicos

## Aplicaciones prácticas

⬜ Publicar resultados de Machine Learning

⬜ Mostrar métricas de modelos

⬜ Mostrar gráficos de Python

⬜ Publicar resultados de tesis

⬜ Crear páginas de proyectos académicos

⬜ Construir portafolio profesional

## Proyecto práctico

Construir un sitio web público que incluya:

- Descripción del proyecto
- Objetivos
- Resultados
- Imágenes
- Gráficos
- Enlace al repositorio GitHub

### Flujo

```text
Repositorio GitHub
        │
        ▼
GitHub Pages
        │
        ▼
Página Web Pública
```

### Resultado esperado

```text
https://usuario.github.io/proyecto/
```

---

# Nivel 9: Git para Ciencia de Datos e IA

## Objetivo

Gestionar proyectos profesionales de Python, Data Science y Deep Learning.

## Estructura profesional

```text
Proyecto/
│
├── data/
├── models/
├── notebooks/
├── src/
├── tests/
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Temas pendientes

⬜ Organización profesional de proyectos

⬜ Manejo de datasets

⬜ Control de notebooks

⬜ Reproducibilidad

⬜ Control de modelos entrenados

⬜ Git LFS

⬜ Versionado de experimentos

⬜ Gestión avanzada de credenciales

⬜ Buenas prácticas de investigación reproducible

---

# Nivel 10: GitHub Actions

## Objetivo

Automatizar tareas mediante integración continua.

## Temas pendientes

⬜ Introducción a GitHub Actions

⬜ Workflows

⬜ Integración continua (CI)

⬜ Ejecución automática de pruebas

⬜ Automatización de reportes

⬜ Automatización de despliegues

⬜ Introducción a CI/CD

### Flujo

```text
Push
 ↓
Validación
 ↓
Pruebas
 ↓
Reporte
 ↓
Despliegue
```

---

# Nivel 11: Flujo profesional completo

## Objetivo

Integrar Git, GitHub y automatización en proyectos reales.

## Flujo profesional

```text
VS Code
 ↓
Git
 ↓
Branch
 ↓
Commit
 ↓
Push
 ↓
Pull Request
 ↓
Review
 ↓
Merge
 ↓
GitHub Actions
 ↓
GitHub Pages
 ↓
Release
```

## Metas finales

⬜ Gestionar repositorios profesionales

⬜ Trabajar colaborativamente

⬜ Resolver conflictos con seguridad

⬜ Mantener proyectos reproducibles

⬜ Publicar documentación profesional

⬜ Crear portafolios técnicos

⬜ Mostrar resultados de IA y Ciencia de Datos

⬜ Automatizar pruebas y despliegues

⬜ Mantener buenas prácticas de seguridad

⬜ Gestionar proyectos académicos y profesionales con Git y GitHub

---

# Verificación antes de la próxima sesión

Ejecutar:

```bash
git status
```

Resultado esperado:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Si el repositorio está limpio, continuaremos directamente con:

## Nivel 6A: Flujo diario de trabajo con Git

- `git diff`
- `git log`
- `git show`
- Modificar → Commit → Push