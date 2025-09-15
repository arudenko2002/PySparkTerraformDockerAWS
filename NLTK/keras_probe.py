'''
Created on Jan 5, 2020

@author: Alexey
'''

import tensorflow
class image_process: 
    def exec(self):
        import keras
        # 3. Import libraries and modules
        import numpy as np
        np.random.seed(123)  # for reproducibility
         
        from keras.models import Sequential
        from keras.layers import Dense, Dropout, Activation, Flatten
        from keras.layers import Convolution2D, MaxPooling2D
        from keras.utils import to_categorical
        from keras.datasets import mnist
         
        # 4. Load pre-shuffled MNIST data into train and test sets
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
         
        # 5. Preprocess input data
        X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
        X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
        
        #Plotting first sample of X_trainPython
        from matplotlib import pyplot as plt
        print("X_train shape =",X_train.shape)
        print("X_train shape =",X_train[0].shape)
        print("X_train[0]",X_train[0].reshape(28,28))

        # Plot
        plt.title('Label is {label}'.format(label="X_train[0].reshape(28, 28)"))
        plt.imshow(X_train[0].reshape(28, 28))
        plt.show()
         
        X_train = X_train.astype('float32')
        X_test = X_test.astype('float32')
        X_train /= 255
        X_test /= 255
        

        # 6. Preprocess class labels
        Y_train = to_categorical(y_train, 10)
        Y_test = to_categorical(y_test, 10)

        # 7. Define model architecture
        model = Sequential()
         
        model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(1,28,28), data_format='channels_first'))
        model.add(Convolution2D(32, 3, 3, activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Dropout(0.25))
         
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(10, activation='softmax'))
       
        # 8. Compile model
        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        # 9. Fit model on training data
        model.fit(X_train, Y_train, 
                  batch_size=32, epochs=10, verbose=0)
 
        # 10. Evaluate model on test data
        score = model.evaluate(X_test, Y_test, verbose=0)
        print("score",score)
        y_pred = model.predict(X_test)
        print("AAAA y_pred",y_pred[:5])
        print("BBBB y_test",y_test[:5])
        aa = [round(max(x),1) if max(x)>0.01 else 0 for x in y_pred[:5]]
        print("AAAA y_pred",aa)
        print("BBBB y_test",y_test[:5])
        
