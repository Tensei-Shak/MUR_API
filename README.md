# APIESP32 - FastAPI

API para la comunicación con un dispositivo ESP32. Esta API permite insertar y recuperar datos relacionados con un simulador que realiza cálculos sobre tiempo, desplazamiento, velocidad y aceleración, todo gestionado a través de un servidor FastAPI.

## Descripción

Este proyecto contiene una API RESTful construida con **FastAPI**. La API está diseñada para recibir y almacenar datos relacionados con simulaciones de un ESP32, y permitir la consulta de estos datos a través de varios endpoints.

### Características

- **Inserción de datos**: Permite insertar datos de simulación.
- **Consulta de datos**: Permite consultar todos los datos insertados o filtrarlos por `group_id`.
- **Soporte para CORS**: Para permitir la interacción con aplicaciones frontend ubicadas en diferentes dominios.

## Instalación

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. **Crea un entorno virtual** (opcional pero recomendado):

    ```bash
    python -m venv .venv
    ```

3. **Activa el entorno virtual**:

    - **Windows**:
    
        ```bash
        .venv\Scripts\activate
        ```

    - **Linux/macOS**:
    
        ```bash
        source .venv/bin/activate
        ```

4. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Levantar el servidor

Para iniciar el servidor FastAPI, ejecuta el siguiente comando:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
