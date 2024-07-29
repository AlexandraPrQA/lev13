# Александра Перетягина, 19-я когорта — Финальный проект.
# Инженер по тестированию плюс

import data
import sender_stand_request


def test_receive_order_and_track():
    response = sender_stand_request.new_order(data.order_body) #созд заказа
    track = response.json()["track"]   #трек номер

def test_receipt_order_status_code_is_200():
    response = requests.get(configuration.URL_SERVICE + configuration.RECEIPT_ORDER+new_order())
    status_code = response.status_code
    assert status_code == 200