from django.shortcuts import render,get_object_or_404,redirect
from myBlog.models import Post

# Create your views here.
from .models import Comment
from .forms import CommentForm

def post_comment(request,post_pk):
    #先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来
    #这里我们使用Django提供了一个快捷函数get_object_or_404
    #这个函数的作用是当获取的文章(Post)存在时，则获取，否则返回404页面给用户
    post=get_object_or_404(Post,pk=post_pk)
    #HTTP请求有get和post两种，一般用户通过表单提交数据都是通过post请求
    if request.method=='POST':
        #用户提交的数据存在request.POST中,这是一个类字典对象
        #我们利用这些数据构造了CommentForm的实例,生成Django表单
        form=CommentForm(request.POST)

        if form.is_valid():
            #检查到数据是合法的，调用表单的save方法保存数据到数据库
            #commit=False的作用是仅仅利用表单的数据生成Comment模型类的实例，但还不保存评论数据到数据库
            comment=form.save(commit=False)

            #将评论和被评论的文章关联起来
            comment.post=post
            #最终将评论数据保存进数据库，调用模型实例的save方法
            comment.save()
            #重定向到post的详情页，实际上当redirect函数接收到一个模型的实例时
            #它会调用这个模型实例的get_absolute_url方法
            return redirect(post)

        else:
            #检查到数据不合法，重新渲染详情页，并且渲染表单的错误
            #文章(post),一个是评论列表,一个是表单form


            comment_list=post.comment_set.all()
            context={
            'post':post,
            'form':form,
            'comment_list':comment_list,

            }

            return render(request,'myBlog/detail.html',context=context)

    return redirect(post)