from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'
    

    def __str__(self) -> str:
        return self.name


class Image(models.Model):
    src = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



























'''
Category -> [Image]      
Image -> Category

Child -> Mother
Many -> One
Image -> Category


Person -> Head
One -> One

Service Provider -> Person
Many -> Many
'''