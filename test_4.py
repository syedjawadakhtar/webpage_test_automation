import modules as md

# Checking if 'Demo Request' button works on the homepage
print("TEST 4: Started")
demo_button = md.driver.find_element(by=md.By.XPATH, value="/html/body/div[2]/div[1]/main/div/section[1]/div[1]/div/div[2]/div[2]/a")
demo_button.click()
md.sleep(3)

html_from_page = md.driver.page_source
soup = md.BeautifulSoup(html_from_page, 'html.parser') # Getting the source of the next page clicked
title_demo = str(soup.title).lower()

assert "demo" in title_demo
assert md.driver.current_url == "https://profilence.com/demo-request/"

print("TEST 4: Passed!")
md.driver.close()