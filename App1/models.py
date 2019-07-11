from django.db import models

# Create your models here.
# 用户模型类
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    age = models.IntegerField()
    height = models.DecimalField(max_digits=5,decimal_places=2)
    weight = models.FloatField()
    birthday = models.DateField()

    def __str__(self):
        return "<obj：name:{}>".format(self.name)
