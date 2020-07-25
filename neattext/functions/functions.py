# -*- coding: utf-8 -*-
# This file is part of the NEAT Project suite of libraries

import re
from neattext.pattern_data import EMAIL_REGEX,NUMBERS_REGEX,PHONE_REGEX,SPECIAL_CHARACTERS_REGEX,EMOJI_REGEX,URL_PATTERN,CURRENCY_REGEX,CURRENCY_SYMB_REGEX,STOPWORDS,DATE_REGEX
from neattext import TextFrame
from collections import defaultdict
from heapq import nlargest
import random,string


# Individual Functions
def remove_emails(text):
	"""Returns A String with the emails removed """
	result = re.sub(EMAIL_REGEX,"",text)
	return result

def remove_numbers(text):
	"""Returns A String with the numbers/digits removed """
	result = re.sub(NUMBERS_REGEX,"",text)
	return result

def remove_phone_numbers(text):
	"""Returns A String with the phone numbers removed """
	result = re.sub(PHONE_REGEX,"",text)
	return result

def remove_puncts(text):
	"""Returns A String with punctuations remove"""
	PUNCT_REGEX = re.compile(r"""[!"&'()*,-./:;?@[\\]^_`{|}]""")
	result = re.sub(PUNCT_REGEX,"",text)
	return result


def remove_special_characters(text):
	"""Returns A String with the specified characters removed """
	result = re.sub(SPECIAL_CHARACTERS_REGEX,"",text)
	return result

def remove_emojis(text):
	"""Returns A String with the emojis removed """
	result = re.sub(EMOJI_REGEX,"",text)
	return result

def remove_stopwords(text):
	"""Returns A String with the stopwords removed """
	result = [word for word in text.split() if word not in STOPWORDS]
	return ' '.join(result)

def remove_urls(text):
	"""Returns A String with URLS removed """
	result = re.sub(URL_PATTERN,"",text)
	return result

def remove_currencies(text):
	"""Returns A String with Currencies removed """
	result = re.sub(CURRENCY_REGEX,"",text)
	return result

def remove_currency_symbols(text):
	"""Returns A String with Currency Symbols removed """
	result = re.sub(CURRENCY_SYMB_REGEX,"",text)
	return result


def extract_emails(text):
	"""Returns the emails extracted """
	result = re.findall(EMAIL_REGEX,text)
	return result
	
def extract_numbers(text):
	"""Returns the numbers/digits extracted """
	result = re.findall(NUMBERS_REGEX,text)
	return result
	
def extract_phone_numbers(text):
	"""Returns the phone number extracted """
	result = re.findall(PHONE_REGEX,text)
	return result
	
def extract_special_characters(text):
	"""Returns the specified characters extracted """
	result = re.findall(SPECIAL_CHARACTERS_REGEX,text)
	return result
	
def extract_emojis(text):
	"""Returns the emojis extracted """
	result = re.findall(EMOJI_REGEX,text)
	return result
	
def extract_stopwords(text):
	"""Returns the stopwords as a list """
	result = [word for word in text.split() if word in STOPWORDS]
	return result
	
def extract_urls(text):
	"""Returns the URLS extracted """
	result = re.findall(URL_PATTERN,text)
	return result

def extract_currencies(text):
	"""Returns the currencies extracted """
	result = re.findall(CURRENCY_REGEX,text)
	return result

def extract_currency_symbols(text):
	"""Returns the currency symbols extracted """
	result = re.findall(CURRENCY_SYMB_REGEX,text)
	return result

def extract_dates(text):
		"""Returns the dates extracted """
		result = re.findall(DATE_REGEX,text)
		return result


def clean_text(text,preserve=False):
	"""Clean Entire Text"""
	if preserve == False:
		email_result = re.sub(EMAIL_REGEX,"",text)
		phone_result = re.sub(PHONE_REGEX,"",email_result)
		number_result = re.sub(NUMBERS_REGEX,"",phone_result)
		url_result = re.sub(URL_PATTERN,"",number_result)
		emoji_result = re.sub(EMOJI_REGEX,"",url_result)
		special_char_result = re.sub(SPECIAL_CHARACTERS_REGEX,"",emoji_result)
		final_result = special_char_result.lower()
	else:
		email_result = re.sub(EMAIL_REGEX,"<EMAIL>",text)
		phone_result = re.sub(PHONE_REGEX,"<PHONENUMBER>",email_result)
		number_result = re.sub(NUMBERS_REGEX,"<NUMBERS>",phone_result)
		url_result = re.sub(URL_PATTERN,"<URL>",number_result)
		emoji_result = re.sub(EMOJI_REGEX,"<EMOJI>",url_result)
		final_result = emoji_result.lower()

	return final_result

