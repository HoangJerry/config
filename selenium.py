
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import *
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

def buyfromwish(request,user,code):
    # url = "https://www.wish.com/c/582912c74e6ae91dd2807baf"
    # response = urllib.urlopen(url)
    # print response.read()
    # # # return response.read()
    # return render(request,response.read() , {})
    # browser = webdriver.Chrome('/var/www/html/HoangTN/project/merchant-wish-django/chromedriver')
    # browser = webdriver.Chrome()
    # import pdb
    # pdb.set_trace()
    # display = Display(visible=0, size=(800, 800))  
    # display.start()
    customer = OneDollarUser.objects.filter(id=user)[0]
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-setuid-sandbox")
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver.get("http://www.google.com")
    # print driver.page_source.encode('utf-8')
    # driver.quit()
    
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('https://www.wish.com/c/58b7e6eafdcf3e3cf77dd836')
    # first_result = ui.WebDriverWait(browser, 15).until(lambda browser: browser.find_element_by_class_name('rc'))
    # first_link = first_result.find_element_by_tag_name('a')
    main_window = browser.current_window_handle
    # login = browser.find_element_by_css_selector('#signup-form')
    sleep(0.5)
    fb = browser.find_element_by_css_selector('#signup-form .fb-login-btn.btn.cronkite')
    
    action = ActionChains(browser)
    action.click(fb).perform()

    print "coca"
    print browser.current_url

    # Switch to new window opened
    for handle in browser.window_handles:
        browser.switch_to_window(handle)

    user = browser.find_element_by_css_selector('.inputtext._55r1.inputtext.inputtext')
    user.send_keys("0993592412")

    user.send_keys(Keys.TAB)
    browser.switch_to_active_element().send_keys('hoangtnfacebook123123')
    browser.switch_to_active_element().send_keys(Keys.ENTER)
    sleep(0.5)
    browser.switch_to_window(main_window)
    print browser.current_url

    #Buy click
    buy = browser.find_element_by_css_selector('.buy-button-style.buy-button-link.add-to-cart')
    action.reset_actions()
    action.click(buy).perform()

    #Edit click
    edit = browser.find_element_by_css_selector('#edit-shipping-info')
    action.reset_actions()
    action.click(edit).perform()
    print browser.current_url
    sleep(1)
    first_name = browser.find_element_by_css_selector('input#first-name')
    print browser.current_url
    first_name.clear()
    first_name.send_keys(customer.first_name)
    first_name.send_keys(Keys.TAB)
    browser.switch_to_active_element().send_keys(customer.last_name)
    browser.switch_to_active_element().send_keys(Keys.TAB)
    browser.switch_to_active_element().send_keys(customer.street1)
    browser.switch_to_active_element().send_keys(Keys.TAB)
    browser.switch_to_active_element().send_keys(customer.street2)
    browser.switch_to_active_element().send_keys(Keys.TAB)
    # browser.switch_to_active_element().send_keys("V")
    browser.switch_to_active_element().send_keys(Keys.TAB)
    browser.switch_to_active_element().send_keys(customer.city)
    browser.switch_to_active_element().send_keys(Keys.TAB)
    browser.switch_to_active_element().send_keys(customer.province)
    browser.switch_to_active_element().send_keys(Keys.TAB)
    browser.switch_to_active_element().send_keys(customer.postal_code)
    browser.switch_to_active_element().send_keys(Keys.TAB)
    browser.switch_to_active_element().send_keys(int(customer.phone))
    browser.maximize_window()
    sleep(0.5)
    submit_button = browser.find_element_by_css_selector('#submit-form-btn-container .cronkite')
    action.reset_actions()
    action.click(submit_button).perform()

    # sleep(1)
    # remove = browser.find_element_by_css_selector('.grey-btn.simplemodal-close')
    # action.reset_actions()
    # action.click(remove).perform()

    submit_button = browser.find_element_by_css_selector('#submit-form-btn-container .cronkite')
    action.reset_actions()
    action.click(submit_button).perform()

    browser.back()

    remove = browser.find_element_by_css_selector('.remove-item.clickable.cronkite')
    action.reset_actions()
    action.click(remove).perform()
    
    comfirm = browser.find_element_by_css_selector('.grey-btn.confirm-btn')
    action.reset_actions()
    action.click(comfirm).perform()
    # Close current tab
    # sleep(15)
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    browser.quit()
    # display.stop()
    # return JsonResponse({'status':1})
    return HttpResponseRedirect('https://www.wish.com/c/'+code)
