from selenium.webdriver.common.by import By

class BaseSPageLocators():
	ABOUT_LINK = (By.CSS_SELECTOR, "div.horzmenu > ul > li:nth-child(2) > a")
	MAIN_LINK = (By.CSS_SELECTOR, "div.horzmenu > ul > li:nth-child(1) > a")
	PORTFOLIO_LINK = (By.CSS_SELECTOR, "div.horzmenu > ul > li:nth-child(3) > a")
	CONTACT_LINK = (By.CSS_SELECTOR, "div.horzmenu > ul > li:nth-child(4) > a")
	SCYPE_LINK = (By.CSS_SELECTOR, "div.divSocialIcons > a:nth-child(1)")
	GITHUB_LINK = (By.CSS_SELECTOR, "div.divSocialIcons > a:nth-child(2)")


class MainPageLocators():
	ORDER_FORM = (By.CSS_SELECTOR, "div.order_wrapper > form")
	USERNAME_FORM = (By.CSS_SELECTOR, "div.order_wrapper > form > div.wrapper_form > #userName")
	USERMAIL_FORM = (By.CSS_SELECTOR, "div.order_wrapper > form > div.wrapper_form > #userMail")
	USERFILES_FORM = (By.CSS_SELECTOR, "div.order_wrapper > form > div.wrapper_form > #userFiles")
	USERCOMMENT_FORM = (By.CSS_SELECTOR, "div.order_wrapper > form > div.wrapper_form > #userComment")
	SUBMIT_FORM = (By.CSS_SELECTOR, "div.order_wrapper > form > div.wrapper_form > [type=submit]")
	PHOTO_IMG = (By.CSS_SELECTOR, "img.dragoPhoto")


class AboutPageLocators():
	ORDER_INPUT = (By.CSS_SELECTOR, "input.feat")
	ORDER_BOTTOM_INPUT = (By.CSS_SELECTOR, "div.bottomLine > input.feat160C")


class ContactPageLocators():
	ORDER_BOTTOM_INPUT = (By.CSS_SELECTOR, "div.footer > input.feat160C")
	MAIL_FORM = (By.CSS_SELECTOR, "div.div_send > form")
	USERNAME_FORM = (By.CSS_SELECTOR, "div.div_send > form > #name")
	USERMAIL_FORM = (By.CSS_SELECTOR, "div.div_send > form > #email")
	SUBJECT_FORM = (By.CSS_SELECTOR, "div.div_send > form > #subject")
	CONTENT_FORM = (By.CSS_SELECTOR, "div.div_send > form > #content")
	SUBMIT_FORM = (By.CSS_SELECTOR, "div.div_send > form > [type=submit]")


#stepik
class loginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class WarePageLocators():
	ADDTOCART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner")
	MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
	
	
class BasketPageLocators():
	BASKET_SUMMARY_FORM = (By.CSS_SELECTOR, "#basket_formset")
	BASKET_TEXT_EMPTY = (By.CSS_SELECTOR, "#content_inner p")


#пустая строка в конце файла
