from django.shortcuts import render,redirect
from django.urls import reverse
import firebase,pyrebase,firebase_admin
from firebase_admin import credentials , firestore,storage
from Seller.models import seller_singup,clothes, shoes, Mobile, Laptop, Gadget, Toy ,all_product
import json
import datetime


field_names = [field.name for field in seller_singup._meta.get_fields()]
# firebaseConfig = {
#   'apiKey': "AIzaSyBCFpno1naa_1Thc4BUjt0TV7Uokvqf1W8",
#   'authDomain': "ecomm3-254e9.firebaseapp.com",
#   'databaseURL': "https://ecomm3-254e9-default-rtdb.europe-west1.firebasedatabase.app",
#   'projectId': "ecomm3-254e9",
#   'storageBucket': "ecomm3-254e9.appspot.com",
#   'messagingSenderId': "820764794719",
#   'appId': "1:820764794719:web:d1d2ec9cf5709adc21e0ea",
#   'measurementId': "G-QEJ2HNXHQW"
# };
# firebase = pyrebase.initialize_app(firebaseConfig)
# storage = firebase.storage()

def Seller_Singup(request):
    
    Name=request.POST.get('name')
    Mobile_number=request.POST.get('Mobile_number')
    Email=request.POST.get('Email')
    password=request.POST.get('password')
    if Name != None and Mobile_number != None and Email != None and password != None:
        main_id="Sell"+Name[::2]+Mobile_number[::3]+Email[::4]
        seller_singup_info = seller_singup(Name = Name ,Mobile_number = Mobile_number , Email = Email ,password = password,main_id = main_id)
        seller_singup_info.save()
    print(f'database test .....?????')
    seller_singup_info = seller_singup.objects.filter(Email = Email , password = password)
    print(seller_singup_info)
    print(f'database test .....?????')
    s_data = None
    for data_part in seller_singup_info:
        # print(data_part)
        s_data = {field: getattr(data_part, field) for field in field_names}
    print(s_data)
    if s_data != None:
        print(f'Seller account oppen & data uplod complet of {Name}')
        return render(request,'Seller-login_page.html',{ "s_data" :s_data })
    else:
        print("Account cant't open")
    return render(request,'Seller-Singup.html')


def Seller_login(request):
    s_data = None
    request.session['s_data'] = s_data
    print("you are in seler login page .................... . . .")
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(f'{email} {password}')
    seller_singup_info = seller_singup.objects.filter(Email = email , password = password , Type = 'Seller')
    for data_part in seller_singup_info:
        s_data = {field: getattr(data_part, field) for field in field_names}
    print(s_data)
    if s_data != None: 
        print("Seller sucess to sign up")
        request.session['s_data'] = s_data
        return redirect('Seller:sellerHome')
    else:
        print(f"fail to sign in ......... ? ? ?")
    return render(request,'Seller-login_Page.html')

# from django.contrib.auth import logout

def logout(request):
    request.session.flush()
    return redirect('Seller_login')


def sellerHome(request):
    print("you are in seler home page .////////////////////////////")
    s_data = request.session.get('s_data', {})
    
    if s_data == None or s_data == {}:
        return redirect('Seller:Seller_login')
    else:
        print("..................................................")
        print(s_data)
        print("..................................................")
        request.session['s_data'] = s_data
    return render(request,"sellerHome.html",{'s_data':s_data})

