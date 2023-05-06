import modules as md

# Subscribing to newsletter

print("TEST 2: Started")

md.driver.find_element(md.By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection").click()
md.driver.find_element(md.By.ID, "contact-email").send_keys("standard_user@gmail.com")
terms_btn = md.driver.find_element(md.By.ID, "contact-accept")
terms_btn.click()
submit_button = md.driver.find_element(md.By.XPATH, value="/html/body/div[2]/div[1]/main/div/section[9]/div/div/div[2]/div/form/button/span")
submit_button.click()

md.sleep(3) # Waiting for it to subscribe

assert "Thank you" in md.driver.page_source

print("TEST 2: Passed!")

md.driver.close()