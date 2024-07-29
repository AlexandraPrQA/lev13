import configuration
import requests
import data

#Создание заказа
def new_order(body):
    new_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=body)
    return new_order


#Получение заказа по треку
def receipt_order(track):
    response = requests.get(configuration.URL_SERVICE + configuration.RECEIPT_ORDER+track)
    return response