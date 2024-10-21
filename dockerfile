FROM fedora

# Install dependencies

RUN yum install -y apt-transport-https
RUN yum install -y python-pip
RUN yum install -y stockfish
# Set the working directory inside the container
WORKDIR /app


# Copy the requirements file to the working directory
COPY requirements.txt .
COPY config.toml .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
