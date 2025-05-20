import bs4 as bs
import urllib.request as url
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import heapq
from string import punctuation

scraped_data = url.urlopen('https://en.wikipedia.org/wiki/Financial_market')
article = scraped_data.read()
parsed_article = bs.BeautifulSoup(article,'lxml')
paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text

article_text

article_text = re.sub(r' [0-9]*', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

# remove special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

# @title Tokenize Sentences
sentence_list = nltk.sent_tokenize(article_text)

#@title Find Weighted Frequency of Occurence
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}

for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords and word not in punctuation:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
word_frequencies

#@title Frequency Distribution
frequency_dist = nltk.FreqDist(word_frequencies)
frequency_dist.plot(30)

#@title Calculate Sentence Scores
sentence_scores = {}

for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
sentence_scores

#@title Extract Output Summary
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)
summary

# Install dependencies
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Import required libraries
import bs4 as bs
import urllib.request as url
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from string import punctuation
import heapq

# Summarization function
def summarize_url(link):
    try:
        # Fetch and parse article
        scraped_data = url.urlopen(link)
        article = scraped_data.read()
        parsed_article = bs.BeautifulSoup(article, 'lxml')
        paragraphs = parsed_article.find_all('p')

        article_text = " ".join([p.text for p in paragraphs])
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)

        formatted_text = re.sub('[^a-zA-Z]', ' ', article_text)
        formatted_text = re.sub(r'\s+', ' ', formatted_text)

        sentence_list = sent_tokenize(article_text)
        stop_words = set(stopwords.words('english'))

        # Word frequencies
        word_frequencies = {}
        for word in word_tokenize(formatted_text.lower()):
            if word not in stop_words and word not in punctuation:
                word_frequencies[word] = word_frequencies.get(word, 0) + 1

        max_freq = max(word_frequencies.values())
        for word in word_frequencies:
            word_frequencies[word] /= max_freq

        # Sentence scoring
        sentence_scores = {}
        for sent in sentence_list:
            for word in word_tokenize(sent.lower()):
                if word in word_frequencies and len(sent.split()) < 30:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

        # Get top sentences
        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary

    except Exception as e:
        return f"Error: {e}"

# Example: Paste your URL here
url_input = input("Paste a URL to summarize: ")
print("\nGenerating summary...\n")
print(summarize_url(url_input))
