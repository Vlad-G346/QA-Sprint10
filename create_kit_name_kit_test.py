# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data
# Импорт модуля sender_stand_request, содержащий функции для отправки HTTP-запросов к API
import sender_stand_request

# Единоразово получаем токен авторизации для всех тестов
auth_token = sender_stand_request.get_new_user_token()

# Генерация набора для тестов
def get_kit_body(name):
    correct_kit_body = data.kit_body.copy()
    correct_kit_body["name"] = name
    return correct_kit_body

# Функция для позитивной проверки
def positive_assertion(name):
    kit_body_positive = get_kit_body(name)
    kit_body_positive_response = sender_stand_request.post_new_kit(kit_body_positive, auth_token)
    assert kit_body_positive_response.json()["name"] == name
    assert kit_body_positive_response.status_code == 201

# Функция для негативной проверки
def negative_assertion(name):
    kit_body_negative = get_kit_body(name)
    kit_body_negative_response = sender_stand_request.post_new_kit(kit_body_negative, auth_token)
    assert kit_body_negative_response.status_code == 400

# Функция для негативной проверки с пустым телом запроса
def negative_assertion_no_name(kit_body):
    kit_no_name = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert kit_no_name.status_code == 400

# Тест 1: Допустимое количество символов (1), ОР: 201
def test_kit_1_in_name_get_success_response():
    positive_assertion("a")

# Тест 2: Допустимое количество символов (511), ОР: 201
def test_kit_511_in_name_get_success_response():
    positive_assertion("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabca\
                       bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                       abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdacb\
                       abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdacba\
                       bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcbcb\
                       dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabaca\
                       cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcbc\
                       cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcbca\
                       dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc")

# Тест 3: Количество символов меньше допустимого (0), ОР: 400
def test_kit_0_in_name_get_error_response():
    negative_assertion("")

# Тест 4: Количество символов больше допустимого (512), ОР: 400
def test_kit_512_in_name_get_error_response():
    negative_assertion("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdаacba\
                        bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                        abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdbca\
                        abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdacba\
                        bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcabc\
                        dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdababc\
                        cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdababc\
                        cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcabc\
                        dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdacb")

# Тест 5: Разрешены английские буквы: (QWErty), ОР: 201
def test_kit_eng_in_name_get_success_response():
    positive_assertion("QWErty")

# Тест 6: Разрешены русские буквы: (Мария), ОР: 201
def test_kit_rus_in_name_get_success_response():
    positive_assertion("Мария")

# Тест 7: Разрешены спецсимволы: ("№%$@",), ОР: 201
def test_kit_spec_in_name_get_success_response():
    positive_assertion("№%$@")

# Тест 8: Разрешены пробелы: ( " Человек и КО " ), ОР: 201
def test_kit_space_in_name_get_success_response():
    positive_assertion(" Человек и КО ")

# Тест 9: Разрешены цифры: (123), ОР: 201
def test_kit_num_in_name_get_success_response():
    positive_assertion("123")

# Тест 10: Параметр не передан в запросе, ОР: 400
def test_kit_type_no_name_get_error_response():
    correct_kit_body_no_name = data.kit_body.copy()
    correct_kit_body_no_name.pop("name")
    negative_assertion_no_name(correct_kit_body_no_name)

# Тест 11: Передан другой тип параметра (число), ОР: 400
def test_kit_type_in_name_get_error_response():
    negative_assertion(123)
