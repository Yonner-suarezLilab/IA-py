FROM python:3.8-slim

# Set the working directory to /api
WORKDIR /app

# Copy the current directory contents into the container at /api
COPY . /app

# Agregar un usuario no privilegiado
RUN adduser --disabled-password myuser

# Instalar Git
RUN apt-get update && apt-get install -y git

# Instalar Instantneo desde GitHub
RUN pip install git+https://github.com/dponcedeleonf/instantneo.git

RUN pip install --no-cache-dir -r app/requirements.txt && \
    rm -rf /var/lib/apt/lists/*

# Cambiar al usuario no privilegiado
USER myuser

CMD ["flask", "--app=app", "run", "--host=0.0.0.0", "--port=8000", "--debug"]
