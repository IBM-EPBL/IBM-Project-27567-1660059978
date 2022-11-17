from django.db import models
class Addprodadmin(models.Model):
    dressimages=models.ImageField()
    dress_name=models.CharField(max_length=20)
    dresscolor=models.CharField(max_length=20)
    dress_amount=models.CharField(max_length=10)
    def __str__(self):
        return self.dress_name

class lycrapant(models.Model):
    dressimages=models.ImageField()
    dress_name=models.CharField(max_length=20)
    dresscolor=models.CharField(max_length=20)
    dress_amount=models.CharField(max_length=10)
    def __str__(self):
        return self.dress_name


class vesti(models.Model):
    dressimages=models.ImageField()
    dress_name=models.CharField(max_length=20)
    dresscolor=models.CharField(max_length=20)
    dress_amount=models.CharField(max_length=10)
    def __str__(self):
        return self.dress_name


class shirt(models.Model):
    dressimages=models.ImageField()
    dress_name=models.CharField(max_length=20)
    dresscolor=models.CharField(max_length=20)
    dress_amount=models.CharField(max_length=10)
    def __str__(self):
        return self.dress_name



class vestiandshirrtspattu(models.Model):
    dressimages=models.ImageField()
    dress_name=models.CharField(max_length=20)
    dresscolor=models.CharField(max_length=20)
    dress_amount=models.CharField(max_length=10)
    def __str__(self):
        return self.dress_name




class Girlscollectionpayment(models.Model):
    Customername=models.CharField(max_length=100)
    customeremail=models.EmailField()
    customerphnumber=models.CharField(max_length=100)
    customeraddress=models.CharField(max_length=100)
    dressname=models.CharField(max_length=100)
    dresscolor=models.CharField(max_length=100)
    dressprice=models.CharField(max_length=100)
    ladiessize=(
    ("7meters", "7meters"),
    ("8meters", "8meters"),
    )
    dresssize=models.CharField(max_length=20,choices=ladiessize,default='1')
    dressqnty=models.CharField(max_length=100)
    dressamount=models.CharField(max_length=100)
    paymentmethod=(
    ("Paytm", "Paytm"),
    ("GooglePay", "GooglePay"),
    ("Freecharge", "Freecharge"),
    ("YonoSBI", "YonoSBI"),
    ("Payzapp", "Payzapp"),
    )
    paymentstype=models.CharField(max_length=20,choices=paymentmethod,default='1')
    accountnumber=models.CharField(max_length=100)
    deliverydate=models.CharField(max_length=100)
    def __str__(self):
        return self.dressname

class Genscollectionpayment(models.Model):
    Customername=models.CharField(max_length=100)
    customeremail=models.EmailField()
    customerphnumber=models.CharField(max_length=100)
    customeraddress=models.CharField(max_length=100)
    dressname=models.CharField(max_length=100)
    dresscolor=models.CharField(max_length=100)
    dressprice=models.CharField(max_length=100)
    choice_size=(
    ("1", "M"),
    ("2", "S"),
    ("3", "L"),
    ("4", "XL"),
    ("4", "XXL"),
    )
    size=models.CharField(max_length=20,choices=choice_size,default='1')

    dressqnty=models.CharField(max_length=100)
    dressamount=models.CharField(max_length=100)
    paymentmethod=(
    ("Paytm", "Paytm"),
    ("GooglePay", "GooglePay"),
    ("Freecharge", "Freecharge"),
    ("YonoSBI", "YonoSBI"),
    ("Payzapp", "Payzapp"),
    )
    paymentstype=models.CharField(max_length=20,choices=paymentmethod,default='1')
    accountnumber=models.CharField(max_length=100)
    deliverydate=models.CharField(max_length=100)
    def __str__(self):
        return self.dressname
    
    
    





    def __str__(self):
        return self.dressname



class Getintough(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.CharField(max_length=100)
    def __str__(self):
        return self.name
        

class Rating(models.Model):
    rating=models.CharField(max_length=100)
    def __str__(self):
        return self.rating