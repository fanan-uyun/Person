from django.db import models

# Create your models here.
# 用户模型类
class Person(models.Model):
    # AutoField 指一个能够根据可用ID自增的 IntegerField
    id = models.AutoField(primary_key=True)

    # 字符串字段，适用于中小长度的字符串
    name = models.CharField(max_length=24)

    # IntegerField 整数
    age = models.IntegerField()

    # DecimalField 表示固定精度的十进制数的字段。它有两个必须的参数：
        # DecimalField.max_digits：数字允许的最大位数
        # DecimalField.decimal_places：小数的最大位数
    height = models.DecimalField(max_digits=5,decimal_places=2)

    # FloatField    浮点数字段
    weight = models.FloatField()

    # DateField 日期字段
    birthday = models.DateField()

    def __str__(self):
        return "<obj：name:{}>".format(self.name)
