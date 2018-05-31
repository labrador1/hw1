import numpy as np
import itertools
from operator import itemgetter
import re

#16文字を組み合わせ、一番得点が高い単語を探索する関数
def main(letters, dic):
	letter_list = []	
	total_list = []
	high_score = 0
	high_word = ""

	#入力した文字から組み合わせを求める
	letters = re.sub("qu", "q", letters.lower())
	for i in range(len(letters) + 1):
	  a_list = list(itertools.combinations(letters,i))
	  letter_list.extend(a_list)

	#先頭の空配列は消す
	del letter_list[0] 

	#それぞれの組み合わせを昇順に並べて、リストにする
	for m in letter_list:
		b_list = list(m)
		b_list.sort()
		b_str = map(str,b_list)
		b_list = ("".join(b_str))
		total_list.append(b_list)

	#binary search 
	for n in total_list:
		low = 0
		high = len(dic) - 1
		t = int(len(dic) / 2)
		while (low <= high):
			if (n == dic[t,1]):
				#point関数を呼び出し、high_wordsに得点が最大となるwordを代入する。	
				curr_score = point(n)			
				if(high_score < curr_score):
					high_score = curr_score
					high_word = dic[t,0]
				break
			elif (n > dic[t,1]):
				low = t + 1
			elif (n < dic[t,1]):
				high = t - 1
			t = int((low + high) / 2)

	#得点が最大となるwordとscoreを表示する。		
	print('word : ' + high_word)
	print('score : ' + str(high_score))
	return(high_word, high_score)

#辞書を並び替える関数
def dictionary():
	dic_list = []
	#辞書を読み込む
	with open('dictionary_words.txt', "r") as f:
	    data = [v.rstrip() for v in f.readlines()]
	    j = 0
	    #quをqに変換
	    for i in data:
	    	data[j]  = re.sub("qu", "q", i)
	    	j = j + 1

	for k in data:
		list1 = list(k)
		list1.sort()
		list1 = ("".join(list1))
		dic_list.append(list1)

	#元の辞書の単語をkey,それを昇順で並び替えたものをvalueにした辞書型を作成
	#辞書型をvalueの昇順に並び替えて、二次元配列となる
	dic = dict(zip(data, dic_list)) 
	dic = sorted(dic.items(), key=lambda x:x[1])
	dic = np.array(dic)
	return dic


#単語のscoreを求める関数
def point(words):
	keys = ['a', 'b', 'd', 'e', 'g', 'i', 'n', 'o', 'r', 's', 't', 'u', 'c', 'f', 'h' ,'l', 'm', 'p', 'v', 'w', 'y', 'q', 'j', 'k', 'x', 'z']
	values = [1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3]
	#keyが文字、valueがscoreの辞書型を作成
	dic2 = dict(zip(keys, values)) 

	#scoreの計算
	value =  1
	for i in list(words.lower()):
		value += dic2[i]
	value = pow(value, 2)
	return value



