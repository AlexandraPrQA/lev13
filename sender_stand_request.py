import configuration
import requests
import data

#Создание заказа
def new_order(order_body):
    new_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=order_body)
    return new_order.json()


#Получение заказа по треку
def receipt_order(track):
    response = requests.get(configuration.URL_SERVICE + configuration.RECEIPT_ORDER+str(track))
    return response