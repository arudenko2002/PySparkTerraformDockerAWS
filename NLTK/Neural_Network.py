'''
Created on Mar 25, 2020

@author: Alexey
'''
class tutorial:
    def refs(self):
        nested = [[]] * 3
        nested[1].append('Python')
        nested[1] = ['Monty']
        print(nested)
        
    def is_polindrome(self,strr):
        #str2=''.join(reversed(strr))
        #print(str(str2))
        #return str2==''.join(strr)

        j=len(strr)//2
        for i,v in enumerate(strr):    
            if j==i:
                return True
            if v != strr[len(strr)-i-1]:
                return False
       
        return True
    
    ######################################
    # POS TAG List
    # CC coordinating conjunction
    # CD cardinal digit
    # DT determiner
    # EX existential there (like: "there is" ... think of it like "there exists")
    # FW foreign word
    # IN preposition/subordinating conjunction
    # JJ adjective 'big'
    # JJR adjective, comparative 'bigger'
    # JJS adjective, superlative 'biggest'
    # LS list marker 1)
    # MD modal could, will
    # NN noun, singular 'desk'
    # NNS noun plural 'desks'
    # NNP proper noun, singular 'Harrison'
    # NNPS proper noun, plural 'Americans'
    # PDT predeterminer 'all the kids'
    # POS possessive ending parent's
    # PRP personal pronoun I, he, she
    # PRP$ possessive pronoun my, his, hers
    # RB adverb very, silently,
    # RBR adverb, comparative better
    # RBS adverb, superlative best
    # RP particle give up
    # TO to go 'to' the store.
    # UH interjection errrrrrrrm
    # VB verb, base form take
    # VBD verb, past tense took
    # VBG verb, gerund/present participle taking
    # VBN verb, past participle taken
    # VBP verb, sing. present, non-3d take
    # VBZ verb, 3rd person sing. present takes
    # WDT wh-determiner which
    # WP wh-pronoun who, what
    # WP$ possessive wh-pronoun whose
    # WRB wh-abverb where, when
    ############################################
    def pos_tagging_sentence(self):
        import nltk
        text = "Hello Guru99, You have to build a very good site, and I love visiting your site."
        sentence = nltk.sent_tokenize(text)
        for sent in sentence:
            print(sent)
            p = nltk.pos_tag(nltk.word_tokenize(sent))
            for ind in p:
                print(ind)
                
    #Bigrams, Trigrams            
    def bi_tri_grams(self):
        import nltk
        text = "Guru99 is a totally new kind of learning experience."
        Tokens = nltk.word_tokenize(text)
        output = list(nltk.bigrams(Tokens))
        print("bigrams=",output)
        output = list(nltk.trigrams(Tokens))
        print("trigrams=",output)

class Word_Embedding:
    def Vectorize_words(self):
        from sklearn.feature_extraction.text import CountVectorizer
        vectorizer=CountVectorizer()
        data_corpus=["guru99 is the best site for online tutorials. I love to visit guru99 and zoo."]
        vocabulary=vectorizer.fit(data_corpus)
        print("vocabulary=",vocabulary)
        X= vectorizer.transform(data_corpus)
        print("vectorizer=",X.toarray())
        print("feature_names=",vocabulary.get_feature_names())
        
