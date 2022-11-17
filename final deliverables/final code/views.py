
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def admin(request):
    if request.method == "POST":
        username=request.POST['Username']
        password=request.POST['password']
        users=authenticate(username=username,password=password)
        if users is not None:
            (request, users)
            users.save()
            
            return redirect('admin_page')
        return render(request, "admin.html")
    return render(request, "admin.html")


def admin_page(request):
    address=Addprodadmin.objects.all()
    lycrapants=lycrapant.objects.all()
    vestis=vesti.objects.all()
    shirts=shirt.objects.all()
    vestiandshirrtspattus=vestiandshirrtspattu.objects.all()

    response=Girlscollectionpayment.objects.all()
    smartpayment=Genscollectionpayment.objects.all()
    customermessgae=Getintough.objects.all()
    return render(request, "admin_page.html",{'address':address,'lycrapants':lycrapants,'vestis':vestis,'shirts':shirts,'vestiandshirrtspattus':vestiandshirrtspattus,'smarts':response, 'smartpayment':smartpayment,'getintouch':customermessgae})


def genscollections(request):
    addprodd=Addprodadmin.objects.all()
    lycrapan=lycrapant.objects.all()
    vestis=vesti.objects.all()
    shirts=shirt.objects.all()
    vestiandshirrtspattus=vestiandshirrtspattu.objects.all()
    return render(request, "genscollections.html",{'addprodd':addprodd,'lycrapan':lycrapan,'vestis':vestis,'shirts':shirts,'vestiandshirrtspattus':vestiandshirrtspattus})
#======================================================Admin Add  Dress=============================
def lycrashirt(request):
    if request.method =="POST":
        dress_name=request.POST['proname']
        dressimages=request.POST.get('dressfiles')
        dress_amount=request.POST['Dressamount']
        addprod=Addprodadmin.objects.create(dress_name=dress_name,dressimages=dressimages,dress_amount=dress_amount)
        addprod.save()
        messages.success(request, "Add Dresses successfully ")
        return redirect('admin_page') 
    return render(request, "add.html")

def lycrapantss(request):
    if request.method =="POST":
        dress_name=request.POST['proname']
        dressimages=request.POST.get('dressfiles')
        dress_amount=request.POST['Dressamount']
        lycrapants=lycrapant.objects.create(dress_name=dress_name,dressimages=dressimages,dress_amount=dress_amount)
        lycrapants.save()
        messages.success(request, "Add dress successfully")
        return redirect('admin_page') 
    return render(request, "add.html")



def tshirts(request):
    if request.method =="POST":
        dress_name=request.POST['proname']
        dressimages=request.POST.get('dressfiles')
        dress_amount=request.POST['Dressamount']
        lycrapants=shirt.objects.create(dress_name=dress_name,dressimages=dressimages,dress_amount=dress_amount)
        lycrapants.save()
        messages.success(request, "Add dress successfully")
        return redirect('admin_page') 
    return render(request, "add.html")



def vestiandshirrtss(request):
    if request.method =="POST":
        dress_name=request.POST['proname']
        dressimages=request.POST.get('dressfiles')
        dress_amount=request.POST['Dressamount']
        lycrapants=vesti.objects.create(dress_name=dress_name,dressimages=dressimages,dress_amount=dress_amount)
        lycrapants.save()
        messages.success(request, "Add dress successfully")
        return redirect('admin_page') 
    return render(request, "add.html")


def vestiandshirrtsspattu(request):
    if request.method =="POST":
        dress_name=request.POST['proname']
        dressimages=request.POST.get('dressfiles')
        dress_amount=request.POST['Dressamount']
        lycrapants=vestiandshirrtspattu.objects.create(dress_name=dress_name,dressimages=dressimages,dress_amount=dress_amount)
        lycrapants.save()
        messages.success(request, "Add dress successfully")
        return redirect('admin_page') 
    return render(request, "add.html")



#======================================================================================================


def gendelete(request, id):
    get=Genscollectionpayment.objects.get(id=id)
    get.delete()
    messages.success(request, "Data was Deleted")
    return redirect('admin_page')


def girldelete(request, id):
    geirldele=Girlscollectionpayment.objects.get(id=id)
    geirldele.delete()
    messages.success(request, "Data was Deleted")
    return redirect('admin_page')



  
def home(request):
    return render(request, "home.html")

def user_register(request):
    if request.method == "POST":
        username = request.POST['txtname']
        email=request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            user=User.objects.create_user(username=username,email=email,password=confirm_password)
            user.save()
            messages.success(request, username +" is register in page, successfully")
            return redirect('login')
        return render(request, "user_register.html")
    return render(request, "user_register.html")

