from neattext import __version__
from neattext import TextCleaner,TextExtractor,TextMetrics
from neattext.neattext import clean_text,remove_emails,extract_emails,replace_emails,replace_urls


def test_version():
    assert __version__ == '0.0.2'

def test_remove_emails():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_emails()
	assert result == 'This is the mail  ,our WEBSITE is https://example.com 😊.'


def test_extract_emails():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_emails()
	assert result == ['example@gmail.com']

def test_remove_emojis():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_emojis()
	assert result == 'This is the mail example@gmail.com ,our WEBSITE is https://example.com .'

def test_extract_emojis():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_emojis()
	assert result == ['😊']


def test_remove_urls():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_urls()
	assert result == 'This is the mail example@gmail.com ,our WEBSITE is  😊.'


def test_extract_urls():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_urls()
	assert result == ['https://example.com']

def test_remove_stopwords():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_stopwords()
	assert result == 'This mail example@gmail.com ,our WEBSITE https://example.com 😊.'


def test_extract_stopwords():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_stopwords()
	assert result == ['is', 'the', 'is']

def test_single_fxn_remove_emails():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = remove_emails(t1)
	assert result == 'This is the mail  ,our WEBSITE is https://example.com 😊.'


def test_single_fxn_extract_emails():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = extract_emails(t1)
	assert result == ['example@gmail.com']

def test_single_fxn_clean_text():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com ."
	result = clean_text(t1,True)
	assert result == 'this is the mail <email> ,our website is <url> .'

def test_single_fxn_clean_text_false():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = clean_text(t1,False)
	assert result == 'this is the mail  our website is  '

def test_single_fxn_replace_emails():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = replace_emails(t1)
	assert result == 'This is the mail <EMAIL> ,our WEBSITE is https://example.com 😊.'

def test_single_fxn_replace_urls():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = replace_urls(t1)
	assert result == 'This is the mail example@gmail.com ,our WEBSITE is <URL> 😊.'

	



