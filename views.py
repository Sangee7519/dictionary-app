# import librarys 

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from dictapp import views
import mysql.connector as mysql
from PyDictionary import PyDictionary
from translate import Translator

# dictionary 
def Dictionary(request):
	if request.method == "POST":
		word=request.POST['word']
		url='https://www.dictionary.com/browse/'+word
		r=requests.get(url)
		data=r.content
		soup=BeautifulSoup(data,'html.parser')
		span=soup.find_all('span',{"class":"one-click-content"})
		synonyms=soup.find_all("a",{'class':'luna-xref'})
		idoms=soup.find_all("li",{'class':'one-click-content'})
		ss=[]
		for b in synonyms[0:]:
			re=b.text.strip()
			ss.append(re)
		synonyms=ss
		idom=[]
		for i in idoms[0:]:
			re=i.text
			idom.append(re)
		idom=idom
		language = request.POST["language"]
		translator= Translator(to_lang=language)
		translation = translator.translate(word)
		param={'text':span[0].text,'word':word,'se':synonyms,'idoms':idom,'translator':translation}
		return render(request,'index.html',param)

	else:
		return render(request,'index.html')	
# home page 
def h(request):
	import random
 
	# prints a random value from the list
	list1 = ["'The purpose of our lives is to be happy'. — Dalai Lama",
	"'Life is what happens when you’re busy making other plans.' — John Lennon",
	"Get busy living or get busy dying. — Stephen King",
	"“You only live once, but if you do it right, once is enough.” — Mae West",
	"“Many of life’s failures are people who did not realize how close they were to success when they gave up.”– Thomas A. Edison",
	" “If you want to live a happy life, tie it to a goal, not to people or things.”– Albert Einstein",]
	re=random.choice(list1)
	return render(request,'h1.html',{"result":re})
 

# templates	
def login(request):
	return render(request,'h3.html')
def signup(request):
	return render(request,'h2.html')
def Quotes(request):
	return render(request,'quotes.html')
def page1(request):
	return render(request,'quo.html')	
def page2(request):
	return render(request,'q2.html')

# database
def insert (request):
	name=request.GET.get("name")
	email=request.GET.get("email")
	password=request.GET.get("password")
	conn=mysql.connect(host="127.0.0.1",user="root",password="75197519",database="signup",port="3306")
	cr=conn.cursor()
	query="insert into dicts values('{0}','{1}','{2}')".format(name,email,password)
	cr.execute(query)
	conn.commit()
	conn.close()
	return redirect("/login")


	
def logintask(request):
	email=request.GET.get("email")
	password=request.GET.get("pass")
	conn=mysql.connect(host="127.0.0.1",user="root",password="75197519",database="signup",port="3306")
	cr=conn.cursor()
	cr.execute("select * from dicts")
	while True:
		row=cr.fetchone()
		if row is None:
			break;
			
		elif row[2]==email and row[3]==password:
			return redirect('/Dictionary')
	return redirect('/login')			

# adimin pannel information
def admin(request):
	return render(request,"admin.html")
def adminlogin(request):
	username=request.GET.get("uname")
	password=request.GET.get("pswd")
	conn=mysql.connect(host="127.0.0.1",user="root",password="75197519",database="signup",port="3306")
	cr=conn.cursor()
	cr.execute("select * from admin")
	while True:
		row=cr.fetchone()
		if row[0]==username or row[1]==password:
			return redirect('/view')
	return redirect('/login')
	
def view(request):
	conn=mysql.connect(host="127.0.0.1",user="root",password="75197519",database="signup",port="3306")
	cr=conn.cursor()
	cr.execute("select * from dicts")
	result=cr.fetchall()
	conn.commit()
	conn.close()
	return render(request,"adminpage.html",{'result':result})