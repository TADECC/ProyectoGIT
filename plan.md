# Plan de Aprendizaje Git y GitHub
## Daniel Eduardo Casallas Castellanos

Última actualización: Octubre 2026

---

# Estado General

✅ Completado
🔄 En progreso
⬜ Pendiente

---

# Nivel 1 - Conceptos Fundamentales

Estado: ✅ Completado

Temas:

- ¿Qué es Git?
- ¿Qué es GitHub?
- Repositorio local
- Repositorio remoto
- Control de versiones
- Flujo básico de trabajo

Comandos aprendidos:

```bash
git --version
git init
git status
```

---

# Nivel 2 - Commits Básicos

Estado: ✅ Completado

Temas:

- Área de trabajo
- Área de preparación (Staging Area)
- Commit

Comandos aprendidos:

```bash
git add .
git add archivo
git commit -m "mensaje"
```

---

# Nivel 3 - Conexión con GitHub

Estado: ✅ Completado

Temas:

- Repositorios remotos
- Origin
- Push inicial

Comandos aprendidos:

```bash
git remote add origin URL
git push -u origin main
git remote -v
```

---

# Nivel 4 - Configuración de Git

Estado: ✅ Completado

Temas:

- Identidad de autor
- Configuración global

Comandos aprendidos:

```bash
git config --global user.name
git config --global user.email
git config --list
```

---

# Nivel 5 - Inspección del Repositorio

Estado: ✅ Completado

Temas:

- Estado del repositorio
- Historial
- Visualización de cambios

Comandos aprendidos:

```bash
git status
git log
git log --oneline
git show
git diff
```

---

# Nivel 6A - Flujo Diario de Trabajo

Estado: ✅ Completado

Temas:

- Modificar archivos
- Preparar cambios
- Crear commits
- Publicar cambios

Flujo dominado:

```bash
git diff
git add .
git commit -m "mensaje"
git push
```

---

# Nivel 6B - Recuperación Básica

Estado: ✅ Completado

Temas:

- Descartar cambios
- Quitar archivos del staging
- Revertir commits

Comandos aprendidos:

```bash
git restore archivo
git restore --staged archivo
git revert HEAD
```

---

# Nivel 7 - Ramas (Branches)

Estado: ✅ Completado

Temas:

- Crear ramas
- Cambiar de rama
- Merge local
- Comparar ramas

Comandos aprendidos:

```bash
git branch
git switch
git switch -c rama
git merge rama

git diff main..HEAD
git log main..HEAD --oneline
```

Conceptos consolidados:

- main
- ramas de funcionalidad
- merge
- comparación entre ramas

---

# Nivel 8 - Pull Requests

Estado: ✅ Completado

Temas:

- Flujo profesional GitHub
- Pull Request
- Merge desde GitHub
- Eliminación de ramas

Flujo dominado:

```text
feature branch
      ↓
commit
      ↓
push
      ↓
Pull Request
      ↓
Merge
      ↓
git pull
```

---

# Nivel 9 - Conflictos de Merge

Estado: ✅ Completado

Temas:

- Conflictos
- Resolución manual
- Conflictos en GitHub
- Conflictos en VS Code

Comandos aprendidos:

```bash
git merge rama
git status
git add archivo
git commit
```

Marcadores comprendidos:

```text
<<<<<<< HEAD
=======
>>>>>>> rama
```

---

# Nivel 10 - Rebase

Estado: ✅ Completado

Temas:

- Diferencia Merge vs Rebase
- Historia lineal
- Actualización de ramas

Comandos aprendidos:

```bash
git rebase main
git rebase --continue
git rebase --abort
```

---

# Nivel 11 - Git Stash

Estado: ✅ Completado

Temas:

- Guardar trabajo temporal
- Recuperar trabajo temporal

Comandos aprendidos:

```bash
git stash
git stash list
git stash apply
git stash pop
git stash drop
```

---

# Nivel 12 - Viajes en el Tiempo

Estado: ✅ Completado

Temas:

- Checkout de commits antiguos
- Reset
- Revert

Comandos aprendidos:

```bash
git show HEAD
git switch --detach

git revert HEAD

git reset --soft
git reset
git reset --hard
```

---

# Nivel 13 - Recuperación de Desastres

Estado: ✅ Completado

Temas:

- Reflog
- Recuperación de commits
- Recuperación de ramas

Comandos aprendidos:

```bash
git reflog
```

Capacidades adquiridas:

- Recuperar commits eliminados
- Recuperar resets erróneos
- Recuperar ramas borradas

---

# Nivel 14 - Tags y Releases

Estado: ✅ Completado

Temas:

- Versionado
- Releases

Comandos aprendidos:

```bash
git tag
git tag -a

git show tag

git push --tags
```

