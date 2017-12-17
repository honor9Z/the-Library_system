from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if not request.user.is_authenticated():
        return redirect("/login/")
    return render(request,'index.html')

def book(request):
    if not request.user.is_authenticated():
        return redirect("/login/")


    booklist=models.Book.objects.all()
    authorlist=models.Book.objects.filter()
    return render(request,'book.html',{'booklist':booklist})

def delbook(request,id):
    if not request.user.is_authenticated():
        return redirect("/login/")


    models.Book.objects.filter(nid=id).delete()
    return redirect('/book/')

def edit(request):
    # if not request.user.is_authenticated():
    #     return redirect("/login/")


    # publist=models.Publish.objects.all()
    # authorlist=models.Author.objects.all()
    if request.method=="POST":
        id=request.POST.get("nid")

        title=request.POST.get("title")
        authorlist=request.POST.getlist("authorlist")
        price=request.POST.get("price")
        pubdate=request.POST.get("pubdate")
        publish_id=request.POST.get("publish")
        print('========================',authorlist)#['1','2']


        authors = models.Author.objects.filter(id__in=authorlist)

        edit_book=models.Book.objects.filter(nid=id).update(title=title,price=price,publish_date=pubdate,publish_id=publish_id)
        p=models.Book.objects.get(nid=id)
        p.authorlist=authors
        p.save()
        return redirect("/book/")

    id = request.GET.get("book_id")
    publist=models.Publish.objects.all()
    authorlist=models.Author.objects.all()

    edit_book=models.Book.objects.filter(nid=id)[0]  #    [obj1,]
    edit_book_authors = edit_book.authorlist.all().values_list("id")
    print(edit_book_authors)
    l = []

    for i in edit_book_authors:
        l.append(i[0])  # [2,3]
    return render(request,"edit.html",locals())


def addbook(request):
    if not request.user.is_authenticated():
        return redirect("/login/")


    publist=models.Publish.objects.all()
    authorlist=models.Author.objects.all()
    if request.method=="POST":
        title=request.POST.get("title")
        authorlist=request.POST.getlist("authorlist")
        price = request.POST.get("price")
        pubdate=request.POST.get("pubdate")
        publish_id=request.POST.get("publish")
        print('========================',authorlist)
        book_obj=models.Book.objects.create(title=title,price=price,publish_date=pubdate,publish_id=publish_id)
        authors = models.Author.objects.filter(id__in=authorlist)
        print('++++++++++++',authors)
        book_obj.authorlist.add(*authors)

        print(book_obj.title,book_obj.nid)


        return redirect("/book/")
    publishlist = models.Publish.objects.all()
    authorlist = models.Author.objects.all()
    return render(request,"addBook.html",locals())


def author(request):
    if not request.user.is_authenticated():
        return redirect("/login/")


    authorlist=models.Author.objects.all()
    return render(request,'author.html',{'authorlist':authorlist})


def delauthor(request,id):
    models.Author.objects.filter(id=id).delete()
    return redirect('/author/')

def editauthor(request):
    if not request.user.is_authenticated():
        return redirect("/login/")


    if request.method=="POST":
        id=request.POST.get("id")

        # 修改方式1：save(效率低)
        # book_obj=models.Book.objects.filter(nid=id)[0]
        # book_obj.title="金平"
        # book_obj.save()

        # 修改方式2：
        name=request.POST.get("name")
        age=request.POST.get("age")


        models.Author.objects.filter(id=id).update(name=name,age=age)
        return redirect("/author/")
    # print(author_obj.id)
    id = request.GET.get("author_id")
    print("==================id",id)
    edit_author=models.Author.objects.filter(id=id)[0]  #    [obj1,]
    return render(request,"editauthor.html",{'edit_author':edit_author})



def addauthor(request):
    if not request.user.is_authenticated():
        return redirect("/login/")


    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        models.Author.objects.create(name=name,age=age)
        return redirect("/author/")
    return render(request,"addauthor.html")


def publish(request):
    if not request.user.is_authenticated():
        return redirect("/login/")


    publist=models.Publish.objects.all()
    return render(request,'publish.html',{'publist':publist})


def addpublish(request):
    if not request.user.is_authenticated():
        return redirect("/login/")


    if request.method=="POST":
        name=request.POST.get("name")
        addr=request.POST.get("addr")
        models.Publish.objects.create(name=name,addr=addr)
        return redirect("/publish/")
    return render(request,'addpublish.html')

def delpublish(request,id):
    if not request.user.is_authenticated():
        return redirect("/login/")


    models.Publish.objects.filter(id=id).delete()
    return redirect('/publish/')

def editpublish(request):
    if not request.user.is_authenticated():
        return redirect("/login/")


    if request.method=="POST":
        id=request.POST.get("id")

        # 修改方式1：save(效率低)
        # book_obj=models.Book.objects.filter(nid=id)[0]
        # book_obj.title="金平"
        # book_obj.save()

        # 修改方式2：
        name=request.POST.get("name")
        addr=request.POST.get("addr")


        models.Publish.objects.filter(id=id).update(name=name,addr=addr)
        return redirect("/publish/")
    # print(author_obj.id)
    id = request.GET.get("publish_id")
    print("==================id",id)
    edit_publish=models.Publish.objects.filter(id=id)[0]  #    [obj1,]
    return render(request,"editpublish.html",{'edit_publish':edit_publish})


def reg(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        User.objects.create_user(username=username,password=password)
        return redirect('/login/')
    return render(request,'reg.html')



def log_in(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect("/index/")
        else:
            info = "用户名或密码错误"
            return render(request, "login.html", {"info": info})
    return render(request,'login.html')


def log_out(request):
    auth.logout(request)
    return redirect("/login/")


def set_pwd(request):
    if request.method=='POST':
        old_pwd = request.POST.get("old_password")
        new_pwd = request.POST.get("new_password")
        username = request.user
        user = User.objects.get(username=username)
        #校验旧密码
        ret = user.check_password(old_pwd)#得到旧密码
        if ret:
            user.set_password(new_pwd)
            user.save()
            return redirect("/login/")
        else:
            info = "输入密码有误"
            return render(request, "set_pwd.html", {"info": info})

    return render(request,'set_pwd.html')