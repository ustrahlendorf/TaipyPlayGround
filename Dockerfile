# Your Python version
FROM python:3.9

# Web port of the application
EXPOSE 5000

# Install your application
WORKDIR /app
COPY . /app
RUN pip install -r venv_requirements.txt

# Start up command
ENTRYPOINT ["python" , "-m", "main", "--host=0.0.0.0"]