def sellerUplod(request ):
    print("you are in seler uplod page .////////////////////////////")
    s_data = None
    s_data = request.session.get('s_data', {})
    if s_data == None:
        return render(request,'Seller:Seller_login')
    print(s_data)
    product_Count = {"product_count":str(int(s_data["product_count"])+1)}
    s_data.update(product_Count)
    print(s_data)
    
    Name = request.POST.get('name')
    price = request.POST.get('price')
    descreption = request.POST.get('descreption')
    select_opt = request.POST.get('hidden_data')
    
    product_id=""
    if Name:
        x=str(datetime.datetime.now())    # generate unique name for product
        product_id="Pd"+Name[::3]+str(int(s_data["product_count"])+1)+x[5:10:1]+x[11:13:1]+x[20:27:1]    # generate unique name for product 
    print(f'name is {Name} and id is {product_id}')
    # product_id is the name 
    path = "sayan"
    if request.POST.get('image'):
        path = request.POST.get('image')
        path  = path.replace("\\","\\\\",1000)
        path = path.replace('"','',1000)
        print(f'the modefied path after replace is : {path}')
    print(f'the modefied path is : {path}')
    {
    # this line is help to uplod image
    # if path:
    #     if storage.child(str(select_opt)).child(f'{select_opt}{product_id}').put(path) :
    #         # storage.child(str(select_opt)).child(f'{select_opt}{product_id}').put(path)
    #         print("img uplode is succes full ...........///////////..............")
    #     else :
    #         print("img uplode is fail ................. ???")
    #         return render(request,'sellerUplod.html',{'s_data':s_data})
    # url = storage.child(str(select_opt)).child(f'{select_opt}{product_id}').get_url(firebaseConfig['storageBucket'])
    }
    if path != None:
        r_url = path   
    elif(path == None):path = "no link from sayan"
    print(f'uploded image link is : {r_url}')
    UplodedProduct_data= {'name':Name,
                          'price':price,
                          'description':descreption,
                          'product_id':product_id,
                          'product_img':r_url,
                          'seller_id':s_data["main_id"],
                          }
    all_ditails_product = UplodedProduct_data
    if(select_opt == 'Clothes' or select_opt == 'Shows'):
        # color,brand,size,faeric,desine,paterns,type,model , User ,waight
        size = request.POST.get('size')
        color = request.POST.get('color')
        brand = request.POST.get('brand')
        fabric = request.POST.get('faeric')
        design = request.POST.get('desine')
        patterns = request.POST.get('paterns')
        type = request.POST.get('type')
        model = request.POST.get('model')
        user = request.POST.get('User')
        weight = request.POST.get('waight')
        option = select_opt
        product_data = {
            'color':color,'brand':brand,'size':size,'fabric':fabric,'design':design,'patterns':patterns,'type':type,'model':model,
            'user':user,'weight':weight,"option":option,
        }
        all_ditails_product.update(product_data)
        UplodedProduct_data.update(product_data)
        if select_opt == 'Clothes':
            print(f'..........................{select_opt}')
            print(UplodedProduct_data)
            clothes.objects.create(**UplodedProduct_data)
            print('..........................')
        elif select_opt == 'Shows':
            print(f'..........................{select_opt}')
            print(UplodedProduct_data)
            shoes.objects.create(**UplodedProduct_data)
            print('..........................')
    elif(select_opt == 'mobile' or select_opt == 'Laptop'):
        # display size , display , battery , network , brand , ram & rom , waight,camera,procacers,warrenty,model number,color,sim slort,wifi , batery type,grafic , charging -->
        display_size = request.POST.get('displaysize')
        display = request.POST.get('display')
        battery = request.POST.get('battery')
        network = request.POST.get('network')
        brand = request.POST.get('brand')
        ram_rom = request.POST.get('ram&rom')
        weight = request.POST.get('waight')
        camera = request.POST.get('camera')
        processors = request.POST.get('procacers')
        warranty = request.POST.get('warrenty')
        model_number = request.POST.get('modelnumber')
        color = request.POST.get('color')
        sim_slot = request.POST.get('simslort')
        wifi = request.POST.get('wifi')
        battery_type = request.POST.get('baterytype')
        graphics = request.POST.get('grafic')
        charging = request.POST.get('charging')
        option = select_opt
        product_data = {
            'display_size':display_size,
            'display':display,
            'battery':battery,
            'network':network,
            'brand':brand,
            'ram_rom':ram_rom,
            'weight':weight,
            'camera':camera,
            'processors':processors,
            'warranty':warranty,
            'model_number':model_number,
            'color':color,
            'sim_slot':sim_slot,
            'wifi':wifi,
            'battery_type':battery_type,
            'graphics':graphics,
            'charging':charging,
            'option':option
        }
        UplodedProduct_data.update(product_data)
        all_ditails_product.update(product_data)
        if select_opt == 'mobile' :
            print(f'..........................{select_opt}')
            print(UplodedProduct_data)
            Mobile.objects.create(**UplodedProduct_data)
            print(f'..........................')
        if select_opt == 'Laptop' :
            print(f'..........................{select_opt}')
            print(UplodedProduct_data)
            Laptop.objects.create(**UplodedProduct_data)
            print(f'..........................')
        # print(product_data)
    elif(select_opt == 'Gagets'):
        # size  , battery , wireless connection , brand , waight  ,warrenty, model number ,color, batery type , type , charging   -->
        battery_present = request.POST.get('batterypresent')
        chargeable = request.POST.get('Chargable')
        brand = request.POST.get('Brand')
        weight = request.POST.get('waight')
        model_number = request.POST.get('modelnumber')
        color = request.POST.get('color')
        wireless_connection = request.POST.get('wirelessconnection')
        battery_type = request.POST.get('baterytype'),
        option = select_opt
        product_data = {
            'battery_present': battery_present,
            'chargeable': chargeable,
            'brand': brand,
            'weight': weight,
            'model_number': model_number,
            'color': color,
            'wireless_connection': wireless_connection,
            'battery_type': battery_type,
            'option':product_id
        }
        UplodedProduct_data.update(product_data)
        all_ditails_product.update(product_data)
        print(f'..........................{select_opt}')
        print(UplodedProduct_data)
        Gadget.objects.create(**UplodedProduct_data)
        print(f'..........................')
        # print(product_data)
    elif(select_opt == 'Toys'):
        age = request.POST.get('age')
        weight = request.POST.get('Waight')
        chargeable = request.POST.get('Chargable')
        size = request.POST.get('Size')
        material = request.POST.get('material')
        brand = request.POST.get('Brand')
        type = request.POST.get('Type')
        model = request.POST.get('Model')
        user = request.POST.get('User')
        option = select_opt
        product_data = {
            'age': age,
            'weight': weight,
            'chargeable': chargeable,
            'size': size,
            'material': material,
            'brand': brand,
            'type': type,
            'model': model,
            'user': user,
            'option':option,
        }
        UplodedProduct_data.update(product_data)
        all_ditails_product.update(product_data)
        print(f'..........................{select_opt}')
        print(UplodedProduct_data)
        Toy.objects.create(**UplodedProduct_data)
        print(f'..........................')
    if(select_opt == 'Clothes' or select_opt == 'Shows'or select_opt == 'Toys' or select_opt == 'Gagets' or select_opt == 'mobile' or select_opt == 'Laptop'):
        rankInAllList = all_product.objects.create(**all_ditails_product)
        print(f'in all product list its rank is {rankInAllList}')
    print(f'selected option is : {select_opt}')
    print('only spacific database')
    print(UplodedProduct_data)
    print('all marged database')
    print(all_ditails_product)
    print("data uplod Succesfull")
    if Name != None:
        return render(request,'UplodSuccesfull.html',{'Name':Name,'s_data':s_data,'product_id':product_id})
    else:
        print("It uploding not complit")
    return render(request,'sellerUplod.html',{'s_data':s_data})


