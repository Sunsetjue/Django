from django.db import models

# Create your models here.
class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)
    school_address = models.CharField(max_length=30)
    def __str__(self):
        return self.school_name

class Manage(models.Model):
    manage_id = models.IntegerField()
    manage_name = models.CharField(max_length=4)
    manage_age = models.IntegerField()
    my_school = models.OneToOneField(School)#管理者和学习一对一，一个学校对应一个管理者
    def __str__(self):
        return self.manage_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=4)
    teacher_age = models.IntegerField()
    teacher_gender = models.CharField(max_length=1)
    teacher = models.ForeignKey(School)#学习和老师一对多，一个学校可以有很多老师，但老师只能在一个学校
    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_name = models.CharField(max_length=4)
    student = models.ManyToManyField(Teacher)
    def __str__(self):
        return self.student_name
