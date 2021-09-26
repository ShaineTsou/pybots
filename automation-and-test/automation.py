# -----  With great power, comes great responsibility. Be ethical.  -----

# Use Selenium to automatically test website using chromedriver
# Create a virtual environment, and install selenium (https://selenium-python.readthedocs.io/installation.html)
# Install chromedriver on your machine (https://sites.google.com/chromium.org/driver/)
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# Test if we are on the right page
assert 'Selenium Easy Demo' in browser.title

# Test if the element is in the page
assert 'Get Total' in browser.page_source

# Grab inputs
value_a = browser.find_element_by_css_selector('div.form-group>input#sum1')
value_b = browser.find_element_by_css_selector('div.form-group>input#sum2')

# Make sure there is no text in the input
value_a.clear()
value_b.clear()

value_a.send_keys('56')
value_b.send_keys('98')

# Grab the button (Get Total) we want to test
get_total_btn = browser.find_elements_by_class_name(
    'btn-default')[1]

get_total_btn.click()

# Grab to display value and test the value
display_value = browser.find_element_by_id('displayvalue')
assert '154' in display_value.text

# Close the browser window
# browser.close()

# Or quit the entire chrome driver
browser.quit()
