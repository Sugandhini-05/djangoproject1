from django.shortcuts import render, redirect, get_object_or_404
from app1.models import Student
from app1.forms import StudentForm

# 🔐 Default credentials (you can change)
USERNAME = "admin"
PASSWORD = "1234"


# 🔹 READ (List)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


# 🔹 CREATE
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})


# 🔹 UPDATE
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {'form': form})


# 🔹 LOGIN BEFORE DELETE
def delete_login(request, id):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == USERNAME and password == PASSWORD:
            request.session['delete_auth'] = True
            return redirect('student_delete', id=id)
        else:
            return render(request, 'delete_login.html', {
                'error': 'Wrong credentials',
                'id': id
            })

    return render(request, 'delete_login.html', {'id': id})


# 🔹 DELETE (Protected)
def student_delete(request, id):

    # check if user is authenticated for delete
    if not request.session.get('delete_auth'):
        return redirect('delete_login', id=id)

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()

        # clear session after delete
        request.session.flush()

        return redirect('student_list')

    return render(request, 'student_confirm_delete.html', {'student': student})