from django.shortcuts import render
from admissions.models import *
from admissions.forms import studentmodelform,vendorform
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

#function based views
@login_required
def homepage(request):
    return render(request,'index.html')


def logoutuser(request):
    return render(request,'logout.html')

@login_required
def addadmission(request):
    form = studentmodelform
    studentform = {'form':form}

    if request.method=='POST':
        form=studentmodelform(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)

    return render(request,'admissions/add-addmission.html',studentform)
@login_required
def admissionsreport(request):

    result = Student.objects.all()

    students = {'allstudents':result}

    return render(request,'admissions/admissionreport.html',students)



def addvendor(request):
    form = vendorform
    studentform = {'form':form}

    if request.method=='POST':
        form=vendorform(request.POST)
        if form.is_valid():
            n=form.cleaned_data['name']
            a=form.cleaned_data['address']
            c=form.cleaned_data['contact']
            i=form.cleaned_data['item']

            response=render(request,'index.html')
            response.set_cookie('name',n)
            response.set_cookie('address',a)
            response.set_cookie('contact',c)
            response.set_cookie('item',i)
        return response

        return homepage(request)

    return render(request,'vendorr.html',studentform)

@login_required
@permission_required('admissions.delete_student')
def deletestudent(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return admissionsreport(request)


@login_required
@permission_required('admissions.change_student')
def updatetable(request,id):
    s=Student.objects.get(id=id)
    form=studentmodelform(instance=s)

    if request.method=='POST':
        form=studentmodelform(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return admissionsreport(request)



    dict={'form':form}
    return render(request,"admissions/update.html",dict)



class FirstClassView(View):
    def get(self,request):
        return HttpResponse("<h1>This is my first class based view</h1>")


class teacherread(ListView):
    model = teacher


class teacherread1(DetailView):
    model = teacher


class teachercreate(CreateView):
    model=teacher
    fields=('name','exp','subject','contact')

class teacherupdate(UpdateView):
    model=teacher
    fields=('subject','contact')


class deleteteacher(DeleteView):
    model=teacher
    success_url=reverse_lazy('teach')
