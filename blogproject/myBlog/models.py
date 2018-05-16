from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.
#分类
class Category(models.Model):
    '''
    Django要求模型必须继承models.Model类。

    '''
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
#标签
class Tag(models.Model):
    name=models.CharField(max_length=70)
    def __str__(self):
        return self.name
class  Post(models.Model):
    #文章标题
    title=models.CharField(max_length=70)

    #文章正文 大段文本使用CharField，但对于文章的正文来说可能会是一大段文本
    body=models.TextField()

    #文章创建的时间和最后一次修改的时间
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()

    #文章摘要，可以没有文章摘要，但默认情况下CharField要求我们必须存入数据
    #指定CharField 的blank=True 参数值后就可以允许空值了
    excrpt=models.CharField(max_length=200,blank=True)


    #
    category=models.ForeignKey(Category)
    tags=models.ManyToManyField(Tag,blank=True)

    #文章作者，这里User是从django.contrib.auth.models动人
    #django.contrib.auth是Django内置的应用专门用于处理网站用户的注册，登录等流程
    #User
    author=models.ForeignKey(User)

    def __str__(self):
        return self.title
    '''
    reverse函数第1个参数的值是'myBlog:detail'意思是myBlog应用下的name=detail函数
    我们在urls.py中通过app_name='blog'告诉Django这个URL模块是属于myBlog应用的,因此Django能够顺利地找到blog应用下的name为detail的视图函数
    '''
    def get_absolute_url(self):
        return reverse('myBlog:detail',kwargs={'pk':self.pk})
    class Meta:
        ordering=['-created_time']