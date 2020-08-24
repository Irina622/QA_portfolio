#для работы параметризации
import pytest
#для работы счетчика времени
import time
#импорт класса главной страницы MainPage
from pages.main_page import MainPage
#импорт класса страницы AboutPage
from pages.about_page import AboutPage
#импорт класса страницы ContactPage
from pages.contact_page import ContactPage

@pytest.mark.main_page
class TestMainPage():
	def test_guest_main_page(self, browser):
		link = "https://htmlpreview.github.io/?https://raw.githubusercontent.com/Irina622/portfolio/master/index.html"
		page = MainPage(browser=browser, url=link)
		page.open()
		page.should_be_main_page()
		page.should_be_base_links_on_page()
		page.should_be_order_form_on_main_page()
		time.sleep(2)

@pytest.mark.about_page
class TestAboutPage():
	def test_guest_about_page(self, browser):
		link = "https://htmlpreview.github.io/?https://raw.githubusercontent.com/Irina622/portfolio/master/about.html"
		page = AboutPage(browser=browser, url=link)
		page.open()
		page.should_be_about_page()
		page.should_be_base_links_on_page()
		time.sleep(2)

@pytest.mark.contact_page
class TestContactPage():
	def test_guest_contact_page(self, browser):
		link = "https://htmlpreview.github.io/?https://raw.githubusercontent.com/Irina622/portfolio/master/contact.html"
		page = ContactPage(browser=browser, url=link)
		page.open()
		page.should_be_contact_page()
		page.should_be_base_links_on_page()
		page.should_be_order_form_on_contact_page()
		time.sleep(2)

#пустая строка в конце файла
