import pickle

x = [1, 2, 3, 4, 5]

string = pickle.dumps(x)
print(pickle.loads(string))