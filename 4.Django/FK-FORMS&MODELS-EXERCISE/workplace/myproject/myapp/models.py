from django.db import models

# Create your models here.
#Menu category
class MenuCategory(models.Model):
    menu_category_name = models.CharField (max_length=200)

#Menu
class Menu(models.Model):
    menu_item =  models.CharField(max_length=200)
    price = models.IntegerField(null = False)
    category =models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")
    
    def __str__(self):
        return  self.menu_item

class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)    
    time_log = models.TimeField(help_text="Enter the exact time")