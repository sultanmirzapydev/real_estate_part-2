from django.shortcuts import render, redirect
#need to import auth for authenticating /  user for creating user
from django.contrib import messages, auth
from django.contrib.auth.models import User
#need to bring contact models from cotacts app
from contacts.models import Contact 	
# Create your views here. 
def register(request):
	if request.method == 'POST':
		#get form values, fetching data from register.html page of registration form submission
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']

		#check if password match
		if password == password2:
			#check if username is already used or not, if not then proceed for next step
			if User.objects.filter(username=username).exists():
				messages.error(request, 'that username is already taken')
				return redirect('register')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request, 'this email is taken')
					return redirect('register')
				else:
					#if everyting is okey then create the user as per the person's input 
					user = User.objects.create_user(username=username, email=email, password=password, 
						first_name=first_name, last_name=last_name)
					#if you want to login the user immediately / automatically as the user register their account
					#auth.login(request, user)
					#to show message that the user is logged in 
					#messages.success(request, 'you are now logged in')
					#return redirect('index')
					
					# if we don't want to login the user directly as they create the user ,	then we can do this
					user.save()
					messages.success(request, 'you are now registered and can log in ')
					return redirect('login')

		else:
			messages.error(request, 'passwords do not match')
			return redirect('register')


	else:

		return render(request, 'accounts/register.html')

def login(request):
	if request.method =='POST':
		#login user
		#fetch the data from post method request
		username = request.POST['username']
		password = request.POST['password']
		#now after extracting the data need to authenticate whether they are registered and saved in the database or not
		user = auth.authenticate(username=username, password=password)

		#if the user details are in database then (check using condition) let use log in
		if user:
			# code for loggin in
			auth.login(request, user)
			#need to inform the user that they have been successfully logged in

			messages.success(request, 'you are now logged in')

			return redirect('dashboard')
		else:
			#if there is no information in our database of what the use has put
			messages.error(request, 'invalid credentials')
			return redirect('login')
			
	else:
		

		return render(request, 'accounts/login.html')

def logout(request):
	# for log out we need to make a post request , we can't use a tag or herf attribute
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request, 'you are now logged out')
		return redirect('index')

def dashboard(request):
	user_contacts = Contact.objects.order_by('-Contact_date').filter(user_id=request.user.id)

	context = {
		'contacts':user_contacts
	}
	return render(request, 'accounts/dashboard.html', context)
