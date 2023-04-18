import requests

import sender_stand_request
import data
import configuration

def get_new_user(token):
    user_body = data.user_body.copy()
#    res = sender_stand_request.post_new_user(user_body)
#   token = res.json()["authToken"]
 #   return token

#def post_new_kits(body, token): # Функция создает новый набор
 #   headers_dict = data.headers_auth_token.copy()
 #   headers_dict["Authorization"] = "Bearer " + token
 #   return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCT_KITS,
  #                       json=data.user_body,
  #                       headers=headers_dict)

def kits_token(kits_token):
    resp = requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCT_KITS,
                         json=data.kits_body,
                         headers=get_new_user(token))


