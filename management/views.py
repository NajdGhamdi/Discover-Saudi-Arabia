from django.http import HttpResponse
from django.shortcuts import render
from destination.models import *
from .forms import EventForm,DestinationForm,SiteForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.


#Start of Destination-Views-Fucntions Section

def destlist_view(request):
    if request.user.is_superuser:
        dest_list=Destination.objects.all()
        context={"All_Destinations_Var":dest_list}
        return render(request,'management/dest_list.html',context)
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")




def showdest_view(request,slug):
    if request.user.is_superuser:
        dest_show=Destination.objects.get(slug=slug)
        context={"Destination_Var":dest_show}
        return render(request,'management/dest_show.html',context)
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")



def createdest_view(request):
    if request.user.is_superuser:
        if request.method=="POST":
            form=DestinationForm(request.POST,request.FILES)
            if form.is_valid():
                myform=form.save(commit=False)
                myform.owner=request.user
                myform.save()
                form=DestinationForm() #this line is for clear all form fields after submitting
                return redirect(reverse('management:destlist_view'))
        else:
            form=DestinationForm()
        return render(request,'management/dest_create.html',{'dest_form':form})
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")


def updatedest_view(request,slug):
    if request.user.is_superuser:
        dest=Destination.objects.get(slug=slug)
        if request.method=="POST":
            form=DestinationForm(request.POST,request.FILES,instance=dest)
            if form.is_valid():
                myform=form.save(commit=False)
                myform.owner=request.user
                myform.save()
                form=DestinationForm() #this line is for clear all form fields after submitting
                return redirect(reverse('management:destlist_view'))
        else:
            form=DestinationForm(instance=dest)

        return render(request,'management/dest_update.html',{"updatedest_form":form,"Destination_Var":dest})
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")


def deletedest_view(request,slug):
    if request.user.is_superuser:
        dest=Destination.objects.get(slug=slug)
        dest.delete()
        messages.success(request,("Destination Deleted Successfully!"))
        return redirect(reverse('management:destlist_view'))
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")
    

#END Of Destination-Views-Fucntions Section

##################################


# Start of Site-Views-Fucntions Section



def sitelist_view(request):
    if request.user.is_superuser:
        site_list=Site.objects.all()
        context={"All_Sites_Var":site_list}
        return render(request,'management/site_list.html',context)




def showsite_view(request,slug):
    if request.user.is_superuser:
        site_show=Site.objects.get(slug=slug)
        context={"Site_Var":site_show}
        return render(request,'management/site_show.html',context)
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")


def createsite_view(request):
    if request.user.is_superuser:
        if request.method=="POST":
            form=SiteForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                form=SiteForm() #this line is for clear all form fields after submitting
                return redirect(reverse('management:sitelist_view'))
        else:
            form=SiteForm()
        return render(request,'management/site_create.html',{'site_form':form})
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")


def updatesite_view(request,slug):
    if request.user.is_superuser:
        site=Site.objects.get(slug=slug)
        if request.method=="POST":
            form=SiteForm(request.POST,request.FILES,instance=site)
            if form.is_valid():
                form.save()
                form=SiteForm() #this line is for clear all form fields after submitting
                return redirect(reverse('management:sitelist_view'))
        else:
            form=SiteForm(instance=site)

        return render(request,'management/site_update.html',{"updatesite_form":form,"Site_Var":site})
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")
  

def deletesite_view(request,slug):
    if request.user.is_superuser:
        site=Site.objects.get(slug=slug)
        site.delete()
        messages.success(request,("Site Deleted Successfully!"))
        return redirect(reverse('management:sitelist_view'))
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")    


#END Of Site-Views-Fucntions Section



####################################################################




# Start of Event-Views-Fucntions Section



def eventlist_view(request):
    if request.user.is_superuser:
        event_list=Event.objects.all()
        context={"All_Events_Var":event_list}
        return render(request,'management/event_list.html',context)
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")



def showevent_view(request,slug):
    if request.user.is_superuser:
        event_show=Event.objects.get(slug=slug)
        context={"Event_Var":event_show}
        return render(request,'management/event_show.html',context)
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")


def createevent_view(request):
    if request.user.is_superuser:
        if request.method=="POST":
            form=EventForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                form=EventForm() #this line is for clear all form fields after submitting
                return redirect(reverse('management:eventlist_view'))
        else:
            form=EventForm()
        return render(request,'management/event_create.html',{'event_form':form})
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")


def updateevent_view(request,slug):
    if request.user.is_superuser:
        event=Event.objects.get(slug=slug)
        if request.method=="POST":
            form=EventForm(request.POST,request.FILES,instance=event)
            if form.is_valid():
                form.save()
                form=EventForm() #this line is for clear all form fields after submitting
                return redirect(reverse('management:eventlist_view'))
        else:
            form=EventForm(instance=event)

        return render(request,'management/event_update.html',{"updateevent_form":form,"Event_Var":event})
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")


def deleteevent_view(request,slug):
    if request.user.is_superuser:
        event=Event.objects.get(slug=slug)
        event.delete()
        messages.success(request,("Event Deleted Successfully!"))
        return redirect(reverse('management:eventlist_view'))
    else:
        return HttpResponse("<h1>You are Not Authorized To Access Here</h1>")       


#END Of Event-Views-Fucntions Section