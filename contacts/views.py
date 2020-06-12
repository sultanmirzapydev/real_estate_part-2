from django.shortcuts import render, redirect
# we need to import messages to show alert messages
from django.contrib import messages
# need to import .models from contacts because we need to save fetch data to database table using models file
from .models import Contact
# to send email we need to import send_mail
from django.core.mail import send_mail



def contact(request):
	# in listing.html we select post method and here we check whether it is post method or not, then fetch the data 

	if request.method == 'POST':
		listing_id = request.POST['listing_id']
		listing    = request.POST['listing']
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		realtor_email = request.POST['realtor_email']

		# check if user has made inquiry already, if they then no need to do it again. so we will show error message
		if request.user.is_authenticated:
			#below comment line(user_id) not really needed
			#user_id = request.user.id  

			has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)

			#check to see if the user has made submission before or not
			if has_contacted:
				messages.error(request, 'you have already made and enquiry for this listing')
				return redirect('/listings/'+listing_id)





		#this next step need to be done . first we created a model for contacts  to save the details in database and then 
		#show it to the admin user section (to show it we need to add contacts to admin section ).
		# to save the data to database we need to match and assign the values to models by every models variable
		# assign every extract values to the variable or tables in database just like we did for registering new acc
		contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
			user_id=user_id)
		contact.save()
		#to send email (email is not working , go to setting.py for more info)
		#send_mail (
		#	'property Listing Inquiry',
		#	'There has been an inquiry for ' + listing + '.Sign into the admin panel for more info',
		#	'sultanmirza136id@gmail.com',
		#	[realtor_email, 'sultanmirza136id@gmail.com'],
		#	fail_silently = False
		#	)

		messages.success(request, 'Your request has been submitted , a realtor will get back to you soon')

		# then need to redirect the use to the listing page
		return redirect('/listings/'+listing_id)


