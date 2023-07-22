from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from allure import step

from helper.model import app
import allure


@allure.feature('UI')
@allure.title('Поиск в wikipedia')
def test_search():
    app.given_opened()

    with step('Ввести в поле поиска текст'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'avito.ru'
        )

    with step('Проверить результат поиска'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))


@allure.feature('UI')
@allure.title('Добавление языков поиска')
def test_add_language():
    with step('Открыть страницу добавления языков'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/addLanguageButton")).click()

    with step('Добавить язык: "Deutsch"'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/wiki_language_title")).element_by(
            have.text("Add language")
        ).click()
    browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/localized_language_name")
        ).element_by(have.text("Deutsch")).click()

    with step('Проверить язык "Deutsch" в списке добавленных'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/wiki_language_title")).element_by(
            have.text("Deutsch")
        ).should(be.visible)


@allure.feature('UI')
@allure.title('Удаление добавленного языка из списка')
def test_delete_added_language():
    with step('Добавить язык: "Deutsch"'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/addLanguageButton")).click()
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/wiki_language_title")).element_by(
            have.text("Add language")
        ).click()
        browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/localized_language_name")
        ).element_by(have.text("Deutsch")).click()

    with step('Удалить язык: "Deutsch" из списка'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "More options")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/title")).click()
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/wiki_language_title")).element_by(
            have.text("Deutsch")
        ).click()
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/menu_delete_selected")
        ).click()
        browser.element((AppiumBy.ID, "android:id/button1")).click()

    with step('Проверить, что язык удален'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/wiki_language_title")).element_by(
            have.no.text("Deutsch")
        )


@allure.feature('UI')
@allure.title('История поиска')
def test_search_history_saved():
    app.given_opened()

    with step('Выполнить поиск по тексту'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'avito.ru'
        )
        browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        ).element_by(have.text("Avito.ru")).click()

    with step('Провить историю поиска'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Navigate up")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Navigate up")).click()
        browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/navigation_bar_item_small_label_view")
        ).element_by(have.text("Search")).click()
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        ).should(have.text("Avito.ru"))
