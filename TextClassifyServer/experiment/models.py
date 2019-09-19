from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class text(models.Model):
        id = models.IntegerField(u'编号',primary_key=True)
        label = models.IntegerField(u'标记')
        content = models.TextField(u'正文')
            
        def status(self):
            if self.label == 0:
                ret = '正常信息'
                color_code = 'green'
            else:
                ret = '垃圾信息'
                color_code = 'red'
            return format_html(
                '<span style="color: {};">{}</span>',
                color_code,
                ret,
            )
        
        status.short_description = u'状态'

        class Meta:
                verbose_name_plural='有标签数据'
                ordering = ['-id']

        def __unicode__(self):
                return self.id

class unlabel_data(models.Model):
        id = models.IntegerField(u'编号',primary_key=True)
        svm = models.BooleanField(u'SVM')
        lr = models.BooleanField(u'LR')
        dt = models.BooleanField(u'DT')
        lgbm = models.BooleanField(u'LGBM')
        content = models.TextField(u'正文')

        class Meta:
                verbose_name_plural='无标签数据'
                ordering = ['-id']

        def __unicode__(self):
                return self.id
