import json
from datetime import datetime

# paste your JSON
json_data = """
{
  "success": true,
  "code": "SUCCESS",
  "data": {
    "from": 1585679400000,
    "to": 1593282600000,
    "transactionData": [
      {
        "name": "Insurance",
        "paymentInstruments": [{ "type": "TOTAL", "count": 185348, "amount": 3.3732166e7 }]
      }
    ]
  },
  "responseTimestamp": 1692610792790
}
"""

data = json.loads(json_data)
tx = data['data']['transactionData'][0]
instrument = tx['paymentInstruments'][0]

from_date = datetime.fromtimestamp(data['data']['from']/1000)
to_date = datetime.fromtimestamp(data['data']['to']/1000)
response_ts = datetime.fromtimestamp(data['responseTimestamp']/1000)

# create a simple dict
row = {
    "from_date": from_date,
    "to_date": to_date,
    "name": tx['name'],
    "type": instrument['type'],
    "count": instrument['count'],
    "amount": instrument['amount'],
    "response_timestamp": response_ts
}

for i,j in row.items():
    print(f"{i}: {j}")
