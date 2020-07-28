# neattext
NeatText:a simple NLP package for cleaning textual data and text preprocessing

[![Build Status](https://travis-ci.org/Jcharis/neattext.svg?branch=master)](https://travis-ci.org/Jcharis/neattext)

[![GitHub license](https://img.shields.io/github/license/Jcharis/neattext)](https://github.com/Jcharis/neattext/blob/master/LICENSE)

#### Problem
+ Cleaning of unstructured text data
+ Reduce noise [special characters,stopwords]
+ Reducing repetition of using the same code for text preprocessing

#### Solution
+ convert the already known solution for cleaning text into a reuseable package


#### Installation
```bash
pip install neattext
```

### Usage
+ The OOP Way(Object Oriented Way)
+ NeatText offers 4 main classes for working with text data
	- TextFrame : a frame-like object for cleaning text
	- TextCleaner: remove or replace specifics
	- TextExtractor: extract unwanted text data
	- TextMetrics: word stats and metrics


### Using TextFrame
+ Keeps the text as `TextFrame` object. This allows us to do more with our text. 
+ It inherits the benefits of the TextCleaner and the TextMetrics out of the box with some additional features for handling text data.
+ This is the simplest way for text preprocessing with this library alternatively you can utilize the other classes too.


```python
>>> import neattext as nt 
>> mytext = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> docx = nt.TextFrame(text=mytext)
>>> docx.text 
"This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>>
>>> docx.describe()
Key      Value          
Length  : 73             
vowels  : 21             
consonants: 34             
stopwords: 4              
punctuations: 8              
special_char: 8              
tokens(whitespace): 10             
tokens(words): 14             
>>> 
>>> docx.length
73
>>> # Scan Percentage of Noise(Unclean data) in text
>>> d.noise_scan()
{'text_noise': 19.17808219178082, 'text_length': 73, 'noise_count': 14}
>>> 
>>> docs.head(16)
'This is the mail'
>>> docx.tail()
>>> docx.count_vowels()
>>> docx.count_stopwords()
>>> docx.count_consonants()
>>> docx.nlongest()
>>> docx.nshortest()
```
#### Basic NLP Task (Tokenization,Ngram,Text Generation)
```python
>>> docx.word_tokens()
>>>
>>> docx.sent_tokens()
>>>
>>> docx.term_freq()
>>>
>>> docx.bow()
```
#### Basic Text Preprocessing
```python
>>> docx.normalize()
'this is the mail example@gmail.com ,our website is https://example.com 😊.'
>>> docx.normalize(level='deep')
'this is the mail examplegmailcom our website is httpsexamplecom '

>>> docx.remove_puncts()
>>> docx.remove_html_tags()
>>> docx.remove_special_characters()
>>> docx.remove_emojis()
>>> docx.fix_contractions()
```

##### Handling Files with NeatText
+ Read txt file directly into TextFrame
```python
>>> import neattext as nt 
>>> docx_df = nt.read_txt('file.txt')
```
+ Alternatively you can instantiate a TextFrame and read a text file into it
```python
>>> import neattext as nt 
>>> docx_df = nt.TextFrame().read_txt('file.txt')
```

##### Chaining Methods on TextFrame
```python
>>> t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
>>> docx = TextFrame(t1)
>>> result = docx.remove_emails().remove_urls().remove_emojis()
>>> print(result)
'This is the mail  ,our WEBSITE is   and it will cost $100 to subscribe.'
```



#### Clean Text
+ Clean text by removing emails,numbers,stopwords,emojis,etc
```python
>>> from neattext import TextCleaner
>>> docx = TextCleaner()
>>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> docx.clean_text()
```

#### Remove Emails,Numbers,Phone Numbers 
```python
>>> print(docx.remove_emails())
>>> 'This is the mail  ,our WEBSITE is https://example.com 😊.'
>>>
>>> print(docx.remove_stopwords())
>>> 'This mail example@gmail.com ,our WEBSITE https://example.com 😊.'
>>>
>>> print(docx.remove_numbers())
>>> docx.remove_phone_numbers()
```


#### Remove Special Characters
```python
>>> docx.remove_special_characters()
```

#### Remove Emojis
```python
>>> print(docx.remove_emojis())
>>> 'This is the mail example@gmail.com ,our WEBSITE is https://example.com .'
```

#### Replace Emails,Numbers,Phone Numbers
```python
>>> docx.replace_emails()
>>> docx.replace_numbers()
>>> docx.replace_phone_numbers()
```

#### Chain Multiple Methods
```python
>>> t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
>>> docx = TextCleaner(t1)
>>> result = docx.remove_emails().remove_urls().remove_emojis()
>>> print(result)
'This is the mail  ,our WEBSITE is   and it will cost $100 to subscribe.'

```

### Using TextExtractor
+ To Extract emails,phone numbers,numbers,urls,emojis from text
```python
>>> from neattext import TextExtractor
>>> docx = TextExtractor()
>>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> docx.extract_emails()
>>> ['example@gmail.com']
>>>
>>> docx.extract_emojis()
>>> ['😊']
```


### Using TextMetrics
+ To Find the Words Stats such as counts of vowels,consonants,stopwords,word-stats
```python
>>> from neattext import TextMetrics
>>> docx = TextMetrics()
>>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> docx.count_vowels()
>>> docx.count_consonants()
>>> docx.count_stopwords()
>>> docx.word_stats()
```

### Usage 
+ The MOP(method/function oriented way) Way

```python
>>> from neattext.functions import clean_text,extract_emails
>>> t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com ."
>>> clean_text(t1,True)
>>>'this is the mail <email> ,our website is <url> .'
>>> extract_emails(t1)
>>> ['example@gmail.com']
```

### Explainer
+ Explain an emoji or unicode for emoji 
	- emoji_explainer()
	- emojify()
	- unicode_2_emoji()


```python
>>> from neattext.explainer import emojify
>>> emojify('Smiley')
>>> '😃'
```

```python
>>> from neattext.explainer import emoji_explainer
>>> emoji_explainer('😃')
>>> 'SMILING FACE WITH OPEN MOUTH'
```

```python
>>> from neattext.explainer import unicode_2_emoji
>>> unicode_2_emoji('0x1f49b')
	'FLUSHED FACE'
```



### Documentation
Please read the [documentation](https://github.com/Jcharis/neattext/wiki) for more information on what neattext does and how to use is for your needs.

### More Features To Add
+ basic nlp task
+ currency normalizer

#### Acknowledgements
+ Inspired by packages like `clean-text` from Johannes Fillter and `textify` by JCharisTech


#### NB
+ Contributions Are Welcomed
+ Notice a bug, please let us know.
+ Thanks A lot


#### By
+ Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech



