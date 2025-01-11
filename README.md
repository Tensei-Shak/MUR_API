# APIESP32

API desarrollada en FastAPI para gestionar datos enviados por un ESP32. La API permite insertar datos, obtener todos los datos almacenados y filtrar datos por `group_id`.

## Requisitos

- **Python**: Versión 3.9 o superior.
- **Framework**: FastAPI.
- **Base de datos**: SQLite.
- **Servidor**: uvicorn.

## Instalación

Sigue los pasos a continuación para configurar y ejecutar el proyecto:

1. **Clona este repositorio**:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta el servidor de desarrollo**:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Accede a la documentación de la API**:

   - Documentación interactiva: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Documentación en formato OpenAPI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Estructura del Proyecto

La organización del proyecto es la siguiente:

```plaintext
.
├── app/
│   ├── __init__.py        # Inicializador del módulo
│   ├── database.py        # Configuración y conexión a la base de datos
│   ├── models.py          # Modelos de datos
│   ├── schematics.py      # Funciones CRUD
├── main.py                # Archivo principal de la API
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentación del proyecto
```

## Endpoints Disponibles

### 1. POST `/api/prototype/insert`

Permite insertar datos de simulación en la base de datos.

#### **Request Body**:

```json
{
  "group_id": "string",
  "time": 123,
  "displacement": 1.23,
  "velocity": 2.34,
  "acceleration": 3.45
}
```

#### **Response**:

```json
{
  "group_id": "string",
  "time": 123,
  "displacement": 1.23,
  "velocity": 2.34,
  "acceleration": 3.45,
  "id": 1
}
```

---

### 2. GET `/api/prototype/view`

Obtiene todos los datos almacenados en la base de datos.

#### **Response**:

```json
[
  {
    "group_id": "string",
    "time": 123,
    "displacement": 1.23,
    "velocity": 2.34,
    "acceleration": 3.45,
    "id": 1
  },
  {
    "group_id": "string",
    "time": 456,
    "displacement": 4.56,
    "velocity": 5.67,
    "acceleration": 6.78,
    "id": 2
  }
]
```

---

### 3. GET `/api/prototype/view/{group_id}`

Obtiene los datos almacenados filtrados por `group_id`.

#### **Response**:

```json
[
  {
    "group_id": "group2",
    "time": 123,
    "displacement": 1.23,
    "velocity": 2.34,
    "acceleration": 3.45,
    "id": 1
  }
]
```
