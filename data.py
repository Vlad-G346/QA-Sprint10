# Тело запроса будет в формате JSON
# Передается токен пользователя
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}

# Тело POST запроса для создания нового пользователя
user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

# Тело POST запроса для создания нового продуктового набора
kit_body = {
       "name": "Мой набор"
   }
