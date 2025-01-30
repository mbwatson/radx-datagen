FROM python:3.12

WORKDIR /app/ui

# copy requirements files
COPY Pipfile Pipfile.lock .

# install dependencies
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# copy in application files
COPY . .

EXPOSE 8855

# environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8855
ENV FLASK_ENV=production

# go!
CMD ["pipenv", "run", "flask", "run"]
