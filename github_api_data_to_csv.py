import json

import requests
import pandas as pd

url = "https://api.github.com/repositories?since=364"

data = requests.get(url)
# print(json.loads(data.content))
response_data = json.loads(data.content)
d_data = pd.DataFrame(response_data)
d_data.to_csv('res_pata.csv', index=False)
