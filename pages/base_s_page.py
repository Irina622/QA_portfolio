#импорт базового класса
from pages.base_page import BasePage
#импорт класса-locators
from pages.locators import BaseSPageLocators

print("\n\n------------------------\n")
print("НАДО!!! ДОБАВИТЬ! (file:[base_s_page.py])")
print("1) Тест ссылок из мобильное меню")
print("2) Страница Контакты")
print("3) Настраиваемость сообщений об удачном проходе теста и их нумерация")
print("\n------------------------\n")

class BaseSPage(BasePage):
	def __init__(self, *args, **kwargs):
		#вызываем конструктор родителя и передаём ему аргументы, переданные в данный конструктор
		super(BaseSPage, self).__init__(*args, **kwargs)

	def should_be_base_links_on_page(self):
		#управляющая функция тестом наличия всех обязательных ссылок на странице
		self.should_be_about_link_on_page()
		self.should_be_main_link_on_page()
		self.should_be_portfolio_link_on_page()
		self.should_be_contact_link_on_page()
		self.should_be_scype_link_on_page()
		self.should_be_github_link_on_page()

	def should_be_about_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.ABOUT_LINK), "<Base S Page>About link is not presented"
		print("ABOUT_LINK Ok")

	def should_be_main_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.MAIN_LINK), "<Base S Page>Main link is not presented"	
		print("MAIN_LINK Ok")

	def should_be_portfolio_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.PORTFOLIO_LINK), "<Base S Page>Portfolio link is not presented"	
		print("PORTFOLIO_LINK Ok")

	def should_be_contact_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.CONTACT_LINK), "<Base S Page>Contact link is not presented"	
		print("CONTACT_LINK Ok")

	def should_be_scype_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.SCYPE_LINK), "<Base S Page>Scype link is not presented"	
		print("SCYPE_LINK Ok")

	def should_be_github_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.GITHUB_LINK), "<Base S Page>Github link is not presented"	
		print("GITHUB_LINK Ok")

#пустая строка в конце файла