def replace_emails(text,replace_with="<EMAIL>"):
	"""Replaces the emails in the text with custom label"""
	result = re.sub(EMAIL_REGEX,replace_with,text)
	return result

def replace_phone_numbers(text,replace_with="<PHONENUMBER>"):
	"""Replaces the phone numbers in the text with custom label"""
	result = re.sub(PHONE_REGEX,replace_with,text)
	return result

def replace_numbers(text,replace_with="<NUMBER>"):
	"""Replaces numbers/digits in the text with custom label"""
	result = re.sub(NUMBERS_REGEX,replace_with,text)
	return result

def replace_special_characters(text,replace_with="<SPECIAL_CHAR>"):
	"""Replaces special characters in the text with custom label"""
	result = re.sub(SPECIAL_CHARACTERS_REGEX,replace_with,text)
	return result

def replace_emojis(text,replace_with="<EMOJI>"):
	"""Replaces emojis in the text with custom label"""
	result = re.sub(EMOJI_REGEX,replace_with,text)
	return result

def replace_urls(text,replace_with="<URL>"):
	"""Replaces URLS/HTTP(S) in the text with custom label"""
	result = re.sub(URL_PATTERN,replace_with,text)
	return result

def replace_currencies(text,replace_with="<CURRENCY>"):
	"""Replaces Currencies in the text with custom label"""
	result = re.sub(CURRENCY_REGEX,replace_with,text)
	return result

def replace_currency_symbols(text,replace_with="<CURRENCY_SYMB>"):
	"""Replaces currency symbols in the text with custom label"""
	result = re.sub(CURRENCY_SYMB_REGEX,replace_with,text)
	return result


def replace_dates(text,replace_with="<DATE>"):
	"""Replaces Dates in the text with custom label"""
	result = re.sub(DATE_REGEX,replace_with,text)
	return result

def replace_term(text,old_term,new_term):
	"""Replaces term in the text with another term"""
	result = re.sub(old_term,new_term,text)
	return result


def read_txt(filename):
	"""
		Read a Text File and Create A TextFrame From it

		
		Parameters
		----------
		text : Main Text
		filename : file with text to read

		Returns
		----------
		Returns a TextFrame for text
	"""
	with open(filename,'r') as f:
		text_read = f.read()
		docx_tf = TextFrame(text_read)
	return docx_tf


def to_txt(text,filename):
	"""
		Save/Write a Text  to A File 

		
		Parameters
		----------
		text : Main Text
		filename : file with text to write/save to

		Returns
		----------
		Creates A New File with Text on it
		

		"""
	with open(filename,'w') as f:
		f.write(text)
		

def hamming_distance(lhs,rhs):
	"""Returns the Hamming Distance of Two Equal Strings

	Usage
	>>> nt.hamming_distance('Pear','Pearls')
	"""
	return len([(x,y) for x,y in zip(lhs,rhs) if x !=y])


__numbers_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
			 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
			11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
			15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
			19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
			50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
			90: 'Ninety', 0: 'Zero',100: 'Hundred',200: 'Two Hundred',300:'Three Hundred',
			400: 'Four Hundred',500:'Five Hundred',600:'Six Hundred',700:'Seven Hundred',
			800: 'Eight Hundred',900:'Nine Hundred',1000:'Thousand',100000:'Hundred Thousand'}


def num2words(num):
		try:
			result = __numbers_dict[num]
		except KeyError:
			try:
				# Find the decimal(tens) using numb - modulus of number and add the remainder to it
				result = __numbers_dict[num-num%10] + __numbers_dict[num%10].lower()
			except KeyError:
				print('Number out of range')
		return result 