def uplodSucessFull(request,Name):
    print("you are in seler login page .////////////////////////////")
    print(" after sucessfull uplod name is "+Name)
    seller_home_url = render('Seller:sellerHome')
    return render(request,'UplodSuccesfull.html',{'seller_home_url': seller_home_url})


# def handle_product_upload(request):
#     if select_opt in ['Clothes', 'Shoes']:
#         size = request.POST.get('size')
#         color = request.POST.get('color')
#         brand = request.POST.get('brand')
#         fabric = request.POST.get('fabric')
#         design = request.POST.get('design')
#         patterns = request.POST.get('patterns')
#         type = request.POST.get('type')
#         model = request.POST.get('model')
#         user = request.POST.get('user')
#         weight = request.POST.get('weight')
#         product_data = {
#             'size': size, 'color': color, 'brand': brand, 'fabric': fabric, 
#             'design': design, 'patterns': patterns, 'type': type, 
#             'model': model, 'user': user, 'weight': weight,
#         }

#     elif select_opt in ['mobile', 'Laptop']:
#         display_size = request.POST.get('display_size')
#         display = request.POST.get('display')
#         battery = request.POST.get('battery')
#         network = request.POST.get('network')
#         brand = request.POST.get('brand')
#         ram_rom = request.POST.get('ram_rom')
#         weight = request.POST.get('weight')
#         camera = request.POST.get('camera')
#         processors = request.POST.get('processors')
#         warranty = request.POST.get('warranty')
#         model_number = request.POST.get('model_number')
#         color = request.POST.get('color')
#         sim_slot = request.POST.get('sim_slot')
#         wifi = request.POST.get('wifi')
#         battery_type = request.POST.get('battery_type')
#         graphics = request.POST.get('graphics')
#         charging = request.POST.get('charging')
#         product_data = {
#             'display_size': display_size, 'display': display, 'battery': battery, 
#             'network': network, 'brand': brand, 'ram_rom': ram_rom, 'weight': weight, 
#             'camera': camera, 'processors': processors, 'warranty': warranty, 
#             'model_number': model_number, 'color': color, 'sim_slot': sim_slot, 
#             'wifi': wifi, 'battery_type': battery_type, 'graphics': graphics, 
#             'charging': charging,
#         }

#     elif select_opt == 'Gadgets':
#         battery_present = request.POST.get('battery_present')
#         chargeable = request.POST.get('chargeable')
#         brand = request.POST.get('brand')
#         weight = request.POST.get('weight')
#         model_number = request.POST.get('model_number')
#         color = request.POST.get('color')
#         wireless_connection = request.POST.get('wireless_connection')
#         battery_type = request.POST.get('battery_type')
#         product_data = {
#             'battery_present': battery_present, 'chargeable': chargeable, 
#             'brand': brand, 'weight': weight, 'model_number': model_number, 
#             'color': color, 'wireless_connection': wireless_connection, 
#             'battery_type': battery_type,
#         }

#     elif select_opt == 'Toys':
#         age = request.POST.get('age')
#         weight = request.POST.get('weight')
#         chargeable = request.POST.get('chargeable')
#         size = request.POST.get('size')
#         material = request.POST.get('material')
#         brand = request.POST.get('brand')
#         type = request.POST.get('type')
#         model = request.POST.get('model')
#         user = request.POST.get('user')
#         product_data = {
#             'age': age, 'weight': weight, 'chargeable': chargeable, 'size': size, 
#             'material': material, 'brand': brand, 'type': type, 'model': model, 
#             'user': user,
#         }

#     UplodedProduct_data.update(product_data)
#     print(f'..........................{select_opt}')
#     print(UplodedProduct_data)
#     Product.objects.create(**UplodedProduct_data)
#     print('..........................')

# # Note: Make sure the request.POST keys match the field names correctly.
