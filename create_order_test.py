# Александра Перетягина, 19-я когорта — Финальный проект.
# Инженер по тестированию плюс

import data
import sender_stand_request


def test_receive_order_and_track():
    response = sender_stand_request.post_new_order(data.order_body)
    track = response.json()["track"]
    return (response(track))
    assert response.status_code == 200

