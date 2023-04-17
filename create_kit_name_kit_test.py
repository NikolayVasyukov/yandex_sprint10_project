import data
import sender_stand_request


def get_kits_body(kits_name): # Функция копирует имя набора

    current_body = data.kits_body.copy()
    current_body["name"] = kits_name

    return current_body

def get_new_user():
    user_body = data.user_body.copy()
    res = sender_stand_request.post_new_user(user_body)
    token = res.json()["authToken"]
    return token

def possitive_assert(kits_name):
    kits_body = get_kits_body(kits_name)
    kits_response = sender_stand_request.post_new_kits(kits_body, get_new_user())

    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kits_name

def negative_assert(kits_name):
    kits_body = get_kits_body(kits_name)
    kits_response = sender_stand_request.post_new_kits(kits_body)

    assert kits_response.status_code == 400

def negative_assert_no_name(kits_body):
    kits_response = sender_stand_request.post_new_kits(kits_body)

    assert kits_response.status_code == 400

# 1 Тест. Допустимое количество символов (1)
def test_create_kit_1_letter_in_name_get_success_response():
    possitive_assert("N")

# 2 Тест. Допустимое количество символов (511)
def test_create_kit_511_letter_in_name_get_success_response():
    possitive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# 3 Тест. Количество символов меньше допустимого (0)
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert("")

# 4 Тест. Количество символов больше допустимого (512)
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabCD")

# 5 Тест. Разрешены английские буквы
def test_create_kit_english_letter_in_name_get_success_response():
    possitive_assert("QWErty")

# 6 Тест. Разрешены русские буквы
def test_create_kit_russian_letter_in_name_get_success_response():
    possitive_assert("Мария")

# 7 Тест. Разрешены спецсимволы
def test_create_kit_special_simbol_in_name_get_success_response():
    possitive_assert("\"№%@\",")

# 8 Тест. Разрешены пробелы
def test_create_kit_space_in_name_get_success_response():
    possitive_assert("Человек и КО ")

# 9 Тест. Разрешены цифры
def test_create_kit_number_in_name_get_success_response():
    possitive_assert("123")

# 10 Тест. Параметр не передан в запросе
def test_create_kit_empty_name_get_success_error_response():
    kits_body = data.kits_body.copy()
    kits_body.pop("name")
    negative_assert_no_name(kits_body)

# 11 Тест. Передан другой тип параметра
def test_create_kit_nomber_type_name_get_error_response():
    kits_body = get_kits_body(12)

    response = sender_stand_request.post_new_kits(kits_body)
    assert response.status_code == 400

