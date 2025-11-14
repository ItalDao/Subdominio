# IMAGEN BASE Python 3.12
FROM python:3.12-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 1001

# Ejecutar la aplicación 
CMD ["python","app.py"]