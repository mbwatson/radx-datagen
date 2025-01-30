FROM python:3.12

WORKDIR /app/api

# copy requirements files
COPY Pipfile Pipfile.lock .

# install dependencies
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# copy in application files
COPY . .

EXPOSE 8888

# environment variables
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=$UI_PORT
ENV FLASK_ENV=$UI_ENV

# go!
CMD ["pipenv", "run", "flask", "run"]
