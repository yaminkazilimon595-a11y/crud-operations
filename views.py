from django.shortcuts import render, redirect,get_object_or_404
from .models import Student

def studentpage(request):
    student=Student.objects.all()
    print('studentpage called', student)
    return render(request, 'student.html', {'student': student})

def singlestudent(request, id):
    student = get_object_or_404(Student, id=id)
    print('singlestudent called', student)
    return render(request, 'singlestudent.html', {'student': student})



def addstudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        student = Student(name=name, email=email, address=address)
        student.save()
        print("Student added successfully!")
        return redirect('studentpage')
        
    return render(request, 'addstudent.html')

def updatestudent(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        student.save()
        return redirect('studentpage')
        print("Student updated successfully!")
    return render(request, 'updatestudent.html', {'student': student})



def deletestudent(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    print("Student deleted successfully!")
    return redirect('studentpage')