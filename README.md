# Word-Density-Analysis

Execution Instructions:

##Step1:
Install virtual environment(Recommended)
install requirement.txt in the local directory
pip3 install -r requirements.txt

##Step2:
I used a Spacy parser which is better than Natural Language Tool Kit(NLTK) so we have to download en model for spacy
python -m spacy download en

##Step3:
execute python code with below command
python3  main.py


##Modules Used and Purpose:
urllib - used to open the URL
BeautifulSoup4 - Used to extract the data from HTML(Source Page)
Used NLTK to remove stopwords, WordNetLemmatizer used to make words appropriate
Spacy Parser: Extract Noun Phrases in the sentences
re: regular expression

##Working

1. Initially, urllib used to open the URL
2. BeautifulSoup4 used to extract web page data from the HTML(Source Page).
   After analyzing the source page content, I followed below approach to clean out all the clutter
    (i) I found a lot of Data which is irrelevant to this project, Hence I decided to ignore few tags in the soup which are "script", "style", "option", "input", "img"
    (ii) After ignoring the tags, there were still blank lines in between so removed all blank lines
    (iii) I also observed there are few special symbols, which are unnecessary for our analysis hence, replaced with an empty string using a regular expression
3. Spacy Parse is the best way to analyze between the words. It is a syntactic dependency parser which is fast and accurate to detect the features. Iterated the parser over the all the sentences in the document to detect noun phrases
4. Used NLTK to remove stop words in between the words
5. Used WordNetLemmatizer to make words appropriate
6. Stored the noun phrases and its count(Number of times it appears in the document) in the dictionary
7. return the top few noun phrases which best describe the document

##Challenges Faced:
Handling the busy page
Detect Noun Phrases from spacy features which best describe the page

#Future Word:
I would like to develop an application like IBM Watson to detect sentiment of the page, Concepts of page



Notes:
IBM Watson Method: I suggest to look at this one
Another way to detect the noun phrases which best describe the document
https://natural-language-understanding-demo.ng.bluemix.net/#url
Open above URL and enter the web URL in URL tab and click Analyze
we can see sentiment, concepts and many other details of the page

