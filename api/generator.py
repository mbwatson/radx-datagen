import os
from flask import jsonify
from sdv.datasets import demo
from sdv.metadata import Metadata
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.datasets.local import load_csvs
from sdv.evaluation.single_table import run_diagnostic
import pandas as pd

datasets = load_csvs(folder_name='./data/')

radx_real_data = datasets['real_data']
metadata = Metadata.load_from_json(filepath='./data/metadata.json')
radx_synthesizer = GaussianCopulaSynthesizer(metadata)
radx_synthesizer.fit(radx_real_data)

def radx_sampler(count):
    synthetic_data = radx_synthesizer.sample(num_rows=count)
    diagnostic_report = run_diagnostic(
        real_data=radx_real_data,
        synthetic_data=synthetic_data,
        metadata=metadata)
    return synthetic_data, diagnostic_report

def demo_sampler(dataset_name, count):
    real_data, metadata = demo.download_demo(
        modality='single_table',
        dataset_name=dataset_name
    )
    synthesizer = GaussianCopulaSynthesizer(metadata)
    synthesizer.fit(real_data)
    synthetic_data = synthesizer.sample(num_rows=count)
    diagnostic_report = run_diagnostic(
        real_data=radx_real_data,
        synthetic_data=synthetic_data,
        metadata=metadata)
    return synthetic_data, diagnostic_report

def convert_values(obj):
    """Recursively convert df in a dictionary to json-serializable format."""
    if isinstance(obj, pd.DataFrame):
        return obj.to_dict(orient='records')  # convert df to list of dicts
    elif isinstance(obj, dict):
        return {k: convert_values(v) for k, v in obj.items()}  # recursively convert
    return obj  # return as-is if not a dataframe

def generate_synthetic_data(dataset_name, count):
    if dataset_name == "radx":
        synthetic_data, diagnostic_report = radx_sampler(count)
    else:
        synthetic_data, diagnostic_report = demo_sampler(dataset_name, count)

    json_synthetic_data = synthetic_data.to_dict(orient='records')
    diagnostic_results = diagnostic_report.get_properties()
    json_diagnostic_results = convert_values(diagnostic_results)  # serialize

    # return synthetic data & diagnostics
    return jsonify({
        'data': json_synthetic_data,
        'diagnostics': json_diagnostic_results,
    }), 200
