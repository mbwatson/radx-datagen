import requests
import json

def fetch_cde_collections():
  try:
    response = requests.post('https://cde.nlm.nih.gov/server/de/search')
    response.raise_for_status()  # raise an HTTPError for bad responses (4xx and 5xx)

    # try to parse response as JSON
    try:
      data = response.json()
      return data['aggregations']['orgs']['orgs']['buckets']
    except ValueError:
      raise ValueError('Response content is not JSON serializable')

  except requests.RequestException as error:
    print('Failed to fetch data:', error)
    raise

def fetch_cdes_from_collection(collection_key):
  """
  fetch all CDEs from a collection (by key) by making multiple paginated requests.
  
  :param collection_key: key of the collection from which we will fetch CDEs
  :return: list of all CDE IDs in the collection
  """
  base_url = 'https://cde.nlm.nih.gov/api/de/search'
  all_cdes = []
  page = 1
  results_per_page = 100

  while True:
    try:
      response = requests.post(base_url, json={
        'excludeAllOrgs': False,
        'excludeOrgs': [],
        'includeAggregations': True,
        'includeRetired': False,
        'nihEndorsed': False,
        'page': page,
        'resultPerPage': results_per_page,
        'searchToken': 'id01bc746c4a995',
        'selectedAdminStatuses': [],
        'selectedCopyrightStatus': [],
        'selectedDatatypes': [],
        'selectedElements': [],
        'selectedElementsAlt': [],
        'selectedOrg': collection_key,
        'selectedStatuses': [],
      })

      response.raise_for_status()  # raise an HTTPError for bad responses (4xx, 5xx)

      # attempt to parse response as JSON
      data = response.json()
      if 'docs' not in data or 'resultsTotal' not in data:
        raise ValueError('Response JSON has an unexpected structure')

      # collect CDEs
      docs = data['docs']
      total_results = data['resultsTotal']
      all_cdes.extend(cde for cde in docs)

      # check if all pages are processed
      if total_results <= len(all_cdes):
        break

      page += 1

    except requests.RequestException as error:
      print('Failed to fetch data:', error)
      raise
    except ValueError as parse_error:
      print('Failed to parse data:', parse_error)
      raise
  
  return all_cdes
