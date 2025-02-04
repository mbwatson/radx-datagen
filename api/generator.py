import os
from flask import jsonify
from sdv.datasets import demo
from sdv.metadata import Metadata
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.datasets.local import load_csvs

datasets = load_csvs(folder_name='./data/')

radx_real_data = datasets['real_data']
metadata = Metadata.load_from_json(filepath='./data/metadata.json')
radx_synthesizer = GaussianCopulaSynthesizer(metadata)
radx_synthesizer.fit(radx_real_data)

def radx_sampler(count):
    return radx_synthesizer.sample(num_rows=count)

def demo_sampler(dataset_name, count):
    real_data, metadata = demo.download_demo(
        modality='single_table',
        dataset_name=dataset_name
    )
    synthesizer = GaussianCopulaSynthesizer(metadata)
    synthesizer.fit(real_data)
    return synthesizer.sample(num_rows=count)

def generate_synthetic_data(dataset_name, count):
    if dataset_name == "radx":
        synthetic_data = radx_sampler(count)
    else:
        synthetic_data = demo_sampler(dataset_name, count)

    json_synthetic_data = synthetic_data.to_dict(orient='records')

    # return synthetic data
    return jsonify({
        'data': json_synthetic_data,
        'diagnostics': 'coming soon...',
    }), 200
