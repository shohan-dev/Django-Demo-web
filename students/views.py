from django.shortcuts import render, redirect,HttpResponse
from .models import Student
from django.contrib.auth.models import User
from django.contrib import messages
import time
import re


def student_s(request):
    if request.method == 'POST':
        # Ensure the form has the 'enctype="multipart/form-data"' attribute
        # in the HTML template where you're rendering the form.

        # Use 'method' instead of 'METHOD' for comparison
        if request.method == 'POST':

            # Retrieve form data including the uploaded image
            s_name = request.POST.get('name')
            s_age = request.POST.get('age')
            s_gender = request.POST.get('gender')
            s_image = request.FILES.get('image')  # Use 'FILES' to get file data
            
            print("This is = ", s_image)  # Debugging
            
            # Create a Student object with the received data
            new_student = Student(name=s_name, age=s_age, gender=s_gender, image=s_image)
            
            # Save the Student object to the database
            new_student.save()

            return redirect("/")

    return render(request, 'student.html')

def table(request):
    data = Student.objects.all()
    context = {"data":data}
    return render(request, 'table.html',context)

def delete_txt(request,id):
    print(id)
    delete = Student.objects.get(id=id)
    delete.delete() 
    return redirect("/table")

# def update_table(request,id,s_name,s_age,s_gender,s_image):
    
    
#     Student.objects.update(name=s_name, age=s_age, gender=s_gender, image=s_image) 
#     return redirect("/table")

def update_table(request, id):
    try:
        data = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse("User not found")

    if request.method == 'POST':
        try:
            # Retrieve form data including the uploaded image
            s_name = request.POST.get('name')
            s_age = request.POST.get('age')
            s_gender = request.POST.get('gender')
            s_image = request.FILES.get('image')

            # Update the student object with new data
            data.name = s_name
            data.age = s_age
            data.gender = s_gender
            if s_image:
                data.image = s_image
            data.save()

            return redirect("/table")
        except Exception as e:
            return HttpResponse(f"Error updating data: {e}")

    context = {"data": data}
    return render(request, 'update_table.html', context)



def login(request):
    return render(request,'login.html')




from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')

        # Simple validation
        errors = {}
        if not name:
            errors['name'] = 'Name is required'
        if not username:
            errors['username'] = 'Username is required'
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Username already exists. Please choose a different username.'
        if not email:
            errors['email'] = 'Email is required'
        elif not isValidEmail(email):
            errors['email'] = 'Invalid email format'
        if not password:
            errors['password'] = 'Password is required'
        if password != request.POST.get('confirm_password'):
            errors['confirm_password'] = 'Passwords do not match'

        if errors:
            return render(request, 'register.html', {'errors': errors, 'data': request.POST})


        # Create user object with provided information
        user = User.objects.create_user(first_name=name, username=username, email=email, password=password)
        
        # Save user object to database
        user.save()

        messages.success(request, 'Registration successful!')
        return redirect('/login')

    # Render registration form for GET requests
    return render(request, 'register.html')

def isValidEmail(email):
    # Simple email validation regex
    emailRegex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(emailRegex, email)






