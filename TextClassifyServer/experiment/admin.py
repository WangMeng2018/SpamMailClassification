from django.contrib import admin
from django.contrib.auth.models import Group, User
from experiment.models import *

# Register your models here.
class TextAdmin(admin.ModelAdmin):
	list_display = ('id','label','content','status',)
	search_fields = ('content',)
	#list_editable = ('theme','label','entity',)
	#list_filter = ('status',)

class Unlabel_dataAdmin(admin.ModelAdmin):
	list_display = ('id','svm','lr','dt','lgbm','content',)
	search_fields = ('content',)

admin.site.site_header = '垃圾信息分类'
admin.site.site_title = '网络数据挖掘'
admin.site.register(text,TextAdmin)
admin.site.register(unlabel_data,Unlabel_dataAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
