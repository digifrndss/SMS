from django.db import models

# Create your models here.
class lookup(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    lookupcode = models.CharField("lookupcode",max_length=30)
    lookname = models.CharField("lookname",max_length=30)    
    status = models.CharField(max_length=25,choices=STATUS_CHOICES,default='Active')
    class Meta:
        db_table = "lookup"
        verbose_name_plural = "lookup" 
    def _str_(self):
        return "%s " % (self.lookname)

class lookupdet(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    USER_CHOICES = (
        ('Other', 'Other'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
    )
    lookupdetdesc = models.CharField(max_length=200)
    lookupvalue = models.CharField(max_length=100)
    lookuplevel = models.PositiveSmallIntegerField(default=0)
    lookup = models.ForeignKey(lookup, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Active')
    user_status = models.CharField(max_length=10,choices=USER_CHOICES,default='Other')
    lookup_other_value=models.CharField("Lookup other value",max_length=50,blank=True, null=True)  
    objects = models.Manager()
    def str(self):
        return self.lookupdetdesc
    class Meta:
        ordering = ('lookupdetdesc')
    def __str__(self):
        return "%s " % (self.lookupdetdesc)
    class Meta:
        db_table = "lookupdet"
        verbose_name_plural="lookupdet"