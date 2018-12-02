from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=4)#输入字符串类型，并且至少有一个类型限制
    age = models.IntegerField()#输入整数类型
    address = models.CharField(max_length=50)#限制字符串的最大长度为50
    course = models.CharField(max_length=20)
    def __str__(self):
        return self.name
