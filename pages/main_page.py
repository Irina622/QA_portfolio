#импорт базового класса
from pages.base_s_page import BaseSPage
#импорт класса-locators
from pages.locators import MainPageLocators
#импорт модуля inspect
import inspect

class MainPage(BaseSPage):
	def __init__(self, *args, **kwargs):
	#вызываем конструктор родителя и передаём ему аргументы, переданные в данный конструктор
		super(MainPage, self).__init__(*args, **kwargs)
	
	def should_be_main_page(self):
		#управляющая функция тестом верности страницы
		self.should_be_main_url()
		self.should_be_photo_on_main_page()

	def should_be_order_form_on_main_page(self):
		#управляющая функция тестом наличия формы заказа на странице
		self.should_be_form_on_main_page()
		self.should_be_username_on_form_on_main_page()
		self.should_be_usermail_on_form_on_main_page()
		self.should_be_userfiles_on_form_on_main_page()
		self.should_be_usercomment_on_form_on_main_page()
		self.should_be_submit_on_form_on_main_page()

	def should_be_photo_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.PHOTO_IMG), "<Main Page>Photo is not presented"
		print(inspect.stack()[0][3] + ": PHOTO_IMG Ok")
		
	def should_be_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.ORDER_FORM), "<Main Page>Order form is not presented"
		print(inspect.stack()[0][3] + ": ORDER_FORM Ok")
		
	def should_be_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.ORDER_FORM), "<Main Page>Order form is not presented"
		print(inspect.stack()[0][3] + ": ORDER_FORM Ok")
		
	def should_be_username_on_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.USERNAME_FORM), "<Main Page>UserName on form is not presented"
		print(inspect.stack()[0][3] + ": USERNAME_FORM Ok")
		
	def should_be_usermail_on_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.USERMAIL_FORM), "<Main Page>UserMail on form is not presented"
		print(inspect.stack()[0][3] + ": USERMAIL_FORM Ok")
		
	def should_be_userfiles_on_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.USERFILES_FORM), "<Main Page>UserFiles on form is not presented"
		print(inspect.stack()[0][3] + ": USERFILES_FORM Ok")
		
	def should_be_usercomment_on_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.USERCOMMENT_FORM), "<Main Page>UserComment on form is not presented"
		print(inspect.stack()[0][3] + ": USERCOMMENT_FORM Ok")
		
	def should_be_submit_on_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.SUBMIT_FORM), "<Main Page>Submit on form is not presented"
		print(inspect.stack()[0][3] + ": SUBMIT_FORM Ok")
		
	def should_be_main_url(self):
		# проверка на корректный url адрес
		uri = "/Irina622/portfolio/"
		url = self.browser.current_url
#		print ("\nMainPage:should_be_ware_url()")
#		print ("\nself.browser.current_url ='" + url + "' (" + str(url.find(uri)) + "; url_len=" + str(len(url)) + "; len=" + str(len(uri)) + "; " + str(len(url)-url.find(uri)-len(uri)) + ")")
		assert 0 < url.find(uri), "<Main Page>URI is wrong"
		print(inspect.stack()[0][3] + ": uri Ok")

#пустая строка в конце файла
