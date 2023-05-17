import pickle


class Inferencer:

    def __init__(self):

        with open("src/data/model.pkl", 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, features):

        return self.model.predict(features)
