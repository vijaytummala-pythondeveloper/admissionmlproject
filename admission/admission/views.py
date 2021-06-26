from django.shortcuts import render
from pathlib import Path
import pickle

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    return render(request,'home.html')

def showdata(request):
    marks = int(request.GET['marks'])
    score = int(request.GET['ts'])
    model_path = f'{BASE_DIR}\\admission\\lrmodel.sav'
    file = open(model_path,'rb')
    model = pickle.load(file)
    res= model.predict([[marks,score]])
    if res[0] == 0:
        str_res = "sorry no admission"
    else:
        str_res = "admission"

    return render(request, 'home.html',{'res':str_res})