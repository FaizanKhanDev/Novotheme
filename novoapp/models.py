from django.db import models
from django.contrib.auth.models import User

class Navlogo(models.Model):
    navlogo = models.TextField(max_length=100)
    def __str__(self):
        return str(self.id) 

class NavLogoImage(models.Model):
    img = models.ImageField(upload_to='allimages')

# === nav main Items === #
class Navitem(models.Model):
    navitems_1 = models.CharField(max_length=20)
    navitems_2 = models.CharField(max_length=20)
    navitems_3 = models.CharField(max_length=20)
    navitems_4 = models.CharField(max_length=20)
    navitems_5 = models.CharField(max_length=20)
    navitems_6 = models.CharField(max_length=20)

# === nav main Items End === #

# === nav Subitems Items  === #

class Navsubitem(models.Model):
    navsubitem_1 = models.TextField(max_length=100)
    navsubitem_2 = models.TextField(max_length=100)
    navsubitem_3 = models.TextField(max_length=100)
    navsubitem_4 = models.TextField(max_length=100)
    navsubitem_5 = models.TextField(max_length=100)
    navsubitem_6 = models.TextField(max_length=100)

# === nav Subitems Items End === #

#=== Nav Left Slide Menu === #

class LeftMenu(models.Model):
    title = models.TextField(max_length=100)
    descriptions = models.TextField(max_length=100)
    def _str__(self):
        return self(self.id)


class Latesttitle(models.Model):
    title = models.TextField(max_length=100)
    def _str__(self):
        return self(self.id)


class LastestPicture(models.Model):
    latestImg =  models.ImageField(upload_to='allimages')
    def _str__(self):
        return self(self.id)


class LeftContact(models.Model):
    title = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    copyRight = models.TextField(max_length=100)
    def _str__(self):
        return self(self.id)

#  ==== Nav is End ==== #

# === home BackGround === #
class HomeBackground(models.Model):
    backgroundimg = models.ImageField(upload_to='allimages')
    bgtitle = models.TextField(max_length=1000)
    descriptions = models.CharField(max_length=100)
    homebtn =  models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)

        
# === home BackGround === #


# === Creative Section  === #
class Creativestitle(models.Model):
    title = models.TextField(max_length=50)
    
class Creative (models.Model):
    title1 = models.TextField(max_length=100)
    title2 = models.TextField(max_length=100)
    description1 = models.TextField(max_length=250)
    description2 = models.TextField(max_length=250)
    img = models.ImageField(upload_to='allimages')
    btn = models.TextField(max_length=20)



class MainServicesTitle(models.Model):
    title = models.CharField(max_length=50)



class OurCompleteService(models.Model):
    frontitle = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    backtitle = models.CharField(max_length=50)
    btn = models.CharField(max_length=10)



class AboutSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    subdescription = models.CharField(max_length=400)
    btn = models.CharField(max_length=10)
    img = models.ImageField(upload_to='allimages')



class MySkills(models.Model):
    img = models.ImageField(upload_to='allimages')
    title = models.CharField(max_length=100)
    skillsName1 = models.CharField(max_length=100)
    progress = models.CharField(max_length=10)
    skillsName2 = models.CharField(max_length=100)
    progress2 = models.CharField(max_length=10)
    skillsName3 = models.CharField(max_length=100)
    progress3 = models.CharField(max_length=10)
    skillsName4 = models.CharField(max_length=100)
    progress4 = models.CharField(max_length=10)
    skillsName5 = models.CharField(max_length=100)
    progress5 = models.CharField(max_length=10)
    skillsName6 = models.CharField(max_length=100)
    progress6 = models.CharField(max_length=10)
    skillsName7 = models.CharField(max_length=100)
    progress7 = models.CharField(max_length=10)
    skillsName8 = models.CharField(max_length=100)
    progress8 = models.CharField(max_length=10)
    skillsName9 = models.CharField(max_length=100)
    progress9 = models.CharField(max_length=10)



class WhyChooseU(models.Model):
    maintitle = models.CharField(max_length=100)
    subtitle1 = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    subtitle2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=100)
    subtitle3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=100)
    subtitle4 = models.CharField(max_length=100)
    description4 = models.CharField(max_length=100)
    subtitle5 = models.CharField(max_length=100)
    description5 = models.CharField(max_length=100)
    subtitle6 = models.CharField(max_length=100)
    description6 = models.CharField(max_length=100)

# ==== About Section === # 


# ====
Contact_CATEGORY_CHOICES = (
    ('seo','SEO'),
    ('WebDesign','WEBDESIGN'),
    ('Graphice Designing','GRAPHICSDESIGNING'),
    ('SocialMediaMarketing','SOCIALMEDIAMARKETING'),
    ('WebDevelopment','WEBDEVELOPMENT'),
    ('EmailMarketing','EMAILMARKETING'),
    ('ADsManagement','ADMANAGEMENT'),
    ('Animations','ANIMATIONS'),
)

# Contact Section === # 
class Contactu(models.Model):
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

class ContactForm(models.Model):
    yourName = models.TextField(max_length=50)
    email = models.EmailField()
    Phonenumber = models.CharField(max_length=20)
    Subject = models.CharField(choices=Contact_CATEGORY_CHOICES,max_length=100)
    Message = models.CharField(max_length=400)

# ==== Contact Section === # 


# ==== footer Section === # 

class ClientsLogo(models.Model):
    img = models.ImageField(upload_to='allimages')

class ClientlightLogo(models.Model):
    img = models.ImageField(upload_to='allimages')


class Footer(models.Model):
    title1 = models.TextField(max_length=50)
    description = models.CharField(max_length=200)
    title2 = models.TextField(max_length=50)
    item1 = models.TextField(max_length=20)
    item2 = models.TextField(max_length=20)
    item3 = models.TextField(max_length=20)
    item4 = models.TextField(max_length=20)
    item5 = models.TextField(max_length=20)
    item6 = models.TextField(max_length=20)
    title3 = models.TextField(max_length=50)
    phone = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    copyright = models.TextField(max_length=200)

# ==== footer Section === # 