def digit2words(num):
	try:
		result = __numbers_dict[num]
	except KeyError:
		num_length = len(str(num))
		if num_length == 2:
			# Find the decimal(tens) using numb - modulus of number and add the remainder to it
			result = __numbers_dict[num-num%10] + __numbers_dict[num%10].lower()
		elif num_length == 3:
			result = __numbers_dict[num-num%100] + __numbers_dict[num%10].lower() 
		elif num_length == 4:
			result = __numbers_dict[num-num%1000] + __numbers_dict[num%10].lower()
		elif num_length == 5:
			result = __numbers_dict[num-num%10000] + __numbers_dict[num%10].lower()
		elif num_length == 6:
			result = __numbers_dict[num-num%100000] + __numbers_dict[num%10].lower()
		elif num_length == 7:
			result = __numbers_dict[num-num%1000000] + __numbers_dict[num%10].lower()
		elif num_length == 8:
			result = __numbers_dict[num-num%10000000] + __numbers_dict[num%10].lower()
		elif num_length == 9:
			result = __numbers_dict[num-num%100000000] + __numbers_dict[num%100000000].lower()
		else:
			print("Number out of range")


	return result


# def summarize(raw_docx):
# 	""" usage: summarize(yourtext) """
	
# 	raw_text = raw_docx
# 	docx = TextFrame(raw_text)
# 	stopwords = list(STOPWORDS)
# 	# Build Word Frequency # word.text is tokenization in spacy
# 	word_frequencies = {}  
# 	for word in docx.text.split():  
# 		if word not in stopwords:
# 			if word not in word_frequencies.keys():
# 				word_frequencies[word] = 1
# 			else:
# 				word_frequencies[word] += 1

# 	print(word_frequencies)
# 	maximum_frequncy = max(word_frequencies.values())

# 	for word in word_frequencies.keys():  
# 		word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
# 	# Sentence Tokens
# 	print(word_frequencies)
# 	sentence_list = [ sentence for sentence in docx.text.split() ]
# 	print(sentence_list)
# 	#Calculate Sentence Scores
# 	sentence_scores = {}  
# 	for sent in sentence_list:  
# 		for word in sent:
# 			if word.lower() in word_frequencies.keys():
# 				if len(sent.split(' ')) < 5:
# 					if sent not in sentence_scores.keys():
# 						sentence_scores[sent] = word_frequencies[word.lower()]
# 					else:
# 						sentence_scores[sent] += word_frequencies[word.lower()]
# 	print(sentence_scores)
# 	# Find N Largest and Join Sentences
# 	summarized_sentences = nlargest(10, sentence_scores, key=sentence_scores.get)
# 	final_sentences = [ w for w in summarized_sentences ]
# 	print(final_sentences)
# 	print(summarized_sentences)
# 	summary = ' '.join(final_sentences)
# 	return summary
	


# Source https://github.com/adashofdata/nlp-in-python-tutorial/blob/master/5-Text-Generation.ipynb
def markov_chain(text):
	"""Returns a dictionary with each word as
	   a key and each value as the list of words that come after the key in the text."""
	
	# Tokenize the text by word, though including punctuation
	words = text.split(' ')
	
	# Initialize a default dictionary to hold all of the words and next words
	m_dict = defaultdict(list)
	
	# Create a zipped list of all of the word pairs and put them in word: list of next words format
	for current_word, next_word in zip(words[0:-1], words[1:]):
		m_dict[current_word].append(next_word)

	# Convert the default dict back into a dictionary
	m_dict = dict(m_dict)
	return m_dict
	


def __generate_text(chain, count=15):
	'''Input a dictionary in the format of key = current word, value = list of next words
	   along with the number of words you would like to see in your generated sentence.'''

	# Capitalize the first word
	word1 = random.choice(list(chain.keys()))
	sentence = word1.capitalize()

	# Generate the second word from the value list. Set the new word as the first word. Repeat.
	for i in range(count-1):
		word2 = random.choice(chain[word1])
		word1 = word2
		sentence += ' ' + word2

	# End it with a period
	sentence += '.'
	# print(sentence)
	return(sentence)




def generate_sentence(text,num_of_words=15):
	"""Returns a new sentence/text From a given text using Markov Chains
	
	Parameters
	----------
	text : Main Text
	num_of_words : number of words to generate

	Returns
	----------
	Returns a new sentence of the number of words specified
	
	Usage
	------
	>>> from neattext.functions import generate_sentence
	>>> t1 = "your text...here"
	>>> generate_sentence(t1)
	>>> generate_sentence(t1,20)
	
	#Alternatively generate 4 sentences
	>>> for i in range(4):
		print(generate_sentence(t1))
	
	
	"""
	result_dict = markov_chain(text)
	final_result_sentence = __generate_text(result_dict,num_of_words)
	return final_result_sentence

