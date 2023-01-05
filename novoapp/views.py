from django.shortcuts import render, redirect
from .forms import ContactUs
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

def homePage(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftmenu = LeftMenu.objects.all()
    latestitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact =LeftContact.objects.all()
    homebackground = HomeBackground.objects.all()
    creativetitle =  Creativestitle.objects.all()
    creative =  Creative.objects.all()
    clientlogo = ClientsLogo.objects.all()
    clientlightlogo = ClientlightLogo.objects.all()
    footer = Footer.objects.all()



    return render (request,'app/home.html',
        {
            'navlogo':navlogo,
            'navlogoimg':navlogoimg,
            'navitems':navitems,
            'navsubitems':navsubitems,
            'leftmenu':leftmenu,
            'latestitle':latestitle,
            'lastestpicture':lastestpicture,
            'leftcontact':leftcontact,
            'homebackground':homebackground,
            'creativetitle':creativetitle,
            'creative':creative,
            'clientlogo':clientlogo,
            'clientlightlogo':clientlightlogo,
            'footer':footer,
        }
    
    )


def blog(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftmenu = LeftMenu.objects.all()
    latestitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact =LeftContact.objects.all()
    clientlogo = ClientsLogo.objects.all()
    clientlightlogo = ClientlightLogo.objects.all()
    footer = Footer.objects.all()
    return render (request,'app/blog.html',
    {   
            'navlogo':navlogo,
            'navlogoimg':navlogoimg,
            'navitems':navitems,
            'navsubitems':navsubitems,
            'leftmenu':leftmenu,
            'clientlogo':clientlogo,
            'clientlightlogo':clientlightlogo,
            'latestitle':latestitle,
            'lastestpicture':lastestpicture,
            'leftcontact':leftcontact,
            'footer':footer,
    })



def services(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftmenu = LeftMenu.objects.all()
    latestitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact =LeftContact.objects.all()
    mainservicetitle = MainServicesTitle.objects.all()
    mainservice = OurCompleteService.objects.all()
    clientlogo = ClientsLogo.objects.all()
    clientlightlogo = ClientlightLogo.objects.all()
    footer = Footer.objects.all()
    
 
    return render(request,'app/services.html',
    {
        'navlogo':navlogo,
        'navlogoimg':navlogoimg,
        'navitems':navitems,
        'navsubitems':navsubitems,
        'leftmenu':leftmenu,
        'latestitle':latestitle,
        'lastestpicture':lastestpicture,
        'leftcontact':leftcontact,
        "mainservicetitle":mainservicetitle,
        "mainservice":mainservice,
        'clientlogo':clientlogo,
        'clientlightlogo':clientlightlogo,
        'footer':footer,
    })


def aboutus(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftmenu = LeftMenu.objects.all()
    latestitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact =LeftContact.objects.all()
    aboutsec_1 = AboutSection.objects.all()
    myskills = MySkills.objects.all()
    whychooseme = WhyChooseU.objects.all()
    clientlogo = ClientsLogo.objects.all()
    clientlightlogo = ClientlightLogo.objects.all()
    footer = Footer.objects.all()

    
    return render(request,'app/aboutus.html',
    {
        'navlogo':navlogo,
        'navlogoimg':navlogoimg,
        'navitems':navitems,
        'navsubitems':navsubitems,
        'leftmenu':leftmenu,
        'latestitle':latestitle,
        'lastestpicture':lastestpicture,
        'leftcontact':leftcontact,
        "aboutsec_1":aboutsec_1,
        "myskills":myskills,
        "whychooseme":whychooseme,
        'clientlogo':clientlogo,
        'clientlightlogo':clientlightlogo,
        'footer':footer,
    })

def contactus(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftmenu = LeftMenu.objects.all()
    latestitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact =LeftContact.objects.all()
    contactus = Contactu.objects.all()
    clientlogo = ClientsLogo.objects.all()
    clientlightlogo = ClientlightLogo.objects.all()
    footer = Footer.objects.all()
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactForm(yourName=yn,email=em,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()     
            return redirect ('/thankyou/')
    else:
        form = ContactUs()
   
    return render(request,'app/contact.html',
    {
        'navlogo':navlogo,
        'navlogoimg':navlogoimg,
        'navitems':navitems,
        'navsubitems':navsubitems,
        'leftmenu':leftmenu,
        'latestitle':latestitle,
        'lastestpicture':lastestpicture,
        'leftcontact':leftcontact,
        'form':form,
        'clientlogo':clientlogo,
        'contactus':contactus,
        'clientlightlogo':clientlightlogo,
        'footer':footer,
    })



def thanks(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftmenu = LeftMenu.objects.all()
    latestitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact =LeftContact.objects.all()
    clientlogo = ClientsLogo.objects.all()
    clientlightlogo = ClientlightLogo.objects.all()
    footer = Footer.objects.all()

    
    return render(request,'app/thanks.html',
    {
        'navlogo':navlogo,
        'navlogoimg':navlogoimg,
        'navitems':navitems,
        'navsubitems':navsubitems,
        'leftmenu':leftmenu,
        'latestitle':latestitle,
        'lastestpicture':lastestpicture,
        'leftcontact':leftcontact,
        'clientlogo':clientlogo,
        'clientlightlogo':clientlightlogo,
        'footer':footer,
    })


def portfolio(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftmenu = LeftMenu.objects.all()
    latestitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact =LeftContact.objects.all()
    clientlogo = ClientsLogo.objects.all()
    clientlightlogo = ClientlightLogo.objects.all()
    footer = Footer.objects.all()

    
    return render(request,'app/portfolio.html',
    {
        'navlogo':navlogo,
        'navlogoimg':navlogoimg,
        'navitems':navitems,
        'navsubitems':navsubitems,
        'leftmenu':leftmenu,
        'latestitle':latestitle,
        'lastestpicture':lastestpicture,
        'leftcontact':leftcontact,
        'clientlogo':clientlogo,
        'clientlightlogo':clientlightlogo,
        'footer':footer,
    })