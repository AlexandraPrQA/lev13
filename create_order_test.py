# Александра Перетягина, 19-я когорта — Финальный проект.
# Инженер по тестированию плюс

import data
import sender_stand_request


def test_receive_order_and_track():
    response = sender_stand_request.new_order(data.order_body) #созд заказа
    track = response.get("track")   #трек номер
    receipt_response = sender_stand_request.receipt_order(track)
    status_code = receipt_response.status_code
    assert status_code == 200