class csv_process:
    # https://www.datacamp.com/community/tutorials/deep-learning-python?utm_campaignid=282657556&utm_adgroupid=1144592160411863&utm_device=c&utm_keyword=keras&utm_matchtype=p&utm_network=o&utm_adpostion=&utm_creative=&utm_targetid=kwd-71537457267176:loc-190&utm_loc_interest_ms=&utm_loc_physical_ms=44152&msclkid=649ee6eb90571488cc9fb867262431bf&utm_source=bing&utm_medium=cpc&utm_campaign=NEW%20Granular%20Topics%20(via%20DSA%20insights)%20%7C%20U.S.%20BING&utm_term=keras&utm_content=community%2Ftutorials%2Fdeep-learning-python
    def exec(self):
        import pandas as pd
        
        # Read in white wine data 
        white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')
        print(white)
        print(white.info())
        # Read in red wine data 
        red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')
        print(red)
        print(red.info())
        
        # First rows of `red` 
        print("HEAD")
        print(red.head())

        # Last rows of `white`
        print("TAIL")
        print(white.tail())
        
        # Take a sample of 5 rows of `red`
        print("SAMPLE(5)")
        print(red.sample(5))
        
        # Describe `white`
        print("DESCRIBE")
        print(white.describe())
        
        # Double check for null values in `red`
        print("RED IS NULL")
        print(pd.isnull(red))
        #self.plot(red,white)
        #self.plot_sulfates_quality(red, white)
        #self.alcohol_acid_quality(red, white)
        wines = self.preprocess(red, white)
        #self.plot_correlation_matrix(wines)
        # create data sets for training/testing 
        (X_train, X_test, y_train, y_test) = self.train_test(wines)
        # model building
        model = self.model_builder()
        # model training
        model.fit(X_train, y_train,epochs=20, batch_size=1, verbose=1)
        # use of model with ALL TEST DATASET
        y_pred = model.predict(X_test)
        print("AAAA y_pred",y_pred[:5])
        print("BBBB y_test",y_test[:5])
        
        # SAMPLE as a fragment of the data set (1 record)
        sample = X_test[2100:2101]
        print("sample=",sample)
        y_pred2 = model.predict(sample)
        res = "white" if y_pred2<0.5 else "red"
        print("RESULT: Y_PRED2=",y_pred2, res)
        
        #MY EXAMPLE
        np_sample = self.get_my_sample()
        y_pred3 = model.predict(np_sample)
        res = "white" if y_pred3<0.5 else "red"
        print("RESULT: Y_PRED3=",y_pred3,res)
        
        print("X_train",y_train)
        print("X_test",X_test)
        print("y_train",y_train)
        print("y_test",y_test)
        print("y_pred=",y_pred)
        print("y_pred.round()=",y_pred.round())
        # model evaluation
        self.evaluate_result(model, X_test, y_test, y_pred)
        
    def get_my_sample(self):
        import numpy as np
        #MY EXAMPLE
        sample2=[[-0.85554075,-0.53271186,1.17719142,0.44532964,-0.10476147,2.09206997,1.98070358,  0.30633732, -0.36036033, -0.40502868, -1.32624454]]
        print("sample2=",sample2)
        print(type(sample2))
        np_sample = np.array(sample2)
        print("np_sample",np_sample)
        print(type(np_sample))
        
        #STANDARDIZATION
        # Import `StandardScaler` from `sklearn.preprocessing`
        from sklearn.preprocessing import StandardScaler
        # Define the scaler 
        scaler = StandardScaler().fit(np_sample)
        # Scale the train set
        #np_sample = scaler.transform(np_sample)
        return np_sample
        
    def evaluate_result(self, model, X_test, y_test, y_pred):
        score = model.evaluate(X_test, y_test,verbose=1)
        print("score=",score)
        # Import the modules from `sklearn.metrics`
        from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score
        # Confusion matrix
        print("confusion matrix = ",confusion_matrix(y_test, y_pred.round()))
        # Precision 
        print("precision_score=",precision_score(y_test, y_pred.round()))
        #0.994565217391
        # Recall
        print("recall=",recall_score(y_test, y_pred.round()))
        #0.98563734290843807
        # F1 score
        print("f1=",f1_score(y_test,y_pred.round()))
        #0.99008115419296661
        # Cohen's kappa
        print("cohen_kappa=",cohen_kappa_score(y_test, y_pred.round()))
        
    def preprocess(self,red, white):
        # Add `type` column to `red` with value 1
        red['type'] = 1
        
        # Add `type` column to `white` with value 0
        white['type'] = 0
        
        # Append `white` to `red`
        wines = red.append(white, ignore_index=True)
        print("Preprocess: added type, white+red=")
        print(wines)
        return wines
    
    def plot_correlation_matrix(self,wines):
        import seaborn as sns
        import matplotlib.pyplot as plt
        corr = wines.corr()
        sns.heatmap(corr, 
                    xticklabels=corr.columns.values,
                    yticklabels=corr.columns.values)
        #you may as well simply use plt.show(), as sns.plt.show() is only working because pyplot is available inside the seaborn namespace.
        plt.show()
        
    def plot(self,red,white):
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots(1, 2)
        
        ax[0].hist(red.alcohol, 10, facecolor='red', alpha=0.5, label="Red wine")
        ax[1].hist(white.alcohol, 10, facecolor='white', ec="black", lw=0.5, alpha=0.5, label="White wine")
        
        fig.subplots_adjust(left=0, right=1, bottom=0, top=0.5, hspace=0.05, wspace=1)
        ax[0].set_ylim([0, 1000])
        ax[0].set_xlabel("Alcohol in % Vol")
        ax[0].set_ylabel("Frequency")
        ax[1].set_xlabel("Alcohol in % Vol")
        ax[1].set_ylabel("Frequency")
        #ax[0].legend(loc='best')
        #ax[1].legend(loc='best')
        fig.suptitle("Distribution of Alcohol in % Vol")
        plt.show()
        
        import numpy as np
        print("RED:")
        print(np.histogram(red.alcohol, bins=[7,8,9,10,11,12,13,14,15]))
        print("WHITE:")
        print(np.histogram(white.alcohol, bins=[7,8,9,10,11,12,13,14,15]))
        
    def plot_sulfates_quality(self, red, white):
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(8, 4))
        ax[0].scatter(red['quality'], red["sulphates"], color="red")
        ax[1].scatter(white['quality'], white['sulphates'], color="white", edgecolors="black", lw=0.5)
        
        ax[0].set_title("Red Wine")
        ax[1].set_title("White Wine")
        ax[0].set_xlabel("Quality")
        ax[1].set_xlabel("Quality")
        ax[0].set_ylabel("Sulphates")
        ax[1].set_ylabel("Sulphates")
        ax[0].set_xlim([0,10])
        ax[1].set_xlim([0,10])
        ax[0].set_ylim([0,2.5])
        ax[1].set_ylim([0,2.5])
        fig.subplots_adjust(wspace=0.5)
        fig.suptitle("Wine Quality by Amount of Sulphates")
        
        plt.show()
        
    def alcohol_acid_quality(self,red,white):
        import matplotlib.pyplot as plt
        import numpy as np
        
        np.random.seed(570)
        
        redlabels = np.unique(red['quality'])
        whitelabels = np.unique(white['quality'])
        
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(8, 4))
        redcolors = np.random.rand(6,4)
        whitecolors = np.append(redcolors, np.random.rand(1,4), axis=0)
        
        for i in range(len(redcolors)):
            redy = red['alcohol'][red.quality == redlabels[i]]
            redx = red['volatile acidity'][red.quality == redlabels[i]]
            ax[0].scatter(redx, redy, c=redcolors[i])
        for i in range(len(whitecolors)):
            whitey = white['alcohol'][white.quality == whitelabels[i]]
            whitex = white['volatile acidity'][white.quality == whitelabels[i]]
            ax[1].scatter(whitex, whitey, c=whitecolors[i])
            
        ax[0].set_title("Red Wine")
        ax[1].set_title("White Wine")
        ax[0].set_xlim([0,1.7])
        ax[1].set_xlim([0,1.7])
        ax[0].set_ylim([5,15.5])
        ax[1].set_ylim([5,15.5])
        ax[0].set_xlabel("Volatile Acidity")
        ax[0].set_ylabel("Alcohol")
        ax[1].set_xlabel("Volatile Acidity")
        ax[1].set_ylabel("Alcohol") 
        #ax[0].legend(redlabels, loc='best', bbox_to_anchor=(1.3, 1))
        ax[1].legend(whitelabels, loc='best', bbox_to_anchor=(1.3, 1))
        #fig.suptitle("Alcohol - Volatile Acidity")
        fig.subplots_adjust(top=0.85, wspace=0.7)
        
        plt.show()
        
    def train_test(self, wines):
        import numpy as np
        # Import `train_test_split` from `sklearn.model_selection`
        from sklearn.model_selection import train_test_split
        
        # Specify the data 
        X=wines.ix[:,0:11]
        
        # Specify the target labels and flatten the array
        y= np.ravel(wines.type)
        
        # Split the data up in train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        
        #STANDARDIZATION
        # Import `StandardScaler` from `sklearn.preprocessing`
        from sklearn.preprocessing import StandardScaler
        
        # Define the scaler 
        scaler = StandardScaler().fit(X_train)
        
        # Scale the train set
        X_train = scaler.transform(X_train)
        
        # Scale the test set
        X_test = scaler.transform(X_test)
        
        return (X_train, X_test, y_train, y_test)
        
    def model_builder(self):
        # Import `Sequential` from `keras.models`
        from keras.models import Sequential
        
        # Import `Dense` from `keras.layers`
        from keras.layers import Dense
        
        # Initialize the constructor
        model = Sequential()
        
        # Add an input layer 
        model.add(Dense(12, activation='relu', input_shape=(11,)))
        
        # Add one hidden layer 
        model.add(Dense(8, activation='relu'))
        
        # Add an output layer 
        model.add(Dense(1, activation='sigmoid'))
        
        # Model output shape
        model.output_shape
        
        # Model summary
        model.summary()
        
        # Model config
        model.get_config()
        
        # List all weight tensors 
        model.get_weights()
        
        model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
        return model
    
    def training_fit(self,model, X_train, y_train, X_test, y_test):
        model.fit(X_train, y_train,epochs=20, batch_size=1, verbose=1)
        y_pred = model.predict(X_test)
        print("AAAA y_pred",y_pred[:5])
        print("BBBB y_test",y_test[:5])
        return y_pred
    
    def play_with_quality(self):
        import pandas as pd
        # Read in white wine data 
        white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')
        print(white)
        print(white.info())
        # Read in red wine data 
        red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')
        print(red)
        print(red.info())
        
        # First rows of `red` 
        print("HEAD")
        print(red.head())

        # Last rows of `white`
        print("TAIL")
        print(white.tail())
        
        # Take a sample of 5 rows of `red`
        print("SAMPLE(5)")
        print(red.sample(5))
        
        # Describe `white`
        print("DESCRIBE")
        print(white.describe())
        
        # Double check for null values in `red`
        print("RED IS NULL")
        print(pd.isnull(red))
        #self.plot(red,white)
        #self.plot_sulfates_quality(red, white)
        #self.alcohol_acid_quality(red, white)
        wines = self.preprocess(red, white)

        # Isolate target labels
        Y = wines.quality
        
        # Isolate data
        X = wines.drop('quality', axis=1) 
        print(X[:5])
        print(Y)
        
        # STANDARDIZATION
        # Import `StandardScaler` from `sklearn.preprocessing`
        from sklearn.preprocessing import StandardScaler
        # Scale the data with `StandardScaler`
        X = StandardScaler().fit_transform(X)
        print(X[:5])
        
        # MODEL BUILDING
        # Import `Sequential` from `keras.models`
        from keras.models import Sequential
        # Import `Dense` from `keras.layers`
        from keras.layers import Dense
        # Initialize the model
        #model = Sequential()
        # Add input layer 
        #model.add(Dense(64, input_dim=12, activation='relu'))  
        # Add output layer 
        #model.add(Dense(1))
        
        import numpy as np
        from sklearn.model_selection import StratifiedKFold
        
        seed = 7
        np.random.seed(seed)
        from sklearn.metrics import r2_score
        kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
        for train, test in kfold.split(X, Y):
            model = Sequential()
            model.add(Dense(64, input_dim=12, activation='relu'))
            model.add(Dense(1))
            
            # Variation #1 Number of layers
            #model = Sequential()
            #model.add(Dense(64, input_dim=12, activation='relu'))
            #model.add(Dense(64, activation='relu'))
            #model.add(Dense(1))
            #mse_value 0.49269656028263015
            #mae_value 0.5493431687355042
            #r2_s 0.35472662717342596
            
            # Variation #2 Number of hiddeen units
            #model = Sequential()
            #model.add(Dense(128, input_dim=12, activation='relu'))
            #model.add(Dense(1))
            #mse_value 0.49788615706335865
            #mae_value 0.5462076663970947
            #r2_s 0.3479299268140168
            
            model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
            # Compilation variation #2 optimizer rmsprop
            #from keras.optimizers import RMSprop
            #rmsprop = RMSprop(lr=0.0001)
            #model.compile(optimizer=rmsprop, loss='mse', metrics=['mae'])
            #mse_value 1.5122553122970488
            #mae_value 0.9712327718734741
            #r2_s -0.9805660771890417
            
            # Compilation variation #3 optimizer sgd
            #from keras.optimizers import SGD
            #sgd=SGD(lr=0.1)
            #model.compile(optimizer=sgd, loss='mse', metrics=['mae'])
            #mse_value 0.49350282155246894
            #mae_value 0.548958420753479
            #r2_s 0.3536706792026868
            
            
            model.fit(X[train], Y[train], epochs=10, verbose=0)
            y_pred = model.predict(X[test])
            print("y_pred=",y_pred)
            mse_value, mae_value = model.evaluate(X[test], Y[test], verbose=0)
            print("mse_value",mse_value)
            #0.522478731072
            print("mae_value",mae_value)
            #0.561965950103
            r2_s = r2_score(Y[test], y_pred)
            print("r2_s",r2_s)
            #0.3125092543
        
if __name__ == '__main__':
    ip = image_process()
    ip.exec()
    print("ENDDDDDDDDDD of EXEC")
    exit(0)
    csvp = csv_process()
    #csvp.exec()
    #csvp.play_with_quality()
    pass