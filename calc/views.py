from django.shortcuts import render
from django.http import HttpResponse
import csv, os
import mysql.connector

# Create your views here.
filename = 'D:/PythonWorkSpace/Django/testProject/testProject/user_details.csv'


def home(request):
    #return HttpResponse("<h2>Hello World</h2>") #when called this method just prints helloworld in the browser.
    #num1 = input("hello world: ")
    #print(num1)

    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def add(request):

    val1 = request.POST['num1']

    flag = check_user(val1)
    if(flag):
        details = get_details(val1)
        print("\n\n\n\n")
        return render(request, 'result.html', {'name': 'welcome '+details[0], 'email': details[1],
                                               'gender': details[2], 'dob': details[3], 'unique_id': details[4]})


    return render(request, 'result.html', {'name' : 'Improper Unique ID'})


def signup(request):

    try:
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        dob = request.POST['birthday']
        next_unique_id = find_next_unique()
        add_user(name,email,gender,dob,next_unique_id)

        return render(request, 'home.html', {'reg_msg': 'User '+ name +' registered successfully with unique id '+ next_unique_id})
    except:
        return render(request,'home.html',{'reg_msg':'Error occured during registration, try again properly'})

def find_next_unique():
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            next_id = row[0]
    next_id = str(int(next_id)+1)
    return next_id

def add_user(name,email,gender,dob,unique_id):
    with open(filename,'a',newline='') as csvfile:
        row = [unique_id,name,email,gender,dob]
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)


def check_user(unique_id):
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            if(unique_id == row[0]):
                return True
        return False


def get_details(unique_id):
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            if(unique_id == row[0]):
                return [row[1],row[2],row[3],row[4],row[0]];

