from selenium import webdriver

browser = webdriver.Firefox(executable_path=r"C:\Windows\geckodriver.exe")
browser.get("https://github.com")


browser.maximize_window() 
browser.implicitly_wait(20)
sign_in = browser.find_element_by_link_text("Sign in")
sign_in.click()

user_name = browser.find_element_by_id("login_field")
user_name.send_keys("user_name")
password = browser.find_element_by_id("password")
password.send_keys("password")
password.submit()


profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "username" in link_label

browser.quit()
