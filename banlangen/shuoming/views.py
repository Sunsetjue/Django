from django.shortcuts import render

# Create your views here.
def sess(request):
    print(type(request.session))
    print(request.session)
    # 如果session中没有teacher_name的值，则返回NoName
    print(request.session.get('teacher_name','NoName'))
    return None