def     user_login(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        userlogin=authenticate(username=username,password=password)
        if userlogin is not None:
            login(request, userlogin)
            userlogin.save()
            messages.success(request, username + " is  login page successfully ")
            return redirect('collection')
        messages.warning(request, "Sorry Password is not matching..")
        return render(request, "user_login.html")
    return render(request, "user_login.html")

def about(request):
    return render(request, "about.html")


#================================================


def getintouch(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        user=Getintough.objects.create(name=name, email=email,message=message)
        user.save()
        return redirect('purchase')
    return render(request, "getintouch.html")

def rating(request):
    if request.method=="POST":
        rating=request.POST['rating']
        rating=Rating.objects.create(rating=rating)
        rating.save()
        messages.success(request, "Thank You")
        return redirect('collection')
    return render(request, "rating.html")

def collection(request):
    return render(request, "collection.html")


#=================================Ladiesdress====================
def Ladiesdress(request):
    return render(request, "Ladiesdress.html")
def paymentpage(request):
    return render(request, "paymentpage.html")



def Kanchipuram(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        dresssize=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Girlscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,dresssize=dresssize,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.dresssize}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "KanchipuramBlue.html")

def Kanchipuramred(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        dresssize=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Girlscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,dresssize=dresssize,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.dresssize}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Kanchipuramred.html")

def KanchipuramredKashta(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        dresssize=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Girlscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,dresssize=dresssize,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.dresssize}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "KanchipuramKashta.html")

def Kanchipuramsarees(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        dresssize=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Girlscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,dresssize=dresssize,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.dresssize}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Kanchipuramsareeyello.html")


def Kanchipuramsarepurple(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        dresssize=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Girlscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,dresssize=dresssize,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.dresssize}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Kanchipuramsarepurple.html")

def Mysoresareepink(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        dresssize=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Girlscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,dresssize=dresssize,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.dresssize}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Mysoresareepink.html")

def Mysorecrepe(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        dresssize=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Girlscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,dresssize=dresssize,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.dresssize}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Mysorecrepe.html")

def Mysorewedding(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        dresssize=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Girlscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,dresssize=dresssize,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.dresssize}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Mysorewedding.html")

def Mysoreblack(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        dresssize=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Girlscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,dresssize=dresssize,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.dresssize}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Mysoreblack.html")

def Mysoresilkblue(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        dresssize=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Girlscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,dresssize=dresssize,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.dresssize}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)

        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Mysoresilkblue.html")
#=======================================Gen


def Vestiandshirts(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        size=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Genscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,size=size,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.size}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    data=vesti.objects.all()
    return render(request, "Vestiandshirtsgens.html",{'data':data})

def tShirtswhite(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        size=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Genscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,size=size,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.size}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    Datas=shirt.objects.all()
    return render(request, "tShirtswhite.html",{'Datas':Datas})

def Jeans(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        size=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Genscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,size=size,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.size}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    data2=lycrapant.objects.all()
    return render(request, "Jeans.html",{'data2':data2})

def Gensshirtblues(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        size=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Genscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,size=size,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.size}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    data3=Addprodadmin.objects.all()
    return render(request, "Gensshirtblues.html",{'data3':data3})

def Jeanshirtslight(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        size=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Genscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,size=size,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.size}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Jeanshirtslight.html")

def Vestiandshirtspattu(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        size=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Genscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,size=size,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.size}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    vestiandshitpattu=vestiandshirrtspattu.objects.all()
    return render(request, "Vestiandshirtspattu.html",{'vestiandshitpattu':vestiandshitpattu})


def Casualshirts(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        size=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Genscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,size=size,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.size}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)

        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Casualshirts.html")

def Shirtspinks(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        size=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Genscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,size=size,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.size}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)

        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Shirtspinks.html")


def Formalshirt(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        size=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Genscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,size=size,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.size}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)

        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Formalshirt.html")

def Checkedshirtss(request):
    if request.method == "POST":
        Customername=request.POST['firstname']
        customeremail=request.POST['email']
        customerphnumber=request.POST['contact']
        customeraddress=request.POST['address']
        dressname=request.POST['dressname']
        dresscolor=request.POST['color']
        dressprice=request.POST['total_cost']
        size=request.POST['selectsize']
        dressqnty=request.POST['Quantity']
        dressamount=request.POST['total_Amount']
        paymentstype=request.POST['paymenttype']
        accountnumber=request.POST['cardnumber']
        deliverydate=request.POST['deliverydate']
        payment=Genscollectionpayment.objects.create(Customername=Customername,customeremail=customeremail,dresscolor=dresscolor,customerphnumber=customerphnumber,customeraddress=customeraddress,dressname=dressname,dressqnty=dressqnty,dressamount=dressamount,dressprice=dressprice,size=size,accountnumber=accountnumber,paymentstype=paymentstype,deliverydate=deliverydate)
        sub='Smart Fashion'
        messagess=f'Hello Mr/Ms:{payment.Customername}. Dress Details: Dress Name: {payment.dressname}, Dress Color: {payment.dresscolor},Dress Size: {payment.size}Dress Price: {payment.dressprice},Dress Quantity: {payment.dressqnty},Dress Total Amount: {payment.dressamount},Delivery Date: {payment.deliverydate} Help Line: 91889 99909'
        email_form=settings.EMAIL_HOST_USER
        recipient_list= [payment.customeremail]
        send_mail(sub,messagess,email_form,recipient_list)
        payment.save()
        messages.success(request, "Booking Succesfully")
        return redirect('rating')
    return render(request, "Checkedshirtss.html")

