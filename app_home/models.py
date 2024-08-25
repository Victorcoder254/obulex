from django.db import models
from django.utils import timezone

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=255, blank=True, null=True)
    visit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Visitor {self.ip_address} on {self.visit_date}"
    
class service(models.Model):
    name_1 = models.CharField(max_length=100, blank=True, null=True) 
    description_1 = models.CharField(max_length=150, blank=True, null=True)  
    name_2 = models.CharField(max_length=100, blank=True, null=True) 
    description_2 = models.CharField(max_length=150, blank=True, null=True) 
    name_3 = models.CharField(max_length=100, blank=True, null=True) 
    description_3 = models.CharField(max_length=150, blank=True, null=True) 
    name_4 = models.CharField(max_length=100, blank=True, null=True) 
    description_4 = models.CharField(max_length=150, blank=True, null=True)   
    last_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Last Edited {self.last_edited}"
    
class about_us(models.Model):
    year_1 = models.CharField(max_length=100, blank=True, null=True)
    sub_heading_1 = models.CharField(max_length=100, blank=True, null=True)  
    description_1 = models.CharField(max_length=350, blank=True, null=True)    
    year_2 = models.CharField(max_length=100, blank=True, null=True)
    sub_heading_2 = models.CharField(max_length=100, blank=True, null=True)  
    description_2 = models.CharField(max_length=350, blank=True, null=True)  
    year_3 = models.CharField(max_length=100, blank=True, null=True)
    sub_heading_3 = models.CharField(max_length=100, blank=True, null=True)  
    description_3 = models.CharField(max_length=350, blank=True, null=True)  
    year_4 = models.CharField(max_length=100, blank=True, null=True)
    sub_heading_4 = models.CharField(max_length=100, blank=True, null=True)  
    description_4 = models.CharField(max_length=350, blank=True, null=True)  
    last_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Last Edited {self.last_edited}"
    
class projects(models.Model):   
    project_name_1 = models.CharField(max_length=100, blank=True, null=True)
    brief_1 = models.CharField(max_length=150, blank=True, null=True)  
    description_1 = models.CharField(max_length=500, blank=True, null=True)    
    project_name_2 = models.CharField(max_length=100, blank=True, null=True)
    brief_2 = models.CharField(max_length=150, blank=True, null=True)  
    description_2 = models.CharField(max_length=500, blank=True, null=True)  
    project_name_3 = models.CharField(max_length=100, blank=True, null=True)
    brief_3 = models.CharField(max_length=150, blank=True, null=True)  
    description_3 = models.CharField(max_length=500, blank=True, null=True)  
    last_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Last Edited {self.last_edited}" 
    
class Team(models.Model):
    name_1 = models.CharField(max_length=100, blank=True, null=True)
    title_1 = models.CharField(max_length=150, blank=True, null=True)  
    twitter_1 = models.URLField(max_length=500, blank=True, null=True)   
    facebook_1 = models.URLField(max_length=500, blank=True, null=True)  
    linkedin_1 = models.URLField(max_length=500, blank=True, null=True)   

    name_2 = models.CharField(max_length=100, blank=True, null=True)
    title_2 = models.CharField(max_length=150, blank=True, null=True)  
    twitter_2 = models.URLField(max_length=500, blank=True, null=True)   
    facebook_2 = models.URLField(max_length=500, blank=True, null=True)  
    linkedin_2 = models.URLField(max_length=500, blank=True, null=True)   

    name_3 = models.CharField(max_length=100, blank=True, null=True)
    title_3 = models.CharField(max_length=150, blank=True, null=True)  
    twitter_3 = models.URLField(max_length=500, blank=True, null=True)   
    facebook_3 = models.URLField(max_length=500, blank=True, null=True)  
    linkedin_3 = models.URLField(max_length=500, blank=True, null=True)   

    last_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Last Edited {self.last_edited}"  
    

# Model for the contact information section
class FooterContactInfo(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    twitter = models.URLField(max_length=500, blank=True, null=True)   
    facebook = models.URLField(max_length=500, blank=True, null=True)  
    linkedin = models.URLField(max_length=500, blank=True, null=True)  
    
    termsofservice = models.CharField(max_length=1000, blank=True, null=True)  
    privacypolicy = models.CharField(max_length=1000, blank=True, null=True) 

    def __str__(self):
        return "Footer Contact Information"