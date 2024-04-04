from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from shop.models import Product
from django.core.mail import send_mail


def get_data(request):
    # Fetch all products
    all_products = Product.objects.all()

    # Number of items per page
    items_per_page = 10

    # Initialize the paginator with the fetched data and the number of items per page
    paginator = Paginator(all_products, items_per_page)

    # Get the current page number from the request, default to 1 if not provided
    page_number = request.GET.get('page', 1)

    # Get the products for the requested page
    data = paginator.get_page(page_number)

    return render(request, 'product.html', {'page_obj': data})


# subject = 'Subject of the Email'
# message = 'This is the message body.'
# from_email = 'sabbirshohan80@gmail.com'  
# to_email = 'shohanplayer100@gmail.com'  

# send_mail(subject, message, from_email, [to_email])


from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.http import HttpResponse

def send_mail_from_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = request.POST.get('from_email')
        to_email = request.POST.get('to_email')
        attached_file = request.FILES.get('file')  # Get the attached file
        # Create EmailMessage instance
        email_message = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[to_email],
        )
        # Attach the file, if provided
        if attached_file:
            email_message.attach(attached_file.name, attached_file.read(), attached_file.content_type)
        try:
            # Send email
            email_message.send()
            # Redirect to '/' on success
            return redirect('/', {'name': name, 'email': email})
        except Exception as e:
            # If there's an error, render email.html with error message
            return render(request, 'email.html', {'error': str(e)})
    else:
        return render(request, 'email.html')




