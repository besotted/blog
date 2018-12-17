from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class stopic(models.Model):
    sname=models.CharField(max_length=30,verbose_name=u'类别名称')
    def __str__(self):
        return u'<stopic:%s>'%self.sname
    class Meta:
        verbose_name_plural=u'类别'
class blog_type(models.Model):
    cname=models.CharField(max_length=30,verbose_name=u'标签名称')
    def __str__(self):
        return u'<types:%s>'%self.cname
    class Meta:
        verbose_name_plural=u'标签'
class postblog(models.Model):
    title=models.CharField(max_length=100,verbose_name=u'标题')
    content=RichTextUploadingField(verbose_name=u'内容')
    timedata=models.DateTimeField(auto_now_add=True,verbose_name=u'发布时间')
    stic=models.ForeignKey(stopic,verbose_name=u'所属类别')
    blg=models.ManyToManyField(blog_type,verbose_name=u'标签')
    def __str__(self):
        return u'<postlog:%s>'%self.title
    class Meta:
        verbose_name_plural=u'帖子'


