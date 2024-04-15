from django.contrib import admin
from .models import Chat,Group

# Register your models here.

#------------By default all fields will be visible in django admin interface----------#
# admin.site.register(Chat)
# admin.site.register(Group)


# ------------To view only the listed columns------------#
@admin.register(Chat)
class ChatModelAdmin(admin.ModelAdmin):
    list_display=['id', 'content', 'timestamp', 'group']
@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display=['id','name']

# admin.site.register(Chat, ChatModelAdmin)
# admin.site.register(Group, GroupModelAdmin)
