import re
import nltk
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import spacy
import urllib
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS
import en_core_web_sm
nlp = en_core_web_sm.load()

#crawl the data from web
def crawl_web(url):
    req = Request(url)
    html = urlopen(req).read()
    soup = BS(html, "html.parser")
    for script in soup(["script", "style", "option", "input", "img"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    lines = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(line for line in lines if line)
    return text


#validate URL
def validate_url(url):
    if 'http' in url or 'www' in url:
        return True
    else:
        return False


#remove stopwords
def remove_stopwords(parse_list):
    new_list = []
    try:
        stop_words = stopwords.words('english')
        for word in parse_list:
            if word in stop_words or len(word) <= 3:
                pass
            else:
                new_list.append(word)
    except UnicodeEncodeError:
        return False

    return new_list


#stem the words
def lematize(parse_list):
    new_list = []
    lmtzer = WordNetLemmatizer()
    for word in parse_list:
        new_list.append(lmtzer.lemmatize(word))
    return new_list


def main():
    input_url = input("Enter the URL which you would like to analyze:")
    input_url += '/'
    check_url = validate_url(input_url)
    if check_url:
        web_text = crawl_web(input_url)
        web_text = re.sub('[!@#$():]', ' ', web_text)
        nlp = spacy.load('en_core_web_sm')
        parse_list = []
        for sent in sent_tokenize(web_text):
            doc = nlp(sent)
            for chunk in doc.noun_chunks:
                parse_list.append(chunk.text)

        # Removal of stopwords
        updated_parse = remove_stopwords(parse_list)

        # Lematization
        updated_parse_new = lematize(updated_parse)

        dic = {}
        for word in updated_parse_new:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1

        counter_dic = nltk.Counter(dic)
        # print(counter_dic.most_common())
        if len(counter_dic) < 500:
            for k, v in counter_dic.most_common(10):
                print(k)
        elif len(counter_dic)>500 and len(counter_dic)<750:
            for k, v in counter_dic.most_common(15):
                print(k)
        else:
            for k, v in counter_dic.most_common(20):
                print(k)
    else:
        print('Entered URL is not valid, please enter URL again')
        main()


if __name__ == '__main__':
    main()
