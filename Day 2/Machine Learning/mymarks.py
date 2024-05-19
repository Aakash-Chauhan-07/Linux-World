import joblib

lr = joblib.load('model')

x = float(input("Enter how many hours you studied: "))
print("Your marks are: ", lr.predict([[ x ]]))