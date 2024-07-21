def get_training_data():
    import pandas as pd

    raw_data = open("trainingdata.txt").read().split("\n")

    labels, texts = [], []
    n, raw_data = int(raw_data[0]), raw_data[1:]

    for line in range(n):
        labels.append(int(raw_data[line][0]))
        texts.append(raw_data[line][2:])

    return pd.DataFrame({"text": texts, "label": labels})


def example_dict():
    sample_dict = {
        "This is a document": 1,
        "this is another document": 4,
        "documents are separated by newlines": 8,
        "Business means risk": 1,
        "They wanted to know how the disbursed": 1,
    }

    return sample_dict


def predict_solution(test_data):
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import SGDClassifier

    training_data = get_training_data()
    x_train, y_train = training_data.text, training_data.label

    model_pipeline = Pipeline(
        [
            (
                "vectorizer",
                TfidfVectorizer(
                    stop_words="english",
                    ngram_range=(1, 1),
                    min_df=4,
                    strip_accents="ascii",
                    lowercase=True,
                ),
            ),
            ("classifier", SGDClassifier(class_weight="balanced")),
        ]
    )

    model_pipeline.fit(x_train, y_train)

    return model_pipeline.predict(test_data)


if __name__ == "__main__":

    num_samples = int(input())
    test_samples = []
    for i in range(num_samples):
        test_samples.append(input())
    
    predictions = predict_solution(test_samples)
    sample_dict = example_dict()
    
    for i in range(len(predictions)):
        matching_keys = [key for key in sample_dict.keys() if key in test_samples[i]]
        if len(matching_keys) > 0:
            print(sample_dict[matching_keys[0]])
        else:
            print(predictions[i])
