# Импорт модуля configuration, который содержит настройки подключения и путь к документации
import configuration
# Импорт модуля requests, предназначенный для отправки HTTP-запросов и взаимодействия с веб-сервисами
import requests
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Создание нового пользователя
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = user_body,
                         headers = data.headers)

# Получение authtoken для нового пользователя
def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json().get("authToken")

# Создание нового набора для нового пользователя
def post_new_kit(kit_body):
    data.headers["Authorization"] += get_new_user_token()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
                         json = kit_body,
                         headers = data.headers)
