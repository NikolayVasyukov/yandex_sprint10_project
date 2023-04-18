import configuration
import requests
import data



def post_new_user(body): # Функция создает нового пользователя
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers_auth_token)
res = post_new_user(data.user_body)
print(res.json())




def post_new_kits(body, token): # Функция создает новый набор
    headers_dict = data.headers_auth_token.copy()
    headers_dict["Authorization"] = "Bearer " + token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCT_KITS,
                         json=body,
                         headers=headers_dict)
