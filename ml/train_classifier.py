import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data_dict = pickle.load(open('data.pickle', 'rb'))

X = data_dict['data']
y = data_dict['labels']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=True, stratify=y
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)

print("✅ Model trained and saved as model.p")
