# Synthetic Data Generator

## 🚧 Development

To develop both the API and UI simultaneously, we can spin up both.

1. clone this repo & move into project root
2. spin up development API and UI servers: `docker compose up`
3. You now should be able to view the UI in your browser at [http://localhost:8855/](http://localhost:8855/) and hit the API at [http://localhost:8888/](http://localhost:8888/).
4. CTRL+C to quit.

Note: To run _only_ the API or only the UI, one simply runs `docker compose up api` or `docker compose up ui`.

The source directories are mounted into the containers,
so editing locally works as expected, complete with hot module reloading.

## 🎁 Production

There is a `docker-compose.prod.yaml` file for production deployment that will likely need modification, but we're not there yet. To use it anyway, use `docker compose -f docker-compose.prod.yaml up`.

## 🌉 Architecture

The application is comprised of two parts: an API and a UI.
The API is a [Flask](https://flask.palletsprojects.com/en/stable/) app.
The frontend is a [Dash](https://dash.plotly.com/) app.

## 📝 The Temporary Real Data

ChatGPT was given this prompt:

> generate a CSV with 1000 rows having columns
> `first_name`, `last_name`, `age`, and `has_disease_x`,
> with the following specifications:
> 
> - 500 rows represent people aged below 60,
>   50 of which have `has_disease_x=True`.
>   The other 450 have `has_disease_x=False`.
> 
> - 500 rows represent people aged 60 or older,
>   450 of which have `has_disease_x=True`.
>   The remaining 50 have `has_disease_x=False`.

The distribution of `has_disease_x` is summarized in the following table.

|                       | `age < 60` | `60 ≤ age` |
| --------------------: | :--------: | :--------: |
|  `has_disease_x=True` |     50     |    450     |
| `has_disease_x=False` |    450     |     50     |
|                 total |    500     |    500     |

The API utilizes this
[data](https://github.com/mbwatson/radx-datagen/blob/dev/api/data/real_data.csv),
as temporary real data, to generate synthetic data with [SDV](https://docs.sdv.dev/sdv).
