from django.shortcuts import render,redirect
from .models import People
import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="1432000",
#   database="testdb"
# )

def show(request):
    people_list = People.objects.all()
    ppl = {'ppl':people_list}
    return render(request,'show.html',ppl)

    # mycursor = mydb.cursor()
    # mycursor.execute("SELECT * FROM people")
    # myresult = mycursor.fetchall()
    # ppl = {'people_list':myresult}
    # for p in myresult:
    #     print(p)
    # return render(request,'templates/show.html',ppl)
    