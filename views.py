from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']
        print(name,email,phone,course)
        Student.objects.create(Name=name,Email=email,PhoneNumber=phone,Course=course)

        return render(request,'home.html')
    return render(request,'home.html')


def all_student(request):
    all_students = Student.objects.all()
    return render(request,'all_student.html',{'all_students':all_students})

def Delete(request,stu_id):
    student = Student.objects.get(id=stu_id)
    if student:
        student.delete()
    return redirect(all_student)


def Edit(request,stu_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']

        old_student = Student.objects.get(id=stu_id)
        old_student.Name = name
        old_student.Email = email
        old_student.PhoneNumber = phone
        old_student.Course = course
        old_student.save()
        return redirect(all_student)
    return render(request,'edit.html')
        