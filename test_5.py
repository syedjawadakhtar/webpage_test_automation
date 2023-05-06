import modules as md

# Testing Navbar

print("TEST 5: Started")
solutions=md.driver.find_element(by=md.By.XPATH, value="/html/body/div[2]/div[1]/header/div/div/button")
solutions.click()
md.sleep(3)

sections_nav_bar = md.driver.find_elements(md.By.CLASS_NAME, "menu-item")
assert len(sections_nav_bar) == 6

print("TEST 5: Passed")
md.driver.close()