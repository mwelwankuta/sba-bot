import csv

from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Bot:
	def __init__(self):
		print('\nSTARTING BOT...\n\n') 
		self.browser = webdriver.Chrome('chromedriver.exe')
		self.browser.get('http://www.omes.exams-council.org.zm/g7/login.php')
		self.subject = 3

		# keeps track of current learner.
		self.count = 0

	def login(self, username, password):
		if len(username) < 1 or len(password) < 1:
			return print("\nERROR: you need to provide bot username and password")

		print(f'\nLOGGED IN AS: {username}\n') 

		self.browser.find_element_by_xpath("//*[@id='username']").send_keys(username)
		self.browser.find_element_by_xpath("//*[@id='password']").send_keys(password)
		self.browser.find_element_by_xpath("/html/body/div/form/input").click()

		# navigate to sba mark schedule
		self.browser.find_element_by_xpath("/html/body/div/div[2]/ul/li[4]/a").click()

	def select_subject(self, name='ENGLISH LANGUAGE', status_code='L'):
		print(f'\nSELECTED {name}\n')
		self.name = name 

		# subject code
		# matches array index of subject with csv data
		if name == 'MATHEMATICS': self.subject = 3
		if name == 'ENGLISH LANGUAGE': self.subject = 4
		if name == 'INTEGRATED SCIENCE': self.subject = 5
		if name == 'ICIBEMBA': self.subject = 6
		if name == 'CREATIVE AND TECHNOLOGY STUDIES': self.subject = 7
		if name == 'SOCIAL STUDIES': subject = 8

		# select subject name
		Select(self.browser.find_element_by_xpath("/html/body/div/div[3]/div/form/div[1]/select")).select_by_visible_text(name)
		# select status
		Select(self.browser.find_element_by_xpath("/html/body/div/div[3]/div/form/div[2]/select")).select_by_visible_text(status_code)

		# submit form
		self.browser.find_element_by_xpath("/html/body/div/div[3]/div/form/div[3]/button").click()

		return self

	def enter_mark(self, mark=0):
		id = self.count

		mark_input = self.browser.find_element_by_xpath(f"/html/body/div/div[3]/div/form/div/table/tbody/tr[{id}]/td[7]/input")

		mark_input.clear() # clear input
		mark_input.send_keys(mark) # add mark


	def enter_data(self, file):
		if file == None:
			return print('Error: a file was not passed.')

		# open data
		with open(file, 'r') as data:
			csv_reader = csv.reader(data)
			self.count = self.count + 1
			# skip first line, is title
			next(csv_reader)

			for line in csv_reader:
				self.enter_mark(mark=line[self.subject])

				print(f'ENTERED: {line[2]}    --> {line[self.subject]}') 
				self.count = self.count + 1
			
			print(f'\n\nCOMPLETED ENTERING {self.name} \n')

			# close browser
			self.browser.close()

			# close file reader
			data.close()