class Word2vec:
    def model(self):
        import nltk
        import gensim
        from nltk.corpus import abc
        print("Word2sec Model")
        model= gensim.models.Word2Vec(abc.sents())
        print("abc=",len(abc.sents()))
        print("model",model)
        X= list(model.wv.vocab)
        print("mode vocab=",len(X))
        term='writing'
        data=model.most_similar(term)
        for dat in data:
            print("data:",term,dat)
    def data(self):
        a = [{"tag": "welcome",
            "patterns": ["Hi", "How are you", "Is any one to talk?", "Hello", "hi are you available"],
            "responses": ["Hello, thanks for contacting us", "Good to see you here"," Hi there, how may I assist you?"]},
            {"tag": "goodbye",
            "patterns": ["Bye", "See you later", "Goodbye", "I will come back soon"],
            "responses": ["See you later, thanks for visiting", "have a great day ahead", "Wish you Come back again soon."]},
            {"tag": "thankful",
            "patterns": ["Thanks for helping me", "Thank your guidance", "That's helpful and kind from you"],
            "responses": ["Happy to help!", "Any time!", "My pleasure", "It is my duty to help you"]},
                    {"tag": "hoursopening",
            "patterns": ["What hours are you open?", "Tell your opening time?", "When are you open?", "Just your timing please"],
            "responses": ["We're open every day 8am-7pm", "Our office hours are 8am-7pm every day", "We open office at 8 am and close at 7 pm"]},
            {"tag": "payments",
            "patterns": ["Can I pay using credit card?", " Can I pay using Mastercard?", " Can I pay using cash only?" ],
            "responses": ["We accept VISA, Mastercard and credit card", "We accept credit card, debit cards and cash. Please don't worry"]}]
        return a
    
    def process(self):
        #list of libraries used by the code
        import string
        from gensim.models import Word2Vec
        import logging
        from nltk.corpus import stopwords
        #from textblob import Word
        import json
        import pandas as pd
        ###########My patch for Word
        from nltk.stem import WordNetLemmatizer
        from nltk.stem import PorterStemmer
        stemmer = PorterStemmer()
        lemmatizer = WordNetLemmatizer()
        
        #data in json format
        json_file = 'intents.json'
        #with open('intents.json','r') as f:
        #    data = json.load(f)
        data = self.data()
        #displaying the list of stopwords
        stop = stopwords.words('english')
        #dataframe
        df = pd.DataFrame(data)
        
        df['patterns'] = df['patterns'].apply(', '.join)
        # print(df['patterns'])
        #print(df['patterns'])
        #cleaning the data using the NLP approach
        print(df)
        df['patterns'] = df['patterns'].apply(lambda x:' '.join(x.lower() for x in x.split()))
        df['patterns']= df['patterns'].apply(lambda x: ' '.join(x for x in x.split() if x not in string.punctuation))
        df['patterns']= df['patterns'].str.replace('[^\w\s]','')
        df['patterns']= df['patterns'].apply(lambda x: ' '.join(x for x in x.split() if  not x.isdigit()))
        df['patterns'] = df['patterns'].apply(lambda x:' '.join(x for x in x.split() if not x in stop))
        df['patterns'] = df['patterns'].apply(lambda x: " ".join([lemmatizer.lemmatize(word) for word in x.split()]))
        #taking the outer list
        bigger_list=[]
        for i in df['patterns']:
            li = list(i.split(" "))
            bigger_list.append(li)
        #structure of data to be taken by the model.word2vec
        print("Data format for the overall list:",bigger_list)
        #custom data is fed to machine for further processing
        model = Word2Vec(bigger_list, min_count=1,size=300,workers=4)
        #print(model)
        #save model
        print("saved model")
        model.save("word2vec.model")
        model.save("model.bin")
        #read model
        print("read model")
        model = Word2Vec.load('model.bin')
        #check vocabilary ion the model
        vocab = list(model.wv.vocab)
        print("Vocabilary=", vocab)
        #use model
        similar_words = model.most_similar('thanks')    
        print("similar words=",similar_words)
        dissimilar='See you later thanks for visiting'.split()
        print("dissimilar",dissimilar)
        # my module keyedvectors.py uses non-sequence iterables such as generators (deprecated)
        dissimilar_words = model.doesnt_match(dissimilar)
        print("dissimlar_words",dissimilar_words)
        #similarity between 2 words
        similarity_two_words = model.similarity('please','see')
        print("Please provide the similarity between these two words:")
        print("similarity_two_words",similarity_two_words)
        #  Find similar
        similar = model.similar_by_word('kind')
        print("similar=",similar)
        
