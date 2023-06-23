# Your Python version
FROM python:3.11-bookworm

# Web port of the application
EXPOSE 5001

# Install your application
WORKDIR /app
COPY . /app
RUN pip install -r venv_requirements.txt

# Start up command
ENTRYPOINT ["python" , "-m", "main", "--host=0.0.0.0"]