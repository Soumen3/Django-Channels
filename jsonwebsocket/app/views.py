from django.shortcuts import render
from .models import Chat,Group


# Create your views here.
def index(request, group_name):
    context={'group_name':group_name}
    group=Group.objects.filter(name=group_name).first()
    print("The group is ",group)

    if group:
        chat=Chat.objects.filter(group=group)
        context['chats']=chat
    else:
        Group(name=group_name).save()
    return render(request, 'index.html', context)