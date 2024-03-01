# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

user_response = post_new_user(data.user_body).json()
auth_token = user_response['authToken']


# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data

def post_new_client_kit(kit_body, auth_token):
    new_headers = data.headers.copy()
    new_headers['Authorization'] = 'Bearer ' + auth_token
    new_kit_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_KIT,
                                     json=kit_body,
                                     headers=new_headers)
    return new_kit_response

