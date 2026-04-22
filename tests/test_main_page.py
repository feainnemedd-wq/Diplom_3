import allure
import pytest
from page_objects.main_page import MainPage
from page_objects.feed_page import FeedPage

class TestMainPage:

    @allure.title('Проверка перехода в "Ленту заказов" по клику в хедере')
    def test_navigate_to_order_feed_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Переходим в ленту заказов
        main_page.click_header_feed_button()
        
        # Проверяем, что перешли
        assert feed_page.get_text_on_title_of_orders_list() == "Лента заказов"

    @allure.title('Проверка перехода в "Конструктор" из ленты заказов')
    def test_navigate_to_constructor_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Сначала переходим в ленту, чтобы оказаться не на главной
        main_page.click_header_feed_button()
        
        # Кликаем на "Конструктор"
        main_page.click_on_button_constructor()
        
        # Проверяем возврат на главную (Конструктор)
        assert main_page.get_text_on_title_of_constructor() == "Соберите бургер"

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    def test_navigate_to_order_history_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        main_page.click_header_feed_button()
        assert feed_page.get_text_on_title_of_orders_list() == "Лента заказов"

    @allure.title('Проверка отображения модального окна "Детали ингредиента"')
    def test_displaying_modal_window_details_of_ingredient_success(self, driver):
        main_page = MainPage(driver)
        
        main_page.click_on_ingredient()
        assert main_page.check_displaying_of_modal_details()

    @allure.title('Проверка закрытия модального окна "Детали ингредиента" кликом по крестику')
    def test_close_modal_window_details_of_ingredient_success(self, driver):
        main_page = MainPage(driver)
        
        main_page.click_on_ingredient()
        main_page.close_modal()
        assert main_page.check_not_displaying_of_modal_details()

    @allure.title('Проверка увеличения счетчика при добавлении ингредиента в заказ')
    def test_changing_counter_for_ingredients_in_order_success(self, driver):
        main_page = MainPage(driver)
        
        # Получаем значение счетчика ДО добавления
        initial_counter = main_page.get_ingredient_counter_value()
        
        # Выполняем drag and drop ингредиента в корзину
        main_page.drag_and_drop_ingredient_to_order()
        
        # Получаем значение счетчика ПОСЛЕ добавления
        new_counter = main_page.get_ingredient_counter_value()
        
        # Проверяем, что значение увеличилось
        assert int(new_counter) > int(initial_counter)
        assert main_page.check_ingredient_displayed()
        assert main_page.check_basket_displayed()