Conceptos:

```text
v1.0.0
v1.1.0
v2.0.0
```

---

# Nivel 15 - Cherry Pick

Estado: ✅ Completado

Temas:

- Copiar commits entre ramas

Comandos aprendidos:

```bash
git cherry-pick HASH

git cherry-pick --continue

git cherry-pick --abort
```

---

# Nivel 16 - Flujo Profesional Completo

Estado: ✅ Completado

Temas:

- Flujo empresarial moderno
- Buenas prácticas

Proceso dominado:

```text
main
 ↓
feature
 ↓
commits
 ↓
push
 ↓
pull request
 ↓
merge
 ↓
main
```

---

# Nivel 17 - Git para IA y Ciencia de Datos

Estado: ✅ Completado

Temas:

- Estructura profesional de proyectos
- .gitignore para IA
- Modelos y datasets
- Reproducibilidad
- Git LFS

Estructura recomendada:

```text
data/
models/
notebooks/
src/
results/
README.md
requirements.txt
```
---

# Nivel 18 - GitHub Pages

Estado: ✅ Completado

Objetivos:

- Publicar sitios web desde GitHub
- Portafolio profesional
- Página de proyectos
- Difusión académica

Temas:

- index.html
- GitHub Pages
- Publicación automática

---

---

# Próximos Niveles

---

# Nivel 19 - GitHub Actions

Estado: ✅ Completado

Objetivos:

- Automatización

Temas:

- CI/CD
- Workflows
- Automatización de pruebas
- Automatización de despliegues
- Artefactos

---

# Nivel 20 - GitHub para Investigación y Docencia

Estado: ⬜ Pendiente

Objetivos:

- Organización de tesis
- Publicación académica
- Repositorios reproducibles

Temas:

- documentación científica
- proyectos de investigación
- colaboración académica

---

# Nivel 21 - Proyecto Integrador

Estado: ⬜ Pendiente

Objetivos:

Construir un repositorio profesional completo con:

- ramas
- pull requests
- tags
- releases
- github pages
- documentación
- estructura para IA

Resultado esperado:

Repositorio listo para portafolio profesional.

# Nivel 22 - Desarrollo Asistido por IA
# Git + GitHub + Claude Code

Estado: ⬜ Pendiente

Objetivos:

Integrar Git, GitHub y Claude Code dentro de un flujo moderno de desarrollo profesional.

---

## Conceptos Fundamentales

Comprender el papel de cada herramienta:

```text
Git         → Control de versiones

GitHub      → Colaboración y repositorio remoto

Claude Code → Agente de desarrollo asistido por IA
```

---

## Configuración Inicial

Temas:

- Instalación de Claude Code
- Autenticación
- Integración con VS Code
- Acceso a repositorios Git

---

## Flujo Profesional de Desarrollo

Proceso recomendado:

```text
Issue
 ↓
Crear rama
 ↓
Claude Code implementa cambios
 ↓
Revisión humana
 ↓
Tests
 ↓
Commit
 ↓
Push
 ↓
Pull Request
 ↓
Merge
```

---

## Trabajo con Repositorios Existentes

Capacidades:

- Exploración de repositorios
- Comprensión de arquitectura
- Análisis de código
- Generación de documentación
- Refactorización

Ejemplos:

```text
Explica este proyecto.

Documenta este módulo.

Refactoriza esta función.

Genera pruebas unitarias.
```

---

## Buenas Prácticas con Git

Antes de solicitar cambios:

```bash
git switch -c feature-nueva-funcionalidad
```

Después de los cambios:

```bash
git diff
```

Validar siempre:

```bash
git status
git diff
git log
```

Antes de:

```bash
git add
git commit
git push
```

---

## Pull Requests Asistidos por IA

Temas:

- Resúmenes automáticos
- Explicación de commits
- Documentación automática
- Revisiones preliminares

---

## Aplicación en Ciencia de Datos e IA

Uso profesional para:

- Deep Learning
- Machine Learning
- Ciencia de Datos
- Automatización
- Investigación académica
- Desarrollo experimental

---

## Limitaciones y Validación

Comprender que:

```text
La IA acelera el desarrollo
```

pero no reemplaza:

```text
Validación humana
```

Siempre verificar:

- Correctitud
- Seguridad
- Rendimiento
- Reproducibilidad
- Interpretabilidad

---

## Proyecto Final del Programa

Construir un proyecto completo utilizando:

✅ Git

✅ GitHub

✅ Pull Requests

✅ GitHub Pages

✅ GitHub Actions

✅ Claude Code

✅ Documentación profesional

Resultado esperado:

Repositorio profesional listo para:

- Portafolio
- Investigación
- Consultoría
- Docencia
- Desarrollo de IA