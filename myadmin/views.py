from django.shortcuts import render,redirect
from myadmin.models import AdminLoginModel , StateModel , CityModel,CuisineModel
# Create your views here.
from myadmin.forms import StateForm ,CityForm,CuisineForm
def myadmin_login_page(request):
    return render(request,'myadmin/myadmin_login.html')

def myadmin_login(request):

    urn=request.POST.get("uname")
    pwd=request.POST.get("upassword")
    try:
        user=AdminLoginModel.objects.get(username=urn,password=pwd)
        return redirect('admin_home')
    except:
        return render(request,'myadmin/myadmin_login.html',{'error':'invalid user'})

def admin_home(request):
    return render(request,'myadmin/admin_home.html')

def  state_create(request):
    form=StateForm()
    if request.method=="POST":
        form=StateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('state_details')              
    return render(request,'myadmin/insert_state.html',{'form':form})        

def state_details(request):
    list_state=StateModel.objects.all()
    return render(request,'myadmin/details_state.html',{'list_state':list_state})

def state_delete(request,id):
    data=StateModel.objects.get(id=id)
    data.delete()
    return redirect('state_details')

def state_update(request,id):
    data=StateModel.objects.get(id=id) 
    if request.method=="POST":
        form=StateForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('state_details')
    return render(request,'myadmin/update_state.html',{'data':data})        

def  city_create(request):
    form=CityForm()
    if request.method=="POST":
        form=CityForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('city_details')              
    return render(request,'myadmin/city_insert.html',{'form':form})

def city_details(request):
    list_state=CityModel.objects.all()
    return render(request,'myadmin/city_details.html',{'list_state':list_state}) 

def city_delete(request,id):
    data=CityModel.objects.get(id=id)
    data.delete()
    return redirect('city_details')

def city_update(request,id):
    city_data=CityModel.objects.get(id=id) 
    if request.method=="POST":
        form=CityForm(request.POST,request.FILES, instance=city_data)
        if form.is_valid():
            form.save()
            return redirect('city_details')
    return render(request,'myadmin/city_update.html',{'data':city_data})    

#CuisineModel details 
def  cuisine_create(request):
    form=CuisineForm()
    if request.method=="POST":
        form=CuisineForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cuisine_details')              
    return render(request,'myadmin/insert_cuisine.html',{'form':form})        

def cuisine_details(request):
    list_state=CuisineModel.objects.all()
    return render(request,'myadmin/details_cuisine.html',{'list_state':list_state})

def cuisine_delete(request,id):
    data=CuisineModel.objects.get(id=id)
    data.delete()
    return redirect('cuisine_details')

def cuisine_update(request,id):
    data=CuisineModel.objects.get(id=id) 
    if request.method=="POST":
        form=CuisineForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('cuisine_details')
    return render(request,'myadmin/update_cuisine.html',{'data':data})       