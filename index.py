from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

contato = input('Digite o nome do contato que você deseja responder: ')

class Whatsapp():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def config(self):
    self.driver.get("https://web.whatsapp.com/")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2zCfw").click()
    self.driver.find_element(By.CSS_SELECTOR, ".hover > .\\_2WP9Q").click()

    if(contato == ''):
      print('ERROR!')
    else:
      self.driver.find_element(By.CSS_SELECTOR, ".\\_2zCfw").send_keys(contato)
      self.driver.find_element(By.CSS_SELECTOR, ".\\_3u328").click()
      self.driver.find_element(By.CSS_SELECTOR, ".\\_13mgZ").click()
      self.driver.find_element(By.CSS_SELECTOR, ".Kwld2 span").click()
      self.driver.find_element(By.CSS_SELECTOR, ".b46:nth-child(5)").click()
      self.driver.find_element(By.CSS_SELECTOR, ".\\_3M-N- > span").click()
      self.driver.find_element(By.CSS_SELECTOR, ".\\_3u328").click()

      self.driver.find_element(By.CSS_SELECTOR, ".\\_13mgZ").click()
      self.driver.find_element(By.CSS_SELECTOR, ".\\_13mgZ").click()
      self.driver.find_element(By.CSS_SELECTOR, ".\\_3u328").click()

      self.driver.find_element(By.CSS_SELECTOR, ".\\_2WP9Q:nth-child(2) .\\_19RFN:nth-child(2)").click()
      self.driver.find_element(By.CSS_SELECTOR, ".hover .\\_19RFN").click()
      self.driver.find_element(By.CSS_SELECTOR, ".\\_3u328").click()
      self.driver.find_element(By.CSS_SELECTOR, ".\\_3M-N- > span").click()
    
