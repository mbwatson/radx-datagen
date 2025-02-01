import os
from flask import Flask, jsonify, request
from sdv.datasets import demo
from generator import generate_synthetic_data

app = Flask(__name__)

# return available endpoints
@app.route('/', methods=['GET'])
def list_endpoints():
    endpoints = {
        "/": "This response.",
        "/list_datasets": "List of available datasets.",
        "/generate/<string:dataset_name>/<int:count>": "Generate and list `count` number of records from `dataset_name`.",
    }
    return jsonify(endpoints), 200

# return available datasets
@app.route('/list_datasets', methods=['GET'])
def list_datasets():
    demos = demo.get_available_demos(modality='single_table')
    demo_datasets = [record['dataset_name'] for record in demos.to_dict(orient='records')]
    custom_datasets = ['radx']
    return jsonify({
        "demo": demo_datasets,
        "custom": custom_datasets,
    }), 200

# return `count` many synthetic samples from `dataset`
@app.route('/generate/<string:dataset_name>/<int:count>', methods=['GET'])
def generate_data(dataset_name, count):
    return generate_synthetic_data(dataset_name, count)

# just like above route, but `count` can be ommitted; defaults to `default_count`.
default_count = 10
@app.route('/generate/<string:dataset_name>', methods=['GET'])
def generate_data_no_count(dataset_name):
    return generate_data(dataset_name, default_count)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
