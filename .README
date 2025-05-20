
# Automatic Text Summarization from URLs (Google Colab)


## Features

* 📥 Accepts any article or Wikipedia URL
* 🧠 Uses frequency-based extractive summarization
* ⏱️ Runs directly in Google Colab (no Flask/Streamlit needed)
* 📃 Outputs a clean, human-readable summary


## Getting Started

1. Open the notebook in **Google Colab**
2. Paste the following code in a new cell:

```python
# Download dependencies
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Import libraries
import bs4 as bs
import urllib.request as url
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import heapq

# Summarization Function
def summarize_url(link):
    try:
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

        word_frequencies = {}
        for word in word_tokenize(formatted_text.lower()):
            if word not in stop_words and word not in punctuation:
                word_frequencies[word] = word_frequencies.get(word, 0) + 1

        max_freq = max(word_frequencies.values())
        for word in word_frequencies:
            word_frequencies[word] /= max_freq

        sentence_scores = {}
        for sent in sentence_list:
            for word in word_tokenize(sent.lower()):
                if word in word_frequencies and len(sent.split(' ')) < 30:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
url_input = "https://en.wikipedia.org/wiki/Financial Markets"
print(summarize_url(url_input))
```

---

## 📊 Example Output

> For long term finance, they are usually called the capital markets; for short term finance, they are usually called money markets. [1] Within the financial sector, the term "financial markets" is often used to refer just to the markets that are used to raise finances. The capital markets may also be divided into primary markets and secondary markets. Money markets allow firms to borrow funds on a short-term basis, while capital markets allow corporations to gain long-term funding to support expansion (known as maturity transformation). A financial market is a market in which people trade financial securities and derivatives at low transaction costs. The term "market" is sometimes used for what are more strictly exchanges, organizations that facilitate the trade in financial securities, e.g., a stock exchange or commodity exchange. Secondary market is the market where the second hand securities are sold (security Commodity Markets).

## 🛠 Requirements

* Python (works in Google Colab)
* `nltk`
* `bs4`
* `urllib`

All dependencies are pre-installed in Colab or easily added with `pip`.

---

## 📜 License

This project is for educational and research purposes only.

