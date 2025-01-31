from flask import Flask, jsonify, request
from sdv.datasets import demo
from sdv.single_table import GaussianCopulaSynthesizer
from uuid import uuid4

app = Flask(__name__)

available_demos = demo.get_available_demos(modality='single_table')
available_datasets = [{
    "name": record['dataset_name'],
    "url": f"http://localhost:8888/generate/{record['dataset_name']}",
} for record in available_demos.to_dict(orient='records')]

# curl -X GET http://localhost:8888/
@app.route('/', methods=['GET'])
def list_endpoints():
    endpoints = {
        "/": "This response.",
        "/list_datasets": "List available datasets.",
        "/generate/<string:dataset_name>/<int:count>": "Generate count records in dataset_name.",
    }
    return jsonify(endpoints), 200

# curl -X GET http://localhost:8888/list_datasets
@app.route('/list_datasets', methods=['GET'])
def list_datasets():
    return available_datasets, 200

# curl -X POST http://localhost:8888/generate -H "Content-Type: application/json" -d '{}'
@app.route('/generate/<string:dataset_name>/<int:count>', methods=['GET'])
def generate_data(dataset_name, count):
    real_data, metadata = demo.download_demo(
        modality='single_table',
        dataset_name=dataset_name
    )
    synthesizer = GaussianCopulaSynthesizer(metadata)
    synthesizer.fit(real_data)
    synthetic_data = synthesizer.sample(num_rows=count)

    # json_real_data = real_data.to_dict(orient='records')
    json_synthetic_data = synthetic_data.to_dict(orient='records')

    # return synthetic data
    return jsonify(json_synthetic_data), 200

# curl -X POST http://localhost:8888/generate -H "Content-Type: application/json" -d '{}'
@app.route('/generate/<string:dataset_name>', methods=['GET'])
def generate_data_no_count(dataset_name):
    return generate_data(dataset_name, 10)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=8888)
