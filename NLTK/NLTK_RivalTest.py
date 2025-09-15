'''
Created on Mar 7, 2019

@author: Alexey
'''
import requests
from itertools import groupby
import justext
import nltk
from nltk.corpus import stopwords
from nltk.corpus import brown
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('gutenberg')
nltk.download('names')
import urllib.request

number_strong_terms=100
#nltk.download()
#nltk.download('stopwords')
#nltk.download('brown')

class popular_terms: 
    def __init__(self):
        url="https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity/transcript"
        transcript_one = self.extract_transcript(url)
        url="https://www.ted.com/talks/al_gore_on_averting_climate_crisis/transcript"
        transcript_two = self.extract_transcript(url)
        url="https://www.ted.com/talks/david_pogue_says_simplicity_sells/transcript"
        transcript_three = self.extract_transcript(url)
        # Step 2 count the most popular terms extracting stop words
        transcript_one_counted = self.count_words(transcript_one)
        #print("AAA->"+str(transcript_one_counted))
        transcript_two_counted = self.count_words(transcript_two)
        #print("BBB->"+str(transcript_two_counted))
        transcript_three_counted = self.count_words(transcript_three)
        #print("CCC->"+str(transcript_three_counted))
        
        # Step 3 find intersection of the most popular terms
        intersection_one_two = self.term_intersection(transcript_one_counted,transcript_two_counted)
        intersection_two_three = self.term_intersection(transcript_two_counted,transcript_three_counted)
        intersection_one_two_three = self.term_intersection(intersection_one_two,intersection_two_three)
        #print(intersection_one_two_three)
        
        # Step 4 return N the most popular terms from intersection
        #Extract the most popular terms (turn dictionary to array of tuples, sort by values, extract)
        popular_terms = sorted(intersection_one_two_three.items(),key= lambda kv: kv[1],reverse=True)[:number_strong_terms]
        #print(intersection_one_two_three)
        # DICTIONARY->TUPLES
        #print(list(intersection_one_two_three.items()))
        #Sort by terms:
        popular_terms2 = sorted(popular_terms,key= lambda x: x[0])
        #print(popular_terms2)
        for ind,term in enumerate(popular_terms2):
            print(str(ind)+": "+str(term[0])+" "+str(intersection_one_two_three[term[0]]))
            pass
        
    def get_stop_words(self):
        stop_words= set(stopwords.words('english'))
        return stop_words
                
    def extract_transcript(self,url):
        response = requests.get(url)
        #print (response.status_code)
        #print (response.content)
        #print (response.text)
        #print (response.headers)
        paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
        output = ""
        flag=False
        for paragraph in paragraphs:
            #print ("AAAA->"+paragraph.text)
            # Extract paragraphs with the speech
            if "DetailsAbout the talk" in paragraph.text:
                flag=True
            if "Programs & initiatives" in paragraph.text:
                flag=False
            if flag:
                output += paragraph.text
        
        return output
    
    def count_words(self,transcript):
        words = transcript.replace("\n","") \
            .replace("\t","") \
            .replace("."," ") \
            .replace(","," ") \
            .replace("("," ") \
            .replace(")"," ") \
            .replace("-"," ") \
            .replace("?"," ") \
            .replace("!"," ") \
            .replace('"','').lower().split(" ")
        # remove stop words
        terms=[]
        stop_words=self.get_stop_words()
        for w in words:
            if len(w)>0 and not w in stop_words:
                    terms.append(w)
    
        m={}
        for key, group in groupby(sorted(terms)):
            #print ("KEY=="+key) 
            m[key]=len(list(group))
        return m
    
    def term_intersection(self,dict_one, dict_two):
        intersect={}
        for key in dict_one:
            if key in dict_two:
                # we keep the minimal number occurrences of 2 transcripts (conservatively)
                intersect[key]=min(dict_one[key],dict_two[key])
        return intersect
    
class popular_terms2:
    
    def __init__(self):         
        # Step 1 receive the transcript from 3 relevant talks
        url="https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity/transcript"
        print(url)
        print("Extract transcript(text) from html")
        html = self.extract_transcript(url)
        print("process_html_text")
        #transcript_one = self.process_html(html)
        transcript_one = self.process_html_new(html)
        #print("transcript html",transcript_one)
        transcript_one_counted = self.count_words(transcript_one)
        print("transcript: words counted",transcript_one_counted)
    
#     def process_html(self,html):
#         text = nltk.clean_html(html)
#         print(text)
#         exit(0)
#         from bs4 import BeautifulSoup
#         #soup = BeautifulSoup(html,"html5lib")
#         soup = BeautifulSoup(html, "xml")
#         text = soup.get_text(strip=True)
#         return text
    
    def tokenize_sentences(self, text):
        print(">>>>>>>>>>>>>>>>>",nltk.sent_tokenize(text,"english"))
        return nltk.sent_tokenize(text,"english")
        
    def tokenize_words(self, text):
        print(nltk.word_tokenize(text,"english"))
        return nltk.word_tokenize(text,"english")
    