class neural_network:
    def training_data(self):
        a={"intents": [
        {"tag": "greeting",
         "patterns": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"],
         "responses": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"],
         "context_set": ""
        },
        {"tag": "goodbye",
         "patterns": ["Bye", "See you later", "Goodbye"],
         "responses": ["See you later, thanks for visiting", "Have a nice day", "Bye! Come back again soon."]
        },
        {"tag": "thanks",
         "patterns": ["Thanks", "Thank you", "That's helpful"],
         "responses": ["Happy to help!", "Any time!", "My pleasure"]
        },
        {"tag": "hours",
         "patterns": ["What hours are you open?", "What are your hours?", "When are you open?" ],
         "responses": ["We're open every day 9am-9pm", "Our hours are 9am-9pm every day"]
        },
        {"tag": "payments",
         "patterns": ["Do you take credit cards?", "Do you accept Mastercard?", "Are you cash only?" ],
         "responses": ["We accept VISA, Mastercard and AMEX", "We accept most major credit cards"]
        },
        {"tag": "opentoday",
         "patterns": ["Are you open today?", "When do you open today?", "What are your hours today?"],
         "responses": ["We're open every day from 9am-9pm", "Our hours are 9am-9pm every day"]
        }
        ]}
        return a
    
    def build_training_output(self):
        import nltk
        from nltk import stem
        from nltk.stem.lancaster import LancasterStemmer
        stemmer = LancasterStemmer()
        import numpy
        #import tflearn
        import tensorflow
        import random
        import json
        import pickle

        #import json
        #with open('intents.json') as file:
        #    data = json.load(file)
        data=self.training_data()
        
        try:
            with open("data.pickle", "rb") as f:
                words, labels, training, output = pickle.load(f)
        except:
            words = []
            labels = []
            docs_x = []
            docs_y = []
        
            for intent in data["intents"]:
                for pattern in intent["patterns"]:
                    wrds = nltk.word_tokenize(pattern)
                    words.extend(wrds)
                    docs_x.append(wrds)
                    docs_y.append(intent["tag"])
        
                if intent["tag"] not in labels:
                    labels.append(intent["tag"])
        
                words = [stemmer.stem(w.lower()) for w in words if w != "?"]
                words = sorted(list(set(words)))
            
                labels = sorted(labels)
            
                training = []
                output = []
            
                out_empty = [0 for _ in range(len(labels))]
            
                for x, doc in enumerate(docs_x):
                    bag = []
            
                    wrds = [stemmer.stem(w.lower()) for w in doc]
            
                    for w in words:
                        if w in wrds:
                            bag.append(1)
                        else:
                            bag.append(0)
            
                    output_row = out_empty[:]
                    output_row[labels.index(docs_y[x])] = 1
            
                    training.append(bag)
                    output.append(output_row)
            
            
                training = numpy.array(training)
                output = numpy.array(output)
            
                with open("data.pickle", "wb") as f:
                    pickle.dump((words, labels, training, output), f)
        
        return (training, output, words, labels, data)

    def model_builder(self, training, output):
        import tflearn
        import tensorflow as tf
        tf.compat.v1.reset_default_graph()
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)
        model = tflearn.DNN(net)
        try:
            #1/0 #error to caluclate the model and save it
            print("model loading")
            model.load("model.tflearn")
        except:
            print("model calculation and saving")
            model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
            model.save("model.tflearn")
        return model
    
    def build_model_save(self):
        (training,output, words, labels, data) = self.build_training_output()
        model = self.model_builder(training, output)
        return (model, words, labels, data)
        
    def bag_of_words(self,s, words):
        import nltk
        import numpy
        nltk.download('punkt_tab')
        import random
        from nltk.stem import PorterStemmer
        
        stemmer = PorterStemmer()  
        bag = [0 for _ in range(len(words))]
    
        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]
    
        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1
        #print("bag=",bag,len(words))
        #print(words)        
        return numpy.array(bag)
    
    def chat(self,model,words, labels, data):
        import numpy
        import random
        print("Start talking with the bot (type quit to stop)!")
        while True:
            inp = input("You: ")
            if inp.lower() == "quit":
                break
    
            results = model.predict([self.bag_of_words(inp, words)])
            results_index = numpy.argmax(results)
            tag = labels[results_index]
    
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
    
            print(random.choice(responses))

if __name__ == '__main__':
    nn = neural_network()
    (model, words, labels, data) = nn.build_model_save()
    nn.chat(model,words, labels, data)
    pass