from django.db import models



class Slider(models.Model):
    image = models.ImageField(upload_to='media/slider')

    def __str__(self):
        return str(self.image)

class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/service')

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/category', blank=True, null=True)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/sub_category', blank=True, null=True)
    discription = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.category.name + " | " + self.title 