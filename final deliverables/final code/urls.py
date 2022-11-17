from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #admin============
    path('Userasdmin/',views.admin, name="admin"),
    path('admin_page/',views.admin_page, name="admin_page"),
     #===================================Delete====================
     path('add/',views.lycrashirt, name="add"),
     path('lycrashirt/',views.lycrapantss, name="lycrapantss"),
     path('tshirts/',views.tshirts, name="tshirts"),
     path('vestiandshirrtss/',views.vestiandshirrtss, name="vestiandshirrtss"),
     path('vestiandshirrtsspattu/',views.vestiandshirrtsspattu, name="vestiandshirrtsspattu"),


    path('gendelete/<int:id>/',views.gendelete, name="gendelete"),
    path('girldelete/<int:id>/',views.girldelete, name="girldelete"),
    #=================================================
    #User Register Login
    path('logins/',views.user_login, name="login"),
    path('register/',views.user_register, name="register"),
    #===================================================
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    
    # path('chat/',views.chatbot, name="chat")
 

   
    #========================GET In Touch===================
    path('gteintouch',views.getintouch, name="getintouch"),
    #========================Rating=============================
    path('rating/',views.rating, name="rating"),
    #========================Gen and Girl====================
    path('collection/', views.collection, name="collection"),
    #============================Ladies Dress Collection====================================
    path('LadiesDressCollection/', views.Ladiesdress, name="Ladiesdress"),
    #========================Paymentpagegirls
    path('paymentpage/',views.paymentpage, name="paymentpage"),
    path('KanchipuramBlue/',views.Kanchipuram, name="KanchipuramBlue"),
    path('Kanchipuramred/',views.Kanchipuramred, name="Kanchipuramred"),
    path('KanchipuramredKashta/',views.KanchipuramredKashta, name="KanchipuramredKashta"),
    path('Kanchipuramsareeyello/',views.Kanchipuramsarees, name="Kanchipuramsareeyello"),
    path('Kanchipuramsarepurple /',views.Kanchipuramsarepurple, name="Kanchipuramsarepurple"),
    path('Mysoresareepink /',views.Mysoresareepink, name="Mysoresareepink"),
    path('Mysorecrepe  /',views.Mysorecrepe, name="Mysorecrepe"),
    path('Mysorewedding /',views.Mysorewedding, name="Mysorewedding"),
    path('Mysoreblack/',views.Mysoreblack, name="Mysoreblack"),
    path('Mysoresilkblue/',views.Mysoresilkblue, name="Mysoresilkblue"),
    
    #==========================Gens Collection=======
    path('genscollections/',views.genscollections, name="genscollections"),
    path('Vestiandshirts/',views.Vestiandshirts, name="Vestiandshirts"),
    path('tShirtswhite/',views.tShirtswhite, name="tShirtswhite"),
    path('Jeans/',views.Jeans, name="Jeans"),
    path('Gensshirtblues/',views.Gensshirtblues, name="Gensshirtblues"),
    path('Vestiandshirtspattu/',views.Vestiandshirtspattu, name="Vestiandshirtspattu"),
    path('Jeanshirtslight/',views.Jeanshirtslight, name="Jeanshirtslight"),
    path('Casualshirts/',views.Casualshirts, name="Casualshirts"),
    path('Shirtspinks/',views.Shirtspinks, name="Shirtspinks"),
    path('Formalshirt/',views.Formalshirt, name="Formalshirt"),
    path('Checkedshirtss/',views.Checkedshirtss, name="Checkedshirtss"),
   
    
   
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
