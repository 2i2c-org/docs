# Query cost monitoring API with Grafana

You can directly query the cost monitoring API using the same Grafana token provisioned in [](./prometheus-grafana-access.md).

```{note}
The cost monitoring API returns data as JSON blobs, unlike standard Prometheus time series data. This means that you cannot configure the cost monitoring API as a standard Prometheus datasource for services such as in-built [AWS CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_MultiDataSources-Connect.html#MultiDataSources-Prometheus).
```

## Prerequisites

- A Grafana service account token (see [](./prometheus-grafana-access.md) for instructions)
- A `.env` file to securely store your Grafana token (see {ref}`managing-secrets`)
- A virtual environment with the following Python packages installed:
  - `python-dotenv`
  - `requests`
  - `yarl`

## Sample Code

```python
import json
import os
import requests
from dotenv import load_dotenv
from yarl import URL

# Load Grafana service account token from .env file
load_dotenv()
grafana_token = os.environ["GRAFANA_TOKEN"]

grafana_url = URL("https://grafana.<cluster_name>.2i2c.cloud/")
api_url = grafana_url / "api/datasources"
datasource = requests.get(
    api_url,
    headers={
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {grafana_token}",
    }
)

# Get the cost-monitoring yesoreyeram-infinity-datasource UID
datasource_uid = datasource.json()[1]["uid"]
target_url = URL("http://jupyterhub-cost-monitoring.support.svc.cluster.local")
# See https://jupyterhub-cost-monitoring.readthedocs.io/en/latest/api/ for available endpoints
subpath = "total-costs"

headers = {
    "Authorization": f"Bearer {grafana_token}",
    "Content-Type": "application/json"
}

payload = {
    "queries": [
        {
            "datasource": {
                "type": "yesoreyeram-infinity-datasource",
                "uid": datasource_uid,
            },
            "url": str(target_url / subpath),
            "url_options": {
                "method": 'GET',
                "data": '',
            },
            "type": "json",
            "source": "url",
            "format": "table",
            "parser": "backend",
            "root_selector": "",
            # Columns can change depending on data returned by endpoint – see https://github.com/2i2c-org/jupyterhub-cost-monitoring/blob/a6e49c719e8600fc2490e2fb2a77da09ce4bcd1a/dashboards/common.libsonnet#L128 for examples from existing cloud cost grafana dashboards
            "columns": [
              {"selector": "date", "text": "Date", "type": "timestamp"},
              {"selector": "name", "text": "Name", "type": "string"},
              {"selector": "cost", "text": "Cost", "type": "number"},
            ],
        }
    ],
    "from": "now-1d",
    "to": "now"
}

# https://grafana.com/docs/grafana-cloud/developer-resources/api-reference/http-api/data_source/#query-a-data-source
query_url = grafana_url / "api/ds/query"

response = requests.post(
    query_url,
    headers=headers,
    data=json.dumps(payload)
)

response.raise_for_status()
data = response.json()

print(json.dumps(data, indent=2))
```