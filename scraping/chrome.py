from selenium import webdriver

def get_browser(headless=False) -> webdriver.Chrome:
    # initialize and configure browser
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')
    options.add_argument(f'user-agent={agent}')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    return browser
