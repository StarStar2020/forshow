from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'http://shop.bugred.ru/api/items/get/'

session = Session()

try:
  response = session.post(url, '{"id": 51}')
  assert(response.status_code==200)
  assert (response.encoding == 'utf-8')
  assert response.elapsed.microseconds>10000  #10секунд
  data = json.loads(response.text)
  print(json.dumps(data, indent=4, sort_keys=True))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)