#     def process_html_old(self,html):
#         paragraphs = justext.justext(html, justext.get_stoplist("English"))
#         output = ""
#         flag=False
#         for paragraph in paragraphs:
#             #print ("AAAA->"+paragraph.text)
#             # Extract paragraphs with the speech
#             if "Programs & initiatives" in paragraph.text:
#                 flag=False
#             if flag:
#                 output += paragraph.text
#             if "DetailsAbout the talk" in paragraph.text:
#                 flag=True
#         return output \
#             .replace("."," ") \
#             .replace(","," ") \
#             .replace("?"," ") \
#             .replace("!"," ") \
#             .replace("("," ") \
#             .replace(")"," ") \
#             .replace('"'," ") \
#             .lower()
            
    def process_html_new(self,html):
        paragraphs = justext.justext(html, justext.get_stoplist("English"))
        output = ""
        flag=False
        for paragraph in paragraphs:
            #print ("AAAA->"+paragraph.text)
            # Extract paragraphs with the speech
            if "Programs & initiatives" in paragraph.text:
                flag=False
            if flag:
                output += paragraph.text
            if "DetailsAbout the talk" in paragraph.text:
                flag=True
        sentences = self.tokenize_sentences(output.lower())
        #for ind in sentences:
        #    print(ind+" EOS")
        return output.lower()
        
    def extract_transcript(self,url):
        response = urllib.request.urlopen(url)
        html = response.read()
        return html
    
    def remove_stop_words(self,tokens):
        clean_tokens = tokens[:]
        sw = set(stopwords.words('english'))
        for token in tokens:
            if "'" in token or token in sw:
                clean_tokens.remove(token)
        return clean_tokens

    def count_words(self,transcript):
        #tokens = [t for t in transcript.split()]
        tokens = nltk.word_tokenize(transcript)       
        tokens = self.remove_stop_words(tokens)
        print("Words:",tokens)       
        freq = nltk.FreqDist(tokens)
        print("Words counted:",freq)
        #for key,val in freq.items():
        #    print (str(key) + ':' + str(val))
        #freq.plot(50, cumulative=False)
        return {x:freq[x]  for x in freq} 
    
    def synonyms_antonyms(self):
        print("synonyms_antonyms") 
        from nltk.corpus import wordnet
        synonyms = []
        for syn in wordnet.synsets('Computer'):
            for lemma in syn.lemmas():   
                synonyms.append(lemma.name())
        print("synonym to 'computer': "+str(synonyms))
        antonyms = []
 
        for syn in wordnet.synsets("small"):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        print("antonym to 'small': "+str(set(antonyms)))
        antonyms = []
        for syn in wordnet.synsets("computer"):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        print("antonym to 'computer': "+str(antonyms))
        return antonyms
    
    def stems_lemmas(self):
        print("Stems","Lemmas")
        from nltk.stem import PorterStemmer
        stemmer = PorterStemmer()    
        print("Stem of 'working': "+str(stemmer.stem('working')))
        from nltk.stem import WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()
        print("Lemma of 'increases': "+str(lemmatizer.lemmatize('increases')))
        
    def concordance(self):
        print("Concordance",nltk.corpus.gutenberg.fileids())
        # Get strings with 'surprize' in the text
        from nltk.text import Text 
        emma = Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
        print("Emma:",emma)
        frag = emma.concordance_list("surprize")
        print('fragments with "query"(surprize)',frag)
        for ind in frag:
            #print("Fragments:",ind)
            left = ind.left
            query = ind.query
            right = ind.right
            #for indd in left:
            #    print("left:",indd)
            #print("query",query)
            #for indd in right:
            #    print("right:",indd)
        print("end of 'concordance'")
        
    #https://www.guru99.com/pos-tagging-chunking-nltk.html
    def sentence_tokenize(self):
        text = "God is Great! I won a lottery. I believe that I am tired. My spine hurts. my hands are sore. I said: 'Go to hell.'"
        print(nltk.sent_tokenize(text))
    
    def word_tokenize(self):
        text = "God is Great! I won a lottery. I believe that I am tired. My spine hurts. my hands are sore. I said: 'Go to hell.'"
        print(nltk.word_tokenize(text))
        
    def stemming_lemmarization(self):
        from nltk.stem import WordNetLemmatizer
        from nltk.stem import PorterStemmer
        stemmer = PorterStemmer()
        lemmatizer = WordNetLemmatizer()
        print(stemmer.stem('stones'))
        print(stemmer.stem('speaking'))
        print(stemmer.stem('bedroom'))        
        print(stemmer.stem('jokes'))
        print(stemmer.stem('lisa'))
        print(stemmer.stem('purple'))
        print('----------------------')
        print(lemmatizer.lemmatize('stones'))
        print(lemmatizer.lemmatize('speaking'))
        print(lemmatizer.lemmatize('bedroom'))
        print(lemmatizer.lemmatize('jokes'))
        print(lemmatizer.lemmatize('lisa'))
        print(lemmatizer.lemmatize('purple'))
        
