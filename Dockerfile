# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el script de Python al contenedor
COPY sip_server.py .

# Instalar dependencias (si las hay)
# RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto SIP
EXPOSE 5060/udp

# Comando para ejecutar el script de Python
CMD ["python", "sip_server.py"]
