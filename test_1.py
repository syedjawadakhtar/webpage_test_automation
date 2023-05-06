import modules as md

# Testing if correct website is opened

print("TEST 1: Started")

# Get page title
title = md.driver.title
# print(title) # Debugging title

# Test if title is correct
assert "Profilence" in title

print("TEST 1: Passed!")

md.driver.close()