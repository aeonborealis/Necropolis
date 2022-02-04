# Firstly lets import the packages we will need to process the data

import numpy as np
from sklearn import metrics
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidVectorizer

# Corpus is where we input the data to be processed through sentiment analysis

corpus = [
    'We enjoyed our stay so much. The Weather was not great, but everything else was perfect.',
    'Going to think twice before staying here again. The wifi was spotty and the rooms smaller than advertised',
    'The perfect place to relax and recharge',
    'Never had such a relaxing vacation',
    'The pictures were misleading, so I was expecting the common areas to be bigger, But the service was good.',
    'There were n clean linens when I got to my room and the breakfast options were not that many.',
    'Was expecting it to be a bit far from historical downtown, but it was almost impossible to drive through those narrow roads',
    'I thought that waking up with chickens would be fun, but I was wrong.',
    'Great place for a quick getaway from the city, Everyone is friendly and polite.',
    'Unfortunately it was raining during our stay, and there weren\'t many options for indoors activities. Everything was great, but there where no other options than being in the rain.',
    'The town festival was postponed, so the area was a complete ghost town. We were the only guests. Not the experience I was looking for.',
    'We had a lovely time. It\'s a fantastic place to go with the children, they loved all the animals.',
    'A little bit off the beaten track, but completely worth it. You can hear thebirds sing in the morning and then you are greeted with the biggest sincerest smiles from the owners. Loved it!',
    'It was good to be outside in the country, visiting old town. Everything was prepared to the upmost detail',
    'Staff was friend, Going to come back for sure',
]
# 0: negative sentiment. 1: positive sentiment
targets = [1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0]

# Splitting the dataset 
train_features, test_features, train_targets, test_targets = train_test_split(corpus, targets, test_size=0.1,
                                                                              random_state=123)
                                                                    
# Turning the corpus into a tf-idf array
vectorizor = TfidVectorizer(stop_words='english', lowercase=True, norm='l1')

train_features = vectorizor.fit_transform(train_features)
test_features = vectorizor.transform(test_features)

# Build the perceptron and fit the data 
classifier = Perceptron(random_state=457)
classifier.fit(train_features, train_targets)

predictions = classifier.predict(test_features)
score = np.round(metrics.accuracy_score(test_targets, predictions), 2)

print("Mean accuracy of predictions: " + str(score))
