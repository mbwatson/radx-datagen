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

## About the Data

ChatGPT was given this prompt:

> generate a CSV with 1000 rows having columns
> `first_name`, `last_name`, `age`, and `has_disease_x`,
> with the following specifications:
> 
> - 500 rows represent people aged below 60,
>   50 of which have `has_disease_x=True`. The other 450 have `has_disease_x=False`.
> 
> - 500 rows represent people aged 60 or older, 450 of which have `has_disease_x=True`. The remaining 50 have `has_disease_x=False`.

In summary, the distribution of `has_disease_x` is summarized as in the following table.

|                       | `age < 60` | `age ≥ 60` |
| --------------------: | :--------: | :--------: |
|  `has_disease_x=True` |     50     |    450     |
| `has_disease_x=False` |    450     |     50     |
|                 total |    500     |    500     |

The API utilizes SDV with this data (as temporary real data) to generate synthetic data, which is accessed at the `/generate/radx` endpoint.
