
# coding: utf-8

# In[57]:

from pprint import pprint
from urlib.parse import urlencode
import request

authorize_url = 'https://oauth.vk.com/authorize'
app_id = 6161756
version ='5.67'
auth_data = {
  'client_id': app_id,
  'redirect_uri': 'http://oauth.vk.com/blank.html',
  'display': 'mobile',
  'scope': 'friends',
  'response_type': 'token',
  'v': version
}

#появляется ошибка в последней строке (в независимости от того что это за строка), которую не могу исправить
print('?'.join(authorize_url,urlencode(auth_data))
token = 'вставить из предыдущего результата'
params('access_token' = token, 'v' = version)
response = request.get('https://api.vk.com/method/friends.get', params)
base_response = []
base_response.append(response)
individual_base = {}

#по поводу части кода '.user_id': я правильно написал или нужно его не через точку а в скобках?
for friend in base_response:
  response_individual = request.get('https://api.vk.com/method/friends.get' + '.user_id',friend, params)
  individual_base.update({'friend'}: response_individual)

all_set = []

for key, value in individual_base.items():
  key = set()
  key.add(value)
  all_set.append(key)
  
print(set.intersection_update(*all_set))
