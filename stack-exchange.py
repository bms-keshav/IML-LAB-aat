import json, sys
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer

if sys.version_info[0] >= 3: 
    user_input = input

vectorizer = HashingVectorizer(stop_words='english')

training_data = []
training_labels = []
training_file = open('training.json')
for i in range(int(training_file.readline())):
    record = json.loads(training_file.readline())
    training_data.append(record['question'] + "\r\n" + record['excerpt'])
    training_labels.append(record['topic'])
training_file.close()

training_matrix = vectorizer.fit_transform(training_data)
model = LinearSVC()
model.fit(training_matrix, training_labels)

testing_data = []
for i in range(int(user_input())):
    record = json.loads(user_input())
    testing_data.append(record['question'] + "\r\n" + record['excerpt'])

testing_matrix = vectorizer.transform(testing_data)
predicted_labels = model.predict(testing_matrix)

for label in predicted_labels: 
    print(label)
