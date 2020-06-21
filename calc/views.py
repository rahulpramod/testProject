from django.shortcuts import render
from django.http import HttpResponse
import csv, os
import datetime
import time
#import mysql.connector

# Create your views here.
filename = 'D:/PythonWorkSpace/Django/testProject/testProject/user_details.csv'
file = 'D:/PythonWorkSpace/Django/testProject/testProject/patient_logs.csv'

val1 = 100000
details = []

def home(request):
    #return HttpResponse("<h2>Hello World</h2>") #when called this method just prints helloworld in the browser.
    #num1 = input("hello world: ")
    #print(num1)

    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def add(request):

    val1 = request.POST['num1']
    global details

    flag = check_user(val1)
    if(flag):
        details = get_details(val1)
        print("\n\n\n\n")
        return render(request, 'result.html', {'name': 'welcome '+details[0], 'email': details[1],
                                               'gender': details[2], 'dob': details[3], 'unique_id': details[4]})


    return render(request, 'home.html', {'reg_msg' : 'Improper Unique ID'})

def about(request):
    return render(request, 'about.html')

def gohome(request):
    return render(request,'home.html')

def addLogs(request):
    global details
    return render(request, 'addLogs.html', {'uq_id' : details[0]+'  Unique ID :'+details[4]+' '})

def showLogs(request):
    global details
    data = ''
    i = 1
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if (details[4] == row[0] and data == ''):
                data = data + str(i) + ") " + row[1]
                i+=1

            elif (details[4] == row[0]):
                data = data + ". " + str(i) +") " + row[1]
                i+=1
    return render(request,'showLogs.html', {'logs1': data})


def post_data(request):
        data = request.POST['data']

        with open(file, 'a+', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            date = str(datetime.datetime.now().date())
            tm = str(datetime.datetime.now().time())
            secPart = str(tm.split(':')[2].split('.')[0])
            tmstp = str(date.split('-')[2]) + '/' + str(date.split('-')[1]) + '/' + str(date.split('-')[0]) + ' ' + str(
                tm.split(':')[0]) + ':' + str(tm.split(':')[1]) + ':' + str(secPart)
            data = "On "+ tmstp + " --->" + data
            row = [details[4], data]
            csvwriter.writerow(row)
        return render(request, 'home.html',
                      {'reg_msg':'Patient '+details[0]+' Unique ID: '+details[4]+' have been written into database successfully'})
       # return render(request, 'home.html', {'reg_msg': 'Error occured during writind data in database, try again properly'})



def signup(request):

    try:
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        dob = request.POST['birthday']
        print(dob,type(dob))
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



