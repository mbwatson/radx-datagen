# RADx Synthetic Data Generator

## 🚧 Development

To develop both the API and UI simultaneously, we can spin up both.

1. clone this repo & move into project root
2. spin up development API and UI servers: `docker compose up`
3. You now should be able to view the UI in your browser at [http://localhost:8855/](http://localhost:8855/) and hit the API at [http://localhost:8888/](http://localhost:8888/).
4. CTRL+C to quit.

Note: To run _only_ the API or only the UI, one simply runs `docker compose up api` or `docker compose up ui`.

## 🎁 Production

There is a `docker-compose.prod.yaml` file for production deployment that will likely need modification, but we're not there yet. To use it anyway, use `docker compose -f docker-compose.prod.yaml up`.
