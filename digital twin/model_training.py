from sklearn.linear_model import LinearRegression
import pickle

def train_model(data):
    model = LinearRegression()
    X = data.drop('output', axis=1)
    y = data['output']
    model.fit(X, y)
    return model

def save_model(model, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(model, f)
