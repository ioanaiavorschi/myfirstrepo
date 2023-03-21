from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
chrome = webdriver.Chrome()

class Test(unittest.TestCase):
    def test1(self):
        chrome.get('https://the-internet.herokuapp.com/login')
        actual = chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test2(self):
        chrome.get('https://the-internet.herokuapp.com/login')
        actual = chrome.find_element(By.XPATH, "//h2").text
        expected = "Login Page"
        self.assertEqual(expected, actual, "page title incorect")

    def test4(self):
        chrome.get('https://the-internet.herokuapp.com/login')
        actual = chrome.find_element(By.XPATH, "//i").text
        expected = "Login"
        self.assertEqual(expected, actual, "nu este afisat buton de login")

    def test5(self):
        chrome.get('https://the-internet.herokuapp.com/login')
        actual = chrome.find_element(By.XPATH, '//a[@href="http://elementalselenium.com/"]').text
        expected = "Elemental Selenium"
        self.assertEqual(expected, actual, "textul nu este acelasi")

    def test6(self):
        chrome.get('https://the-internet.herokuapp.com/login')
        actual = chrome.find_element(By.XPATH,'//div[@id="flash"]')
        expected = "User name is invalid!"
        self.assertEqual(expected, actual, "textul de eroare nu este acelasi")

    def test11(self):
        chrome.get('https://the-internet.herokuapp.com/login')
        actual = chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, "Url nu este acelasi")


