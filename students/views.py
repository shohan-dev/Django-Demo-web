from django.shortcuts import render, redirect
from .models import Student

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
