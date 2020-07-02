from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView, DetailView


def signup(request):
    if request.method=='POST':
        name =request.POST['name'],
        address = request.POST['address'],
        salary = request.POST['salary'],


        x=User.objects.create_user(name=name,address=address,salary=salary)
        x.save()
        print("user created")
        return redirect('/')
    else:
          return render(request,'b.html')
# Create your views here.
#Update Employee
class EmployeeUpdate(UpdateView):
    fields = ['address','salary']
    template_name = 'templates/employee_update.html'

    def get_object(self):
        return self.request.user.employee


class EmployeeProfile(DetailView):
    template_name = 'templates/employee.html'

    def get_object(self):
        return self.request.user.employee
#delete Employee

def employee_delete(request,id=None):
    user = get_object_or_404(User,id=id)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('signup'))
    else:
        context = {}
        context['user'] = user
        return render(request,'employee deleted')

