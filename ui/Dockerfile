FROM python:3.12

WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application files into the container
COPY . .

# Expose the necessary port
EXPOSE ${UI_PORT}

# Environment variables
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=${API_PORT}
ENV FLASK_ENV=${API_ENV}

# Start the Flask app
CMD ["python", "-m", "flask", "run"]
