# RADx Synthetic Data Generator

## 🚧 Development

1. clone this repo & move into project root
2. spin up development `api` and `ui` servers: `docker compose up`
```bash
$ docker compose up
WARN[0000] /home/matt/dev/renci/radx/radx-datagen/docker-compose.yaml: `version` is obsolete 
[+] Running 2/0
 ✔ Container radx-datagen-api-1  Created                                                                                0.0s 
 ✔ Container radx-datagen-ui-1   Created                                                                                0.0s 
Attaching to api-1, ui-1
ui-1   |  * Serving Flask app 'app.py'
ui-1   |  * Debug mode: off
ui-1   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
ui-1   |  * Running on all addresses (0.0.0.0)
ui-1   |  * Running on http://127.0.0.1:8855
ui-1   |  * Running on http://172.18.0.3:8855
ui-1   | Press CTRL+C to quit
ui-1   | 172.18.0.1 - - [30/Jan/2025 18:34:32] "GET /_reload-hash HTTP/1.1" 200 -
ui-1   | 172.18.0.1 - - [30/Jan/2025 18:34:34] "GET /_reload-hash HTTP/1.1" 200 -
api-1  |  * Serving Flask app 'api.py'
api-1  |  * Debug mode: off
api-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
api-1  |  * Running on all addresses (0.0.0.0)
api-1  |  * Running on http://127.0.0.1:8888
api-1  |  * Running on http://172.18.0.2:8888
api-1  | Press CTRL+C to quit
ui-1   | 172.18.0.1 - - [30/Jan/2025 18:34:37] "GET /_reload-hash HTTP/1.1" 200 -
```
3. You now should be able to view the UI in your browser at [http://localhost:8855/](http://localhost:8855/)`
and hit the API at [http://localhost:8888/](http://localhost:8888/).
