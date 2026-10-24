# ProyectoGIT

Repositorio educativo para practicar **Git y GitHub** junto con ejercicios básicos de **Python**. Incluye funciones aritméticas con pruebas automatizadas, ejemplos de scripts, un notebook de demostración y una página HTML estática.

## Contenido

- **Git y GitHub:** el [plan de aprendizaje](plan.md) reúne temas y comandos de control de versiones.
- **Python:** funciones para sumar, restar y multiplicar en `src/calculadora.py`.
- **Pruebas:** casos para las operaciones de la calculadora en `tests/test_calculadora.py`.
- **Scripts de ejemplo:** `hola.py` muestra los archivos del directorio actual; `leer_claves.py` comprueba si existe la variable `OPENAI_API_KEY`.
- **Notebook:** `notebooks/demo.ipynb` contiene ejemplos introductorios.
- **Página estática:** `index.html` es una maqueta visual de portafolio que puede abrirse directamente en un navegador.

## Requisitos

- Python 3 instalado. El notebook está configurado con un kernel de Python 3.12.7.
- `pip` para instalar las dependencias declaradas en `requirements.txt`.

## Instalación

Desde la raíz del repositorio, crea y activa un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

En macOS o Linux, activa el entorno con:

```bash
source .venv/bin/activate
```

Instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Uso

Ejecuta las pruebas de la calculadora desde la raíz del repositorio:

```bash
python -m pytest
```

También puedes importar las funciones desde Python:

```python
from src.calculadora import multiplicar, restar, sumar

print(sumar(2, 3))
print(restar(10, 2))
print(multiplicar(4, 5))
```

Para abrir el notebook:

```bash
jupyter notebook notebooks/demo.ipynb
```

Para ver la maqueta, abre `index.html` en un navegador. No requiere servidor ni proceso de compilación.

## Variables de entorno (opcional)

El script `leer_claves.py` usa `python-dotenv` para leer un archivo `.env`. Si necesitas ejecutar ese ejemplo, instala la dependencia opcional:

```bash
python -m pip install python-dotenv
```

Copia `.env.example` a `.env` y asigna el valor de `OPENAI_API_KEY` solo si corresponde. El script únicamente comprueba si la variable está definida; **no realiza llamadas a la API**. No publiques ni compartas el archivo `.env` ni claves reales.

## Estructura del repositorio

```text
.
├── data/                       # Espacio reservado para datos
├── models/                     # Espacio reservado para modelos
├── notebooks/
│   └── demo.ipynb              # Notebook de demostración
├── src/
│   ├── calculadora.py          # Operaciones aritméticas
│   └── calculadora2.py         # Ejemplo adicional de suma
├── tests/
│   └── test_calculadora.py     # Pruebas de la calculadora
├── .env.example                # Plantilla de variable de entorno
├── hola.py                     # Ejemplo de listado de archivos
├── index.html                  # Maqueta estática de portafolio
├── plan.md                     # Plan de aprendizaje de Git y GitHub
└── requirements.txt            # Dependencias del entorno
```

## Contribuciones

Este repositorio sirve para practicar el flujo colaborativo de Git y GitHub. Para proponer un cambio, crea una rama, realiza commits descriptivos y abre un pull request. Ejecuta las pruebas antes de enviar cambios relacionados con la calculadora.
