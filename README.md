# RADx Synthetic Data Generator

## 🚧 Development

1. clone this repo & move into project dir

The API and UI are both Python apps that live in their own directories, `./api` and `./ui`.
These instructions use [Pipenv](https://pipenv.pypa.io/en/latest/), but any virtualenv management tool works fine.

2. API development
  - change into `api` directory
  - start virtual environment, `pipenv shell`
  - install dependencies, `pipenv install`
  - start dev server, `python app.py`

3. UI development
  - change into `ui` directory
  - start virtual environment, `pipenv shell`
  - install dependencies, `pipenv install`
  - start dev server, `python app.py`

4. You now should be able to view the UI in your browser at [http://localhost:8855/](http://localhost:8855/)`
and hit the API at [http://localhost:8888/](http://localhost:8888/).

```bash
$ python app.py
Dash is running on http://127.0.0.1:8855/

 * Serving Flask app 'app'
 * Debug mode: on
```

## 📦 Production

We have included a Dockerfile to build a production app server image.

1. build Docker image, `docker build -t radx-synth-datagen .`
2. run container, `docker run --rm -p 80:8050 radx-synth-datagen`
```bash
$ docker run --rm -p 80:8855 radx-synth-datagen
[2025-01-16 15:28:42 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2025-01-16 15:28:42 +0000] [1] [INFO] Listening at: http://0.0.0.0:8050 (1)