class prediction_male_female:
    
    def print_naive_model(self, featuresets,key1,key2):
        #for ind in featuresets:
        #    print("trainng",ind)
        a = [(x[1],x[0]['last_letter_222_222']) for x in featuresets]
        b = {}
        for ind in a:
            key = ind[0]
            val = ind[1]

            if key in b:
                #print(b[key])
                c = b[key]
                c.append(val)
                b[key]=c
            else:
                b[key]=[val]

        from itertools import groupby 
        d1 = sorted(b[key1])
        #print("d1=",d1)
        male = [list(group) for key,group in groupby(d1)]
        male2 = {group[0]:len(group) for group in male}
        print(key1,male2)
        d1 = sorted(b[key2])
        #print("d1=",d1)
        male = [list(group) for key,group in groupby(d1)]
        male2 = {group[0]:len(group) for group in male}
        print(key2,male2)
        
    def gender_features(self,word): 
        #print('last_letter_222_222', word, word[-2:])
        return {'last_letter_222_222': word[-1:]} 
        
    def prediction(self):
        import nltk.classify.util
        from nltk.classify import NaiveBayesClassifier
        from nltk.corpus import names
         
        # Load data and training 
        names = ([(name, 'male') for name in names.words('male.txt')] + 
             [(name, 'female') for name in names.words('female.txt')])
         
        featuresets = [(self.gender_features(n), g) for (n,g) in names] 
        self.print_naive_model(featuresets,"male","female")
        train_set = featuresets
        classifier = nltk.NaiveBayesClassifier.train(train_set) 
         
        # Predict
        name="ssssser"
        print("predict",classifier.classify(self.gender_features(name)))
        
    def prediction2(self):
        import nltk.classify.util
        from nltk.classify import NaiveBayesClassifier
        from nltk.corpus import names
         
        # Load data and training 
        #names = ([(name, 'male') for name in names.words('male.txt')] + 
        #     [(name, 'female') for name in names.words('female.txt')])
        names = [("blood","red"),("army","red"),("hat","red"),("partizan","red"),("kazak","red"),("her","red")]
        names += names
        names += names
        names2 = [("body","white"),("pudel","white"),("mushroom","white"),("snow","white"),("river","white"),("goryachka","white"),("cord","white")]
        names = names+names2
         
        featuresets = [(self.gender_features(n), g) for (n,g) in names] 
        self.print_naive_model(featuresets,"red","white")
        train_set = featuresets
        classifier = nltk.NaiveBayesClassifier.train(train_set) 
         
        # Predict
        name="clear"
        print("predict",classifier.classify(self.gender_features(name)))
        
class classifier:
    import nltk.classify.util
    from nltk.classify import NaiveBayesClassifier
    from nltk.corpus import names
     
    def word_feats(self,words):
        print("words",words)
        print(dict([(word, True) for word in words]))
        return dict([(word, True) for word in words])
    
    def classify(self):
     
        positive_vocab = [ 'awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)' ]
        negative_vocab = [ 'bad', 'terrible','useless', 'hate', ':(' ]
        neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not' ]
         
        positive_features = [(self.word_feats(pos), 'pos') for pos in positive_vocab]
        negative_features = [(self.word_feats(neg), 'neg') for neg in negative_vocab]
        neutral_features = [(self.word_feats(neu), 'neu') for neu in neutral_vocab]
         
        train_set = negative_features + positive_features + neutral_features
        print("TRAIN",train_set)
         
        classifier = nltk.NaiveBayesClassifier.train(train_set) 
         
        # Predict
        neg = 0
        pos = 0
        neu= 0
        #sentence = "Awesome movie, I liked it"
        sentence = "Movie is good, sound quality bad"
        #sentence = "Fantastic movie"
        #sentence = "I look at you"
        sentence = sentence.lower()
        print("claasify:", sentence)
        words = sentence.split(' ')
        for word in words:
            classResult = classifier.classify( self.word_feats(word))
            if classResult == 'neg':
                neg = neg + 1
                print("neg",neg,word)
            if classResult == 'neu':
                neu = neu + 1
                print("neu",neu,word)
            if classResult == 'pos':
                pos = pos + 1
                print("pos",pos,word)
        print("neg=",neg,"neu=",neu,"pos=",pos)
        print('Positive: ' + str(float(pos)/len(words)))
        print('Negative: ' + str(float(neg)/len(words)))
        
if __name__ == '__main__':
    method1 = popular_terms()
    print("NLTK Start")
    method2 = popular_terms2()
    print("synonyms_antonyms")
    method2.synonyms_antonyms()
    print("stems_lemmas")
    method2.stems_lemmas()
    method2.stemming_lemmarization()
    print("concordabce - search for the word surrounded with left and right words")
    method2.concordance()
    print("tokenization - sentences, words")
    method2.sentence_tokenize()
    method2.word_tokenize()
    print("Prediction male female")
    prediction = prediction_male_female()
    prediction.prediction()
    prediction.prediction2()
    print("classifier")
    classifier = classifier()
    classifier.classify()
    exit(0)
    
    pass