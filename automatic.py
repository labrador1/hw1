#automatic.pyを実行し、search.pyを呼び出す
from selenium import webdriver
import search

#chromedriverのpathを指定する
browser = webdriver.Chrome(executable_path='/Users/MatsumotoNasa/Desktop/step/hw1/chromedriver')
browser.get('https://icanhazwordz.appspot.com/')

total_score = 0
#search.pyのdictionary関数を呼び出す
dic = search.dictionary()

#単語入力を10回繰り返す
for i in range(10):
	character = ""
	letters = ""

	#ゲームのWebサイトから16文字を読み込む
	for i in range(1,5):
		for j in range(1,5):
			character = browser.find_element_by_xpath('//table[1][@border="2"]/tbody/tr/td[1]/table/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/div')
			letters = letters + character.text

	#search.pyのmain関数を呼び出す
	high = search.main(letters, dic)
	high_words = high[0]
	total_score = total_score + high[1]

	#scoreをSubmitする。16文字で１つも単語が作れない場合はPASSする。
	if (high[1] > 0): 
		browser.find_element_by_id("MoveField").send_keys(high_words)
		browser.find_element_by_xpath('//input[@type="submit"]').click()
	else:
		browser.find_element_by_name('pass').click()

#total score を出力
print('total_score = ' + str(total_score))