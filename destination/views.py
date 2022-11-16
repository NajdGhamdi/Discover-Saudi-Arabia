from django.shortcuts import render,redirect
from .models import Destination,Site,Event,Comment
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.contrib import messages
# Create your views here.

def destination_list_view(request):
    destination_list=Destination.objects.all()
    site_list=Site.objects.all()
    context={'Destinations_list_Var':destination_list,'Sites_list_Var':site_list}
    return render(request,'destinations/destination_list.html',context)


def destination_detail_view(request,slug):
    destination_detail=Destination.objects.get(slug=slug)
    destination_list=Destination.objects.all()
    event_list=Event.objects.all()
    site_list=Site.objects.all()
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.destination=destination_detail
            myform.username=str(request.user)
            myform.email=str(request.user.email)
            myform.author=request.user
            myform.save()
            return redirect('destination:destination_detail_view',slug=slug)
            form=CommentForm() 
            print('Succesfully Submit')
    else:
        form=CommentForm()

    context={'Destination_detail_Var':destination_detail,'Destinations_list_Var':destination_list,'Sites_list_Var':site_list,'Events_list_Var':event_list,'CommentForm':form}
    return render(request,'destinations/destination_detail.html',context)
    



def site_detail_view(request,slug):
    site_detail=Site.objects.get(slug=slug)
    context={'Site_detail_Var':site_detail}
    return render(request,'destinations/site_detail.html',context)




def event_detail_view(request,slug):
    event_detail=Event.objects.get(slug=slug)
    context={'Event_detail_Var':event_detail}
    return render(request,'destinations/event_detail.html',context)






def delete_comment_view(request,id):
    comment=Comment.objects.get(id=id)
    if request.user==comment.author or request.user.is_superuser:
        comment.delete()
        messages.success(request,("Comment Deleted Successfully!"))
        return redirect('destination:destination_list_view')
         
    else:
        messages.success(request,("You Aren't Authorized To Delete this Comment!!")) 
        return redirect('destination:destination_list_view')

