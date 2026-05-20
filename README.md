# Практическая работа 8
Swagger: https://secby.ru/docs

Описание: разработать набор api-методов, включающих аутентификацию, авторизацию, получение информации о пользователях в соответствии с ролевой моделью.

Задание: разработать набор автотестов для проверки функциональности API-запросов.
* Проверка авторизации (ввод логин-пароля, получение токена, отправление токена)
* Проверка метода получения информации о пользователе (User Profile)
* Проверка метода получения информации об администраторе

--- 
Как запустить:
1. Склонировать и перейти в репозиторий:
```bash
git clone https://github.com/Timokrut/indeed.git
cd indeed
```
2. Установить необходимые зависимости
\*При необходимости создать venv (для Windows другой путь к activate)
```bash
python3 -m venv venv
source venv/bin/activate
```
Установка зависимостей:
```bash
pip install --no-cache-dir -r requirements.txt
```
3. Настройка `.env`
```
USER_USERNAME / _PASSWORD / _ID   - данные от аккаунта обычного пользователя 
ADMIN_USERNAME / _PASSWORD / _ID  - данные от аккаунта администратора
MODERATOR_USERNAME / _PASSWORD /  - данные от аккаунта модератора
TEST_USER_ID   - ID пользователя, которому admin меняет роль и профиль 
```
[Пример .env](.env-example)

4. Запуск тестов
```bash
pytest
```
---

Результаты тестирования:
```bash
pytest
========================================================== test session starts ==========================================================
platform darwin -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0 -- /Users/timokrut/Coding/indeed/venv/bin/python3.14
cachedir: .pytest_cache
rootdir: /Users/timokrut/Coding/indeed
configfile: pytest.ini
testpaths: tests
collected 25 items                                                                                                                      

tests/test_admin.py::test_admin_can_get_user_profile PASSED                                                                       [  4%]
tests/test_admin.py::test_admin_can_change_role PASSED                                                                            [  8%]
tests/test_admin.py::test_admin_can_update_profile PASSED                                                                         [ 12%]
tests/test_admin.py::test_admin_cannot_set_password PASSED                                                                        [ 16%]
tests/test_auth.py::test_login_success PASSED                                                                                     [ 20%]
tests/test_auth.py::test_login_invalid_password PASSED                                                                            [ 24%]
tests/test_auth.py::test_login_invalid_user PASSED                                                                                [ 28%]
tests/test_auth.py::test_login_empty_credentials PASSED                                                                           [ 32%]
tests/test_auth.py::test_verify_valid_token PASSED                                                                                [ 36%]
tests/test_auth.py::test_verify_invalid_token PASSED                                                                              [ 40%]
tests/test_auth.py::test_verify_without_token PASSED                                                                              [ 44%]
tests/test_auth.py::test_change_password_success PASSED                                                                           [ 48%]
tests/test_auth.py::test_change_password_invalid_old_password PASSED                                                              [ 52%]
tests/test_auth.py::test_change_password_unauthorized PASSED                                                                      [ 56%]
tests/test_auth.py::test_user_cannot_set_password PASSED                                                                          [ 60%]
tests/test_profiles.py::test_get_current_profile PASSED                                                                           [ 64%]
tests/test_profiles.py::test_get_current_profile_unauthorized PASSED                                                              [ 68%]
tests/test_profiles.py::test_get_profiles PASSED                                                                                  [ 72%]
tests/test_profiles.py::test_get_my_profile_by_id PASSED                                                                          [ 76%]
tests/test_profiles.py::test_get_somebodys_profile_by_id PASSED                                                                   [ 80%]
tests/test_profiles.py::test_update_current_profile PASSED                                                                        [ 84%]
tests/test_profiles.py::test_update_current_profile_unauthorized PASSED                                                           [ 88%]
tests/test_profiles.py::test_user_cannot_update_other_profile PASSED                                                              [ 92%]
tests/test_profiles.py::test_user_cannot_delete_account PASSED                                                                    [ 96%]
tests/test_profiles.py::test_user_cannot_change_role PASSED                                                                       [100%]

========================================================== 25 passed in 24.19s ==========================================================
```