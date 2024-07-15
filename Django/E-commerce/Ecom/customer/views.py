from django.shortcuts import render,redirect
import json
import firebase_admin,pyrebase
from firebase_admin import credentials , firestore
from firebase_admin import credentials, initialize_app, storage
from customer.models import user_singup,shoppingAddres
from HomePage.models import cart
from Seller.models import all_product
from django.core import serializers
from django.forms.models import model_to_dict

field_names = [field.name for field in user_singup._meta.get_fields()]
# ####### singup


def Singup(request):
    Name=request.POST.get('name')
    Mobile_number=request.POST.get('Mobile_number')
    Email=request.POST.get('Email')
    password=request.POST.get('password')
    if Name != None and Mobile_number != None and Email != None and password != None:
        main_id=Name[::2]+Mobile_number[::3]+Email[::4]
        # try :
        new_user = user_singup(Name = Name ,Mobile_number = Mobile_number,Email = Email,password = password ,main_id = main_id)
        new_user.save()
        print(f'account oppen & data uplod complet of {Name}')
        customer_data = None
        customer_info = user_singup.objects.filter(Email = Email,password = password )
        try:
            for data_part in customer_info:
                customer_data = {field: getattr(data_part, field) for field in field_names}
                print(customer_data)
            return render(request,"login_page.html",{"c_data":customer_data})
        except:
            print(f'data is not avaliable')
            print("Account cant't open")
        
    return render(request,'Singup.html')
def user_login(request):
    print("you are in ogin page ")
    c_data = None
    c_data = request.session.get('c_data')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(f'{email} {password}')
    db_c_data=user_singup.objects.filter(Email = email,password = password)
    for data_part in db_c_data:
        print("data_part")
        print(data_part)
        c_data = {field: getattr(data_part, field) for field in field_names}
    print("............................???/")
    print(c_data)
    print("............................???/")
    if c_data != None: 
        request.session['c_data'] = c_data
        print(c_data)
        print("sucess to sign up")
        return redirect("homepage:HomePage")
    else:
        print(f"fail to sign in: {email}")
    return render(request,"login_page.html")
def logOutCustomer(request):
    print("try to log out")
    request.session.flush()
    return redirect('customer:user_login')

def Cart(request):
    c_data = request.session.get('c_data')
    c_Email = c_data['Email']
    
    userCartData = cart.objects.filter(customer_id = c_data['main_id'])
    print(userCartData)
    allCardItems = {}
    for i,j in enumerate(userCartData):
        data = serializers.serialize('json',[j])
        dect_data = json.loads(data)[0]
        allCardItems[i]=(dect_data['fields'])
    cartDataLen = len(userCartData)
    totalPrice = 0
    allCardItemsData = {}
    for i in allCardItems:
        cart_product_id = allCardItems[i]['productId']
        # print(cart_product_id)
        product_data = ''
        product_gr = all_product.objects.filter(product_id = cart_product_id)
        for key,j in enumerate(product_gr):
            product_data = serializers.serialize('json',[j])
            product_data = json.loads(product_data)[0]
        # print(product_data)
        # print("\n\n")
        totalPrice = totalPrice + int(product_data['fields']['price'])
        allCardItemsData[i] = (product_data['fields'])
        prices = {
            'customerId':c_data['main_id'],
            'totalItem': i+1,
            'productPrice' : totalPrice,  
            'discountPrice' : '00',
            'PackagingFee' : '40',
            'DeliveryCharge' : '100',
        }
        totalPrice = int(prices['totalItem']) + int(prices['productPrice']) + int(prices['PackagingFee']) + int(prices['discountPrice']) + int(prices['DeliveryCharge'])
        prices.update({'totalPrice':totalPrice})
    allCardItemsData['price'] = prices
    newAddress = {}
    try: # try to uplode new address 
        print('try to add a new address')
        ReciverName = request.POST.get('ReciverName')
        ReciverMobileNo = request.POST.get('ReciverMobileNo')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        Home_Rode_Address = request.POST.get('Home_Rode_Address')
        newAddress = {
            'customerId':c_data['main_id'],
            'ReciverName':ReciverName,
            'ReciverMobileNo':ReciverMobileNo,
            'state':state,
            'city':city,
            'pincode':pincode,
            'Home_Rode_Address':Home_Rode_Address,
        }
        print(newAddress)
        for k in newAddress:
            print(f'{newAddress[k]} --->  {len(newAddress[k])}')
        # newShoppingAddres = addShoppingAddres.objects.create(**newAddress)
        newShoppingAddres = shoppingAddres(**newAddress)
        newShoppingAddres.save()
    except:
        print('No try about add address')

    userAddress = shoppingAddres.objects.filter(customerId = c_data['main_id'])
    userAddres = {}
    j=0
    for i in userAddress:
        j+=1
        print(type(i))
        # userAddress[j] = i
        print(f'{i}')
        model_dict = model_to_dict(i)
        # Store the dictionary in userAddres
        userAddres[j] = model_dict
    print('end..................................')
    print(userAddres)
    return render(request , "cart.html",{'cartItems':allCardItemsData ,'userAddres':userAddres})

def allOrders(request):
    return render(request , "allOrders.html")

def aboutOrder(request):
    return render(request,'aboutOrder.html')