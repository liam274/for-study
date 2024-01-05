import selenium
from selenium import webdriver
chrome_opt=webdriver.chrome.options.Options()
chrome_opt.add_experimental_option("debuggerAddress","localhost:9222")
d=webdriver.Chrome(options=chrome_opt)
d.get("google.com")
while True:
    tabs=d.window_handles
    for tab in tabs:
        d.switch_to.window(tab)
        current_url=d.current_url
        if current_url=="chrome://dino":
            d.close()
