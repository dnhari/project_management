from django.shortcuts import render,redirect
from .models import Book
from .models import MultipleBooks
from .models import User_extra
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as djangologin,logout as djlogout
from django.contrib.auth.decorators import login_required
import pdb
from .forms import BookForm
# Create your views here.
def index(request): 
	next_url = request.GET.get('next')
	return render(request,"login.html",context={'next_url':next_url})

@login_required(login_url='/')
def get_books(request):
	book_name=[]

	book_obj=Book.objects.all()
	for i in book_obj:
		book_name.append({'name':i.name,'author':i.author.username})

		 
	return render(request,"sample.html",context={'books':book_name,'flag':True})
@login_required(login_url='/')	
def get_bookby_id(request):
	book_list=[]

	book_id=request.GET.get('id')
	book_obj=Book.objects.filter(id=book_id)
	if book_obj.exists():
		for i in book_obj:
			book_list.append({'name':i.name,'author':i.author.username})
		return HttpResponse(book_list)
	else:
		return HttpResponse("no Book found")
@login_required(login_url='/')
def get_booksByUsers(request):
	book_list=[]

	book_id=eval(request.GET.get('id'))
	print(book_id)
	
	book_obj=Book.objects.filter(pk__in=book_id)
	if book_obj.exists():
		for i in book_obj:
			book_list.append({'name':i.name,'author':i.author.username,'id':i.id})
		return HttpResponse(book_list)
	else:
		return HttpResponse("no Book found")
@login_required(login_url='/')
def get_user_details(request):
	user_details=[]
	username=eval(request.GET.get('username'))
	print(user_details)

	user=User_extra.objects.filter(user__username=username).values('user__email','age','user__username','user__password','firstName','lastName','gender','address')
	#user_e=User_extra.objects.filter(user=user)
	print(user)
	for i in user:
		user_details.append(i)
	return render(request,'sample.html',context={'userDtails':user})

def login(request):
	username=request.POST.get('username')
	password=request.POST.get('password')
	auth_user=authenticate(username=username,password=password)
	current_user=request.user
	print(current_user)
	if auth_user:
		djangologin(request,auth_user)
		current_user=request.user.username
		if request.GET.get('next'):
			print(next)
			return redirect(request.GET.get('next'))
		return render(request,"dashboard.html",context={'username':current_user})
	else:
		return render(request,"failure.html")

def register(request):
	if request.method=='GET':
		return render(request,"register.html")
	else:
		print('d')
		username=request.POST.get('username')
		password=request.POST.get('password')
		firstname=request.POST.get('firstName')
		lastname=request.POST.get('lastName')
		age=request.POST.get('age')
		gender=request.POST.get('gender')
		address=request.POST.get('address')

		user_obj=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname)
		user_obj.save()
		user_details=User_extra.objects.create(user=user_obj,age=age,gender=gender,address=address)
		user_details.save()
		return render(request,'login.html')

def profile(request):
	if request.method=='GET':
		return render(request,"profile.html")
	else:
		firstName=request.POST.get('firstName')
		lastName=request.POST.get('lastName')
		age=request.POST.get('age')
		gender=request.POST.get('gender')
		address=request.POST.get('address')
		current_user=user
		print(current_user)
		user=User.objects.get(pk=current_user)
		print(user)
		user_obj=User_extra.objects.create(user=user,firstName=firstName,lastName=lastName,age=age,gender=gender,address=address)
		user_obj.save()
		return render(request,'dashboard.html')

	
def insert_book(request):
	if request.method=='GET':
		users=User.objects.all()
		return render(request,"insertbook.html",context={"users":users})
	else:
		name=request.POST.get('name')
		author=request.POST.get('author_id')
		print(author)
		multipleBooks=MultipleBooks.objects.create(name=name,author=User.objects.get(id=author))
		return render(request,'success.html')


def logout(request):
	djlogout(request)
	return HttpResponseRedirect('/')

def insert_book_form(request):
	if request.method=='GET':
		
		return render(request,"insertbookform.html",context={"form":BookForm()})
	else:
		form=BookForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'success.html')
		else:
			return HttpResponse("Failure")








	




