from django.shortcuts import redirect, render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return redirect('add_show')  # Redirect after successful form submission
    else:
        fm = StudentRegistration()
    stu = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'students': stu})

# This function will delete
def delete_data(request, id):
    if request.method == "POST":
        # id = request.POST.get('id')
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('add_show')
    return render


def edit_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('add_show')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})