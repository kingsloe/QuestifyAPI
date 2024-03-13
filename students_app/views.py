from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import (
    StudentUserInfoForm, 
    OutsideStudentInfoForm,
)
from .models import StudentInfo
from django.contrib.auth.models import Group
from django.contrib import messages
from notice_app.models import Notice

# Create your views here.


def student_signup_view(request):
    form1 = StudentUserInfoForm()
    form2 = OutsideStudentInfoForm()

    if request.method == 'POST':
        form1 = StudentUserInfoForm(request.POST)
        form2 = OutsideStudentInfoForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
            messages.success(request, 'Signing up was successful')
            return redirect('login')
        else:
            messages.error(request, 'Could not sign up')

    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'student_signup.html', context)


def student_homepage_view(request):
    student_data = get_object_or_404(StudentInfo, status=True, user=request.user)
    payment_record = student_data.payment_set.all().order_by('-id')
    notices = Notice.objects.all()

    context = {
        'student_data': student_data,
        'payment_record': payment_record,
        'notices': notices,
        'method': student_data.payment_method == 'School_Fees_Aside',
    }
    return render(request, 'student_homepage.html', context)

def non_approved_students_view(request):
    return render(request, 'student_wait_for_approval.html')