import modules  as md

# Testing if solutions page is opened from 'Learn More' button

print("TEST 3: Started")
solutions=md.driver.find_element(by=md.By.XPATH, value="/html/body/div[2]/div[1]/main/div/section[2]/div/div/div[2]/div[2]/a")
solutions.click()
md.sleep(3)

html_from_page = md.driver.page_source
soup = md.BeautifulSoup(html_from_page, 'html.parser') # Getting the source of the next page clicked
title_solutions = str(soup.title).lower()

assert "solutions" in title_solutions
assert md.driver.current_url == 'https://profilence.com/solutions/solutions-overview/'

print("TEST 3: Passed!")

md.driver.close()