import requests
import json

def fetch_datasets():
  try:
    response = requests.get('http://api:8888/list_datasets')
    response.raise_for_status()  # raise an HTTPError for bad responses (4xx and 5xx)

    # try to parse response as JSON
    try:
      return response.json()
    except ValueError:
      raise ValueError('Response content is not JSON serializable')

  except requests.RequestException as error:
    print('Failed to fetch data:', error)
    raise

def fetch_synthetic_data(dataset, count):
  try:
    response = requests.get(f'http://api:8888/generate/{dataset}/{count}')
    response.raise_for_status()  # raise an HTTPError for bad responses (4xx and 5xx)

    try:
      return response.json()
    except ValueError:
      raise ValueError('Response content is not JSON serializable')

  except requests.RequestException as error:
    print('Failed to fetch data:', error)
    raise

