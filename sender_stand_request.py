import configuration
import requests
import data



def post_new_user(body): # Функция создает нового пользователя
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers_auth)




def post_new_kits(body, token): # Функция создает новый набор
    headers_dict = data.headers_auth_token.copy()
    headers_dict["Authorization"] = "Bearer " + token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCT_KITS,
                         json=data.user_body,
                         headers=headers_dict)