from django.shortcuts import render, redirect
from .models import Member
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

total_members = []
users = {}
programdata = {"signed_in": False}

def redshare(request):

	if not request.user.is_authenticated:
		return redirect('/display')

	return redirect("/login")

def login(request):
	if request.user.is_authenticated:
		return redirect('/display')

	try:
		username = request.POST['username']
		password = request.POST['password']
	except:
		return render(request, 'login.html')


	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return redirect('/')
	else:
		messages.info(request, "Wrong Credentials")
		return render(request, 'login.html')


def display(request):
	if not request.user.is_authenticated:
		return redirect('/login')

	total_members = Member.objects.all()
	return render(request, "display.html", {"members": total_members})

def signup(request):
	if request.user.is_authenticated:
		return redirect('/display')
	try:
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		
		username = request.POST['username']
		password = request.POST['password']
	except:
		return render(request, "signup.html")

	if User.objects.filter(username=username).exists():
		messages.info(request, "Usename Already Exists")
		return render(request, 'signup.html')

	user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password)
	user.save()

	return redirect("display")


def add_donor(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	try:
		name = request.POST['name']
		blood_group = request.POST['blood-group']
		phone_number = request.POST['ph-number']
		place = request.POST['place']
	except:
		return render(request, 'add_donor.html', {'section': "ADD DONOR"})

	donor = Member(name=name, blood_group=blood_group, phone_number=phone_number, place=place)
	donor.save()

	return redirect("/display")

	

def logout(request):
	auth.logout(request)
	messages.info(request, "Logged Out")
	programdata['signed_in'] = False
	return redirect("/login")