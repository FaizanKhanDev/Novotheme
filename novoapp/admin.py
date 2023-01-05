from django.contrib import admin
from .models import (
    Navlogo,
    NavLogoImage,
    Navitem,
    Navsubitem,
    LeftMenu,
    Latesttitle,
    LastestPicture,
    LeftContact,
    HomeBackground,
    Creativestitle,
    Creative,
    MainServicesTitle,
    OurCompleteService,
    AboutSection,
    MySkills,
    WhyChooseU,
    ContactForm,
    ClientsLogo,
    ClientlightLogo,
    Footer,
    Contactu,


)


@admin.register(Navlogo)
class NavlogoAdmin(admin.ModelAdmin):
    list_display = ['id','navlogo']

@admin.register(NavLogoImage)
class NavLogoImage(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(Navitem)
class NavitemAdmin(admin.ModelAdmin):
    list_display = ['id','navitems_1','navitems_2','navitems_3','navitems_4','navitems_5','navitems_6']


@admin.register(Navsubitem)
class NavsubitemAdmin(admin.ModelAdmin):
    list_display = ['id','navsubitem_1','navsubitem_2','navsubitem_3','navsubitem_4','navsubitem_5','navsubitem_6']


@admin.register(LeftMenu)
class LeftMenuAdmin(admin.ModelAdmin):
    list_display = ['id','title','descriptions']

@admin.register(Latesttitle)
class LatesttitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(LastestPicture)
class LastestPictureAdmin(admin.ModelAdmin):
    list_display = ['id','latestImg']

@admin.register(LeftContact)
class LeftContactAdmin(admin.ModelAdmin):
    list_display = ['id','title','phone','email','copyRight']

@admin.register(HomeBackground)
class HomeBackgroundAdmin(admin.ModelAdmin):
    list_display = ['id','backgroundimg','bgtitle','descriptions','homebtn']


@admin.register(Creative)
class CreativeAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2','description1','description2','img','btn']

@admin.register(Creativestitle)
class CreativestitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']   


@admin.register(MainServicesTitle)
class MainServicesTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(OurCompleteService)
class MainServiceAdmin(admin.ModelAdmin):
    list_display = ['id','frontitle','description','backtitle','btn']


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['id','title','subtitle','description','subdescription','btn','img']

@admin.register(MySkills)
class MySkillsAdmin(admin.ModelAdmin):
    list_display = ['id',
    'img','title','skillsName1','progress','skillsName2',
    'progress2','skillsName3','progress3',
    'skillsName4','progress4','skillsName5',
    'progress5','skillsName6','progress6',
    'skillsName7','progress7','skillsName8',
    'progress8','skillsName9','progress8']

@admin.register(WhyChooseU)
class WhyChooseUAdmin(admin.ModelAdmin):
    list_display = ['id','maintitle','subtitle1','description',
    'subtitle2','description2','subtitle3','description3','subtitle4','description4',
    'subtitle5','description5','subtitle6','description6']

@admin.register(Contactu)
class ContactuAdmin(admin.ModelAdmin):
    list_display = ['id','phone','email','location','description']

@admin.register(ContactForm)
class ContactForm(admin.ModelAdmin):
    list_display = ['id','yourName','email','Phonenumber','Subject','Message',]





@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['id','title1','description','title2','item1','item2','item3','item4','item5','item6','title3','phone','email','copyright']


@admin.register(ClientsLogo)
class ClientsLogoAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(ClientlightLogo)
class ClientlightLogoAdmin(admin.ModelAdmin):
    list_display = ['id','img']

