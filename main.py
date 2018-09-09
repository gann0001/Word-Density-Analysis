import re
import nltk
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import spacy
import urllib
import urllib.request
from bs4 import BeautifulSoup as BS
import en_core_web_sm
nlp = en_core_web_sm.load()

def Crawly(url):
    html = urllib.request.urlopen(url).read()
    soup = BS(html, "html.parser")
    for script in soup(["script", "style", "option", "input", "img"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    lines = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(line for line in lines if line)
    return text


def validate_url(url):
    if 'http' in url or 'www' in url:
        return True
    else:
        return False


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

def lematize(parse_list):
    new_list = []
    lmtzr = WordNetLemmatizer()
    for word in parse_list:
        new_list.append(lmtzr.lemmatize(word))
    return new_list




def main():
    input_url = input("Enter the URL which you would like to analyze:")
    # web_text = Crawly('http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster')
    # web_text = Crawly('http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/')
    # web_text = Crawly('http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/')

    input_url += '/'
    check_url = validate_url(input_url)
    if check_url:
        web_text = Crawly(input_url)
        web_text = re.sub('[!@#$():]', ' ', web_text)
        nlp = spacy.load('en_core_web_sm')
        parse_list = []
        for sent in sent_tokenize(web_text):
            doc = nlp(sent)
            for chunk in doc.noun_chunks:
                parse_list.append(chunk.text)

        # Removal of stopwords
        updated_parse = remove_stopwords(parse_list)
        print(len(updated_parse))

        # Lematization
        updated_parse_new = lematize(updated_parse)
        print(len(updated_parse_new))

        dic = {}
        for word in updated_parse_new:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        # print(dic)

        counter_dic = nltk.Counter(dic)
        # print(counter_dic.most_common())

        for k, v in counter_dic.most_common(10):
            print(k)
    else:
        print('Entered URL is not valid, please enter URL again')
        main()










main()



#Validate URL
# try catch blocks for all the methods
#print 20 if wordcount is more than uniq words
#read me
