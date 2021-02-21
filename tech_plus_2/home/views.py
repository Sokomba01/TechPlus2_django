from django.shortcuts import render, HttpResponse
from  .models import MyUsers
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect,render
# Create your views here.
from w3lib import form


def index(request):
    return render(request, 'report.html')

def SignInPage(request):
    return render(request, 'login.html')

def SignUpPage(request):
    return render(request, 'signup.html')

def TermsPage(request):
    return render(request, 'terms.html')

def PolicyPage(request):
    return render(request, 'policy.html')

def PricingPage(request):
    return render(request, 'pricing.html')


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

def SignIn(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        dbEmail = MyUsers.objects.get(email = email)
        #dbPassord = MyUsers.objects.get(password = password)

        print("emial",email)
        print("pass", password)
        print("dbEmail", dbEmail.password)
        print("dbPass", dbEmail.email)

        if dbEmail.email == email and password == dbEmail.password:
            #obj = MyUsers.objects.get(email=email)
            return render(request, 'index.html')

        else:
            return redirect('signInPage')
