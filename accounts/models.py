from django.db import models
from lookup.models import lookup
from django_userforeignkey.models.fields import UserForeignKey
from django.contrib.auth.models import User
# Create your models here.
class User_reg(models.Model):
    name = models.CharField("name",max_length=500, blank=True, null=True)
    usertype = models.ForeignKey(lookup,on_delete=models.CASCADE,related_name='lookup_fk_usertype',blank=True, null=True, default=None) 
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True, default=None) 
    created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated = models.DateTimeField(auto_now=True,blank=True, null=True)
    created_by = UserForeignKey(auto_user_add=True, verbose_name="The user that is automatically assigned", related_name="user_reg_created_by_user")
    updated_by = UserForeignKey(auto_user=True, verbose_name="The user that is automatically assigned", related_name="user_reg_updated_by_user")
    class Meta:
        db_table = "user_reg"
    def __str__(self):
        return "%s " % (self.name)