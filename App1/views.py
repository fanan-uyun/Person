from django.shortcuts import render,redirect
from App1 import models
# Create your views here.

def add_person(request):
    if request.method == 'POST':
        # 2.获取表单提交过来的内容
        username = request.POST.get('username')
        age = request.POST.get('age')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        birthday = request.POST.get('birthday')
        print(username,age,height,weight,birthday)
        # 3.保存至数据库
        models.Person.objects.create(
            name = username,
            age = age,
            height = height,
            weight = weight,
            birthday = birthday
        )
        # 4.返回一句提示操作成功的语句
        # return HttpResponse("提交成功。。。。")
        return redirect("/all_person/")
    else:
        # 1.如果是get请求，则返回页面
        return render(request, "add_person.html")

# 查询数据库，并返回至页面
def all_person(request):
    person_obj_list = models.Person.objects.all()
    # print(person_obj_list)
    # < QuerySet[ < Person: < obj：name: 姚锌 >>, < Person: < obj：name: 祥和 >>] >
    # return HttpResponse("查询成功")
    return render(request,"all_person.html",locals())

# 删除用户
def delete_person(request):
    # 获取id(获取的get请求参数当中的id值) #/delete_person/?id=2
    id = request.GET.get('id')
    models.Person.objects.get(id=id).delete()
    # print(id)
    # return HttpResponse("删除成功")
    # 删除完成后重定向到查询页面
    return redirect("/all_person/")

# 修改信息
def update_person(request):
    # 如果通过点击‘修改’链接（get方式），就重新返回一个加载页面（加载要修改记录的默认数据）
    if request.method == 'GET':
        # 获取id
        id = request.GET.get('id')
        # 查询数据库，获取对应数据对象
        person_obj = models.Person.objects.get(id=id)
        print(person_obj)
        # 返回修改页面
        return render(request,"update_person.html",{"person_obj":person_obj})

    # 否则通过加载页面，进行‘修改’按钮提交（post方式），进行数据修改操作
    else:
        # 获取表单提交过来的内容
        username = request.POST.get('username')
        age = request.POST.get('age')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        birthday = request.POST.get('birthday')
        id = request.POST.get('id')
        # 查询数据库进行修改
        person_obj = models.Person.objects.get(id=id) # 通过id获取对应数据对象
        person_obj.name = username
        person_obj.age = age
        person_obj.height = height
        person_obj.weight = weight
        person_obj.birthday = birthday
        person_obj.save() # 保存修改，提交数据库
        return redirect("/all_person/")

        # models.Person.objects.update(
        #     name = request.POST.get('username'),
        #     age = request.POST.get('age'),
        #     height= request.POST.get('height'),
        #     weight= request.POST.get('weight'),
        #     birthday=request.POST.get('birthday')
        # )
        # return redirect("/all_person/")


