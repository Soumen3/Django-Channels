from django.shortcuts import render
from .models import Chat,Group

# Create your views here.
def index(request, group_name):
    context={'groupname':group_name}

    # save the group in database and display the chat
    group=Group.objects.filter(name=group_name).first()
    if group:
        chat=Chat.objects.filter(group=group)
        context['chat']=chat
    else:
        Group(name=group_name).save()

    
    
    return render(request, 'index.html',context)