def normalize(text,level='shallow'):
	"""Normalize Text by converting to lowercase,removing punctuations and square brackets

	Parameters
	----------
	text : Main Text
	level : level of normalization (shallow/deep)
		shallow:lowercase,remove text in brackets and digits
		deep: shallow + removing puncts,emojis,bad commas,etc
	Returns
	----------
	Returns a new clean and normalized sentence
	
	Usage
	------
	>>> from neattext.functions import normalize
	>>> t1 = "your text...here"
	>>> normalize(t1)
	
	#Alternatively
	>>> normalize(t1,level='deep')
	"""
	
	if level == 'shallow':
		# Lowercase
		text = text.lower() 
		# Remove Txt in Square Bracket
		text = re.sub('\\[.*?\\]', '', text) 
		text = re.sub('\\w*\\d\\w*', '', text) 

	elif level == 'deep':
		# Lowercase
		text = text.lower() 
		# Remove Txt in Square Bracket
		text = re.sub('\\[.*?\\]', '', text) 
		# Remove Digit containing words
		text = re.sub('\\w*\\d\\w*', '', text) 
		# Remove Punct
		text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
		# Remove Bad Quotations
		text = re.sub('[‘’“”…]', '', text)
		# Remove emojis
		text = re.sub(EMOJI_REGEX,"",text)

	return text
	


def fix_contractions(text):
	"""Fix contractions in a text"""
	text = text.lower()
	text = re.sub(r"i'm", "i am", text)
	text = re.sub(r"he's", "he is", text)
	text = re.sub(r"she's", "she is", text)
	text = re.sub(r"that's", "that is", text)        
	text = re.sub(r"what's", "what is", text)
	text = re.sub(r"where's", "where is", text) 
	text = re.sub(r"\'ll", " will", text)  
	text = re.sub(r"\'ve", " have", text)  
	text = re.sub(r"\'re", " are", text)
	text = re.sub(r"\'d", " would", text)
	text = re.sub(r"\'ve", " have", text)
	text = re.sub(r"won't", "will not", text)
	text = re.sub(r"don't", "do not", text)
	text = re.sub(r"did't", "did not", text)
	text = re.sub(r"can't", "can not", text)
	text = re.sub(r"it's", "it is", text)
	text = re.sub(r"couldn't", "could not", text)
	text = re.sub(r"have't", "have not", text)
	return text


def word_freq(text):
	"""Returns a term/word frequency"""
	stopwords = list(STOPWORDS)
	# Build Word Frequency(bag) # word.text is tokenization in spacy
	word_frequencies = {}  
	for word in text.split():  
		if word not in stopwords:
			if word not in word_frequencies.keys():
				word_frequencies[word] = 1
			else:
				word_frequencies[word] += 1

	# print(word_frequencies)
	maximum_frequency = max(word_frequencies.values())

	for word in word_frequencies.keys():  
		word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
	
	return word_frequencies


def term_freq(text):
	""" Returns the Term Frequency of Words in a Sentence

	Definition
	---------
	The number of times a word appears in a document divided by the total number of words in the document. 
		
	Formular
	---------
	TF = (Frequency of the word in the sentence) / (Total number of words in the sentence)

	"""
	stopwords = list(STOPWORDS)
	# Build Bag of Words or Word Frequency(bag) # 
	term_frequencies = {}  
	for word in text.split():  
		if word not in stopwords:
			if word not in term_frequencies.keys():
				term_frequencies[word] = 1
			else:
				term_frequencies[word] += 1

	
	maximum_frequency = max(term_frequencies.values())

	for word in term_frequencies.keys():  
		term_frequencies[word] = (term_frequencies[word]/maximum_frequency)
	
	return term_frequencies
	
def inverse_df(text):
	"""IDF: log((Total number of sentences (documents))/(Number of sentences (documents) containing the word))

	It is important to mention that to mitigate the effect of very rare and very common words on the corpus, the log of the IDF value can be calculated before multiplying it with the TF-IDF value.

	"""
	import math
	word_idf_values = {}
	total_num_sent = len(text)
	tokenize_word_list = term_freq(text).keys()
	doc_containing_word = 0
	for token in tokenize_word_list:
		for sentence in text:
			if token in sentence.split(' '):
				doc_containing_word +=1
		word_idf_values[token] = math.log((total_num_sent)/(1 + doc_containing_word))

	return word_idf_values
	