from django.http import HttpResponse
from django.shortcuts import render
import joblib,os
import pickle

phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)

def home(request):
    return render(request,"home.html")


def result(features):
	X_predict = []
	X_predict.append(str(features))
	y_Predict = phish_model_ls.predict(X_predict)
	if y_Predict == 'bad':
		result = "ALERT!! PHISHING SITE DETECTED"
	else:
		result = "LEGITMATE SITE DETECTED"

	return render(features, "result.html",{'result' : result})
