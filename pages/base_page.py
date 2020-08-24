#Основные функции не привязанные к конкретному сайту
#импорт исключения NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
#импорт исключения TimeoutException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
	def __init__(self, browser, url, timeout=10):
	#инициируем класс
		self.browser = browser
		self.url = url
#		self.browser.implicitly_wait(timeout)
	
	def is_element_present(self, how, what):
	#поиск элемента на странице: если есть - return true, else false
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True
	
	def is_not_element_present(self, how, what, timeout=20):
	#поиск элемента на странице в течение времени: если есть - ?return true, else false?
	#элемента не должно быть по-дефаулту, но потом должен проявиться
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True
		return False
	
	def is_disappeared(self, how, what, timeout=20):
	#поиск элемента на странице в течение времени: если есть - ?return true, else false?
	#элемент должен быть по-дефаулту, но потом должен исчезнуть
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).\
				until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False
		return True
	
	def is_element(self, how, what):
	#поиск элемента на странице: запуск после def is_element_present()=true
		return self.browser.find_element(how, what)
	
	def open(self):
	#открываем ссылку
		self.browser.get(self.url)


#пустая строка в конце файла
