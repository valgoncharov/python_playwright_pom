import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@allure.title("Название теста")
def test_login_failure(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('invalid_user', 'invalid_password')
    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@allure.epic("Web interface")
@allure.feature("Доступ к системе")
@allure.story("Авторизаци")
def test_login_success(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login('admin', 'admin')

    dashboard_page.assert_welcome_message("Welcome admin")


@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success0(page, username, password):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login(username, password)

    dashboard_page.assert_welcome_message(f"Welcome {username}")


#Используем фикстуры для упрощения тестов.
@allure.description("Описание теста")
def test_login_failure_with_fixture(login_page):
    login_page.navigate()
    login_page.login('user', 'password')

    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success1(login_page, dashboard_page, username, password):
    login_page.navigate()
    login_page.login(username, password)
    dashboard_page.assert_welcome_message(f"Welcome {username}")
