from django.shortcuts import render, HttpResponse
from  .models import MyUsers
# Create your views here.
from w3lib import form


def index(request):
    return render(request, 'signup.html')


def SignUp(request):
    if request.method == 'POST':
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        portExistingNumber = request.POST["portExistingNumber"]
        password = request.POST["password"]
        attachedDocument = request.POST["attachedDocument"]
        ins = MyUsers(fName = fname, lName = lname, email = email, password = password, portExistingNumber = portExistingNumber, sharedDocument = attachedDocument)
        ins.save()
    return render(request, 'index.html')
