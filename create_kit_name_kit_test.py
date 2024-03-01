import data
import sender_stand_request

print(sender_stand_request.auth_token)


def get_kit_body(name):
    new_data = data.kit_body.copy()
    new_data['name'] = name
    return new_data


def test_one_char():
    body = get_kit_body('a')
    response = sender_stand_request.post_new_client_kit(body, sender_stand_request.auth_token)
    return response


def test_51_chars():
    body = get_kit_body(data.kit_body_511['name'])
    response = sender_stand_request.post_new_client_kit(body, sender_stand_request.auth_token)
    return response


def test_zero_char():
    body = get_kit_body('')
    response = sender_stand_request.post_new_client_kit(body, sender_stand_request.auth_token)
    return response


def test_512_char():
    body = get_kit_body(data.kit_body_512['name'])
    response = sender_stand_request.post_new_client_kit(body, sender_stand_request.auth_token)
    return response


def test_english_chars():
    body = get_kit_body('QWErty')
    response = sender_stand_request.post_new_client_kit(body, sender_stand_request.auth_token)
    return response


def test_russian_chars():
    body = get_kit_body('Мария')
    response = sender_stand_request.post_new_client_kit(body, sender_stand_request.auth_token)
    return response


def test_special_chars():
    body = get_kit_body('"№%@",')
    response = sender_stand_request.post_new_client_kit(body, sender_stand_request.auth_token)
    return response


def test_allow_spaces():
    body = get_kit_body('Человек и КО')
    response = sender_stand_request.post_new_client_kit(body, sender_stand_request.auth_token)
    return response


def test_allow_digits():
    body = get_kit_body('123')
    response = sender_stand_request.post_new_client_kit(body, sender_stand_request.auth_token)
    return response


def test_empty_name_field():
    response = sender_stand_request.post_new_client_kit({}, sender_stand_request.auth_token)
    return response


def test_name_field_number_data_type():
    body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(body, sender_stand_request.auth_token)
    return response


def test_positive_assert():
    one_char_response = test_one_char()
    fiftyone_chars = test_51_chars()
    english_chars_response = test_english_chars()
    russian_chars_response = test_russian_chars()
    special_chars_response = test_special_chars()
    allow_spaces_response = test_allow_spaces()
    allow_digits_response = test_allow_digits()
    assert one_char_response.status_code == 201, "Неверный статус код 1 символ имени"
    assert one_char_response.json()['name'] == 'a'
    assert fiftyone_chars.status_code == 201, "Неверный статус код, 51 символ имени"
    assert fiftyone_chars.json()['name'] == data.kit_body_511['name']
    assert english_chars_response.status_code == 201, "Неверный статус код английские буквы в имени"
    assert english_chars_response.json()['name'] == 'QWErty'
    assert russian_chars_response.status_code == 201, "Неверный статус код русские буквы в имени"
    assert russian_chars_response.json()['name'] == 'Мария'
    assert special_chars_response.status_code == 201, "Неверный статус код специальные символы в имени"
    assert special_chars_response.json()['name'] == '"№%@",'
    assert allow_spaces_response.status_code == 201, "Неверный статус код разрешены пробелы в имени"
    assert allow_spaces_response.json()['name'] == 'Человек и КО'
    assert allow_digits_response.status_code == 201, "Неверный статус код разрешены цифры в имени"
    assert allow_digits_response.json()['name'] == '123'


test_positive_assert()


def test_negative_assert():
    zero_char_response = test_zero_char()
    five_hundred_12_response = test_512_char()
    empty_name_field_response = test_empty_name_field()
    name_field_data_type_number_response = test_name_field_number_data_type()
    assert zero_char_response.status_code == 400, "Статус код должен быть 400"
    assert five_hundred_12_response.status_code == 400, "Статус код должен быть 400"
    assert empty_name_field_response.status_code == 400, "Статус код должен быть 400"
    assert name_field_data_type_number_response.status_code == 400, "Статус код должен быть 400"


test_negative_assert()
