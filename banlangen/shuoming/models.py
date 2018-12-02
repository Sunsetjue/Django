from django.db import models
import time
# Create your models here.
class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=10)
    roomName = models.CharField(max_length=10)
    def cTime(self):
        return time.ctime()
    cTime.short_description = "当前时间"
    def __str__(self):
        return self.roomName

class Teacher(models.Model):
    teacherName = models.CharField(max_length=4)
    course = models.CharField(max_length=10)
    def __str__(self):
        return self.teacherName
    # 一个老师对应一个教室
    teacher = models.OneToOneField(ClassRoom)

class Student(models.Model):
    studentName = models.CharField(max_length=4)
    age = models.IntegerField()
    def getClassName(self):
        return self.student.roomName
    getClassName.short_description = "所在教室"
    def __str__(self):
        return self.studentName
    # 一个教室可以有很多学生 而一个学生只能在一个教室
    student = models.ForeignKey(ClassRoom)