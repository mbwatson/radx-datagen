FROM python:3.12

WORKDIR /app

# copy in requirements file
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy in application files
COPY . .

# expose port
EXPOSE ${UI_PORT}

# environment variables
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=${API_PORT}
ENV FLASK_ENV=${API_ENV}

# go!
CMD ["python", "app.py"]
