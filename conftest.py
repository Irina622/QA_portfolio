import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	#добавляем свои параметры в строку запуска pytest
	#--language - accept_languages браузера 
	parser.addoption('--language', \
			action='store', \
			default="en", \
			help="Choose language: ru, en, .. (etc.)")
	#--browser - имя браузера: chrome/ch; firefox/ff
	parser.addoption('--browser', \
			action='store', \
			default="chrome", \
			help="Choose browser: chrome(ch) or firefox(ff)")

def pytest_configure(config):
	#добавляем свои маркеры pytest
	config.addinivalue_line(
		"markers", "main_page: test main page at site"
	)
	config.addinivalue_line(
		"markers", "about_page: test about page at site"
	)
	config.addinivalue_line(
		"markers", "contact_page: test contact page at site"
	)
#	config.addinivalue_line(
#		"markers", "basket: test?"
#	)
	

@pytest.fixture(scope="function")
def browser(request):
	user_language = request.config.getoption("language")
	browser_name = request.config.getoption("browser")
	

	#run browser with emply sheet
	if (browser_name == "chrome")or(browser_name == "ch"):
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		print ("\n\nstart Chrome-browser for test..")
		browser = webdriver.Chrome(options=options)
	elif (browser_name == "firefox")or(browser_name == "ff"):
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", user_language)
		print ("\n\nstart Firefox-browser for test..")
		browser = webdriver.Firefox(firefox_profile=fp)
	else:
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		print ("\n\nYour chouse browser not supplied\nstart Chrome-browser for test..")
		browser = webdriver.Chrome(options=options)
	browser.implicitly_wait(4)

	yield browser

	print("\nquit browser..")
	browser.quit()

#пустая строка в конце файла
