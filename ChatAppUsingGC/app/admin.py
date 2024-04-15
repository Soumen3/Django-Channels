from django.contrib import admin
from .models import Chat, Group
# Register your models here.


"""each object will visible as a object,
after clicking the object we can see the content"""
# admin.site.register(Chat)
# admin.site.register(Group)


# ------------To view only the listed columns------------#
@admin.register(Chat)
class ChatModelAdmin(admin.ModelAdmin):
    list_display=['id', 'content', 'timestamp', 'group']
@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display=['id','name']


#---------------If decorator is not used with the above class, use this method-------------#
# admin.site.register(Chat, ChatModelAdmin)
# admin.site.register(Group, GroupModelAdmin)
