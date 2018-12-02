from django.contrib import admin
from shuoming.models import ClassRoom,Teacher,Student
# Register your models here.

# 修改网页样式
admin.site.site_header = '孙彬沙雕站头'
admin.site.site_title = '这是标语'
admin.site.index_title = '这是我弄的学校'

#创建管理模型的类
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ["roomName","cTime"]

class TeacherAdmin(admin.ModelAdmin):
    list_display = ["teacherName","course"] # 列表里需要显示的东西
    fields = ["teacherName","teacher"] # 具体人物查看页面需要显示的东西

class StudentAdmin(admin.ModelAdmin):
    list_per_page = 2  # 显示一页数据显示的数量
    list_display = ["studentName","age","getClassName"]
    search_fields = ["studentName"] # 搜索框
    fieldsets = (
        ("基本信息",{"fields":["studentName","age"]}),
        ("其他信息",{"fields":["student",]}),
    ) # 具体页面的分组

admin.site.register(ClassRoom,ClassRoomAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
# admin.site.register(ClassRoom)
# admin.site.register(Teacher)
# admin.site.register(Student)