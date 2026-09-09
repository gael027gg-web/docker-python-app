# Usar imagen base de Python
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo app.py al contenedor
COPY app.py .

# Ejecutar el script al iniciar el contenedor
CMD ["python", "app.py"]