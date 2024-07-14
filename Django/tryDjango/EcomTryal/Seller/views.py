from django.shortcuts import render,redirect
from django.urls import reverse
import firebase,pyrebase,firebase_admin
from firebase_admin import credentials , firestore,storage
import json

firebaseConfig = {
  "apiKey": "AIzaSyBCFpno1naa_1Thc4BUjt0TV7Uokvqf1W8",
  "authDomain": "ecomm3-254e9.firebaseapp.com",
  "projectId": "ecomm3-254e9",
  "storageBucket": "ecomm3-254e9.appspot.com",
  "messagingSenderId": "820764794719",
  "appId": "1:820764794719:web:d1d2ec9cf5709adc21e0ea",
  "measurementId": "G-QEJ2HNXHQW",
  "databaseURL":"https://ecomm3-254e9-default-rtdb.europe-west1.firebasedatabase.app/",
};
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
service={
  "type": "service_account",
  "project_id": "ecomm3-254e9",
  "private_key_id": "a0983cfd42c4ad6ac676ca98a635b011239fb266",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCynD7o/SMssh0F\nUOxQou2l5hisqeJYUyXvHK8U0mckc9Bv0Vs9p9IW5fla4WMwEENsnRV1W1/1F9GL\nWG/Sv2BLtMDoHtI+ehTWYy8eLolycON5J4/Wlv5TaHd4LT4UXKD8+SfHJ7S8nM6y\nU3r8CMilBgphWH8+CUz0o45cu7/y/76Op7a3VYaat9FeKhZHMKh0v0vpZNvF2PoE\n9vOwd+4xSVcABWgNABcQq2ncrYbibJFywM05aFp6fMVFVDLcc4IpiAMyU0XceImn\nq0NVNQqq7rtDwqBei+lRJ9qoy2ariXFjLnrwucrYdqornpkjKN8syFdpNGehG9Kd\nXRlr7XZ7AgMBAAECggEAQcw7hLtUTO/krwOrutz6rUYBywHeh2lCLT8k5IfKRWyA\n2eCHO0RqqdLYtHkZgChNnmKT+CLMS88Ve779muazg9A3zIsmKqvwpzXssrK0Ibui\noQxI+eWwFWwDrvsDxp6FFAx5ce2XsHAX2SvVv6lAuUJraocegO0OM4VZOaJUySB+\nNpnEDLOAOYeCNPqJu2JOkZnCDfPlE71tpZmKg3+3DYVKSBLUxWIiDCA2m6TrqeHG\nJIZOUZmHoH1F4SxTtzplZiGPK+W59k25VCwlcTmxIjLxYgbLA6ixD1bUgpjngGhm\nnpGX37707oT2kPcTLZ4DPk3f6Q9f6+B4RGYcaLNlEQKBgQDXDE/ZixHAPpEoHkqR\nlERbyw4f7yJW/b3eN4O0NFfrXQVgMhcIzVyjsXR1tNac0c112V2CbQUlKlQxG5/a\n5UzMwmOguqC5a2lIUbt9F+RELhAFaxVLfMtNEq2h1RlHlshfwmim/vceVg8CeroC\nUxMJIc3I0/J4sJiRuP1oqGqWUwKBgQDUn5PHAbUFWCgFa6LsKHDq8+ROMradrrn0\nkcAkrcdcK/EslNnzjqrTfWOxUscs7AjrdMelLvr5O8pPUgGR6w/iHLowAC/G+7Fi\n7bsp+NOAfsyKVzIupsdmSFb/sNksSio75NLdkZll3SlIz85PRjzpU8fxufFN/Isk\nFXQNHIpKOQKBgBUSmciBfi3Oc77wqPH3C3PLRAkRD9ZiavaZjghckLj5lotEnUk5\nhnhr7TOTkuwvCukfcbBUKornyPQ+9r0mdw4hhk27vAAvbFOv3qV1b+LWeK9vPNj2\n050r1WPkU+PV/LCVhlfG6ERKvpHJoOyVY2ojq9ygGESHWYv+Cqb0ye0NAoGABj7N\ns2m8bHTDcC1SMseZUX1qdlWNAaKxOZrSXwFvuqhbxCh3Im1NXTrwo7O/v/UK6geb\nGaIAozN7ZMsO2r9hzw1y9pf6z0hzVGmRNtFlPP/8eA/JnI8vijSTwZzrNB7VkL7O\n5s0xCUnuvYHFGJUCkwPv+oywps7FM4Eh0ITHFxkCgYEAxdBrpvAKRFDIhcsCerOV\nijIOAeqrc9bObxOtdTm8G3RkkP4xj41F1MdJkuu7E31+ih+7zh0iBVqJjFVXrLBw\n0+JbimKNworNqZsVL7KPKIeL6sQRF0RoEs6DLfr3g65iooMvC/HOqU2PWPm5wA50\nFdMtuTjahNlR/vUmqrOnhA0=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-go3oj@ecomm3-254e9.iam.gserviceaccount.com",
  "client_id": "106062367916651596055",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-go3oj%40ecomm3-254e9.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(service)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
database = firestore.client()
storage = firebase.storage()
# def HomePage(request):
#     return render(request,'SellerHom.html')

def Seller_Singup(request):
    Name=request.POST.get('name')
    Mobile_number=request.POST.get('Mobile_number')
    Email=request.POST.get('Email')
    password=request.POST.get('password')
    s_data={
        'Name':Name,'Mobile_number':Mobile_number,'Email':Email,'password':password,'Type':'Seller','product_count':0,
    }
    try:
        main_id="Sell"+Name[::2]+Mobile_number[::3]+Email[::4]
        s_data['main_id']=main_id
        database.collection('Seller').document(Email).set(s_data)
        print(f'Seller account oppen & data uplod complet of {Name}')
        return render(request,'Seller-login_page.html',{ "data" :s_data })
    except:
        print("Account cant't open")
    return render(request,'Seller-Singup.html')


def Seller_login(request):
    s_data = None
    request.session['s_data'] = s_data
    print("you are in seler login page .////////////////////////////")
    email = request.POST.get('email')
    password = request.POST.get('password')
    # password='123456'
    print(f'{email} {password}')
    s_data=database.collection('Seller').document(email).get().to_dict()
    print(s_data)
    
    if s_data  : 
        if(s_data["Email"] == email and s_data["password"]==password and s_data["Type"]=="Seller"):
            page_T={
                'page_T':"Seller"
            }
            s_data.update(page_T)
            print(s_data)
            print("Seller sucess to sign up")
            request.session['s_data'] = s_data
            return redirect('Seller:sellerHome')
    else:
        print(f"fail to sign in: {email}")
    return render(request,'Seller-login_Page.html')

from django.contrib.auth import logout

def logout(request):
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
    s_data = request.session.get('s_data', {})
    email = s_data['Email']
    
    productCount = int(s_data["product_count"])
    print('...............................................................................')
    print(s_data)
    sellerId=s_data["main_id"]
    # print(f'{sellerId}  {email}')
    # print(f'your total uploded product {productCount}')
    # print(productCount+1)
    customer_data = {"product_count":productCount+1}
    s_data.update(customer_data)
    # print(s_data)
    # print(',.,.,.,.,.,.,.')

    
    # print(s_data)
    Name = request.POST.get('name')
    price = request.POST.get('price')
    descreption = request.POST.get('descreption')
    select_opt = request.POST.get('hidden_data')
    
    # generate unique name for product 
    import datetime
    x=datetime.datetime.now()
    x=str(x)
    p_generated=x[5:10:1]+x[11:13:1]+x[20:27:1]
    product_id=""
    if Name:
        product_id="Pd"+Name[::3]+str(productCount+1)+p_generated
    print(f'name is {Name}')
    # product_id is the name 
    path = request.POST.get('image')
    if path:
        path  = path.replace("\\","\\\\",1000)
        path = path.replace('"','',1000)
        print(f'the modefied path after replace is : {path}')
    print(f'the modefied path is : {path}')
    # this line is help to uplod image
    if path:
        if storage.child(str(select_opt)).child(f'{select_opt}{product_id}').put(path) :
            # storage.child(str(select_opt)).child(f'{select_opt}{product_id}').put(path)
            print("uplode is succes full ...........///////////..............")
        else :
            return render(request,'sellerUplod.html',{'s_data':s_data})
    url = storage.child(str(select_opt)).child(f'{select_opt}{product_id}').get_url(firebaseConfig['storageBucket'])
    r_url = str(url)   
     
    print(f'uploded image link is : {r_url}')
    UplodedProduct_data= {'Name':Name,'price':price,'descreption':descreption,'product_count':productCount+1,'ProductImg':r_url}
    if(select_opt == 'Clothes' or select_opt == 'Shows'):
        # color,brand,size,faeric,desine,paterns,type,model , User ,waight
        color = request.POST.get('color')
        brand = request.POST.get('brand')
        size = request.POST.get('size')
        faeric = request.POST.get('faeric')
        desine = request.POST.get('desine')
        paterns = request.POST.get('paterns')
        type = request.POST.get('type')
        model = request.POST.get('model')
        User = request.POST.get('User')
        waight = request.POST.get('waight')
        option = select_opt
        product_data = {
            'color':color,'brand':brand,'size':size,'faeric':faeric,'desine':desine,'paterns':paterns,'type':type,'model':model,
            'User':User,'waight':waight,"option":option,'seller_id':s_data["main_id"],
        }
        UplodedProduct_data.update(product_data)
        # print(product_data)
    elif(select_opt == 'mobile' or select_opt == 'Laptop'):
        # display size , display , battery , network , brand , ram & rom , waight,camera,procacers,warrenty,model number,color,sim slort,wifi , batery type,grafic , charging -->
        displaysize = request.POST.get('displaysize')
        display = request.POST.get('display')
        battery = request.POST.get('battery')
        network = request.POST.get('network')
        brand = request.POST.get('brand')
        ramrom = request.POST.get('ram&rom')
        waight = request.POST.get('waight')
        camera = request.POST.get('camera')
        procacers = request.POST.get('procacers')
        warrenty = request.POST.get('warrenty')
        modelnumber = request.POST.get('modelnumber')
        color = request.POST.get('color')
        simslort = request.POST.get('simslort')
        wifi = request.POST.get('wifi')
        baterytype = request.POST.get('baterytype')
        grafic = request.POST.get('grafic')
        charging = request.POST.get('charging')
        option = select_opt
        product_data = {
            'displaysize':displaysize,'display':display,'battery':battery,'network':network,'brand':brand,'camera':camera,'procacers':procacers,'warrenty':warrenty,
            'modelnumber':modelnumber,'color':color,'simslort':simslort,'wifi':wifi,'baterytype':baterytype,'grafic':grafic,'charging':charging,'option':option
        }
        UplodedProduct_data.update(product_data)
        # print(product_data)
    elif(select_opt == 'Gagets'):
        # size  , battery , wireless connection , brand , waight  ,warrenty, model number ,color, batery type , type , charging   -->
        batterypresent = request.POST.get('batterypresent')
        chargable = request.POST.get('Chargable')
        brand = request.POST.get('Brand')
        weight = request.POST.get('waight')
        model_number = request.POST.get('modelnumber')
        color = request.POST.get('color')
        wireless_connection = request.POST.get('wirelessconnection')
        battery_type = request.POST.get('baterytype'),
        option = select_opt
        product_data = {
            'batterypresent': batterypresent,
            'Chargable': chargable,
            'Brand': brand,
            'waight': weight,
            'modelnumber': model_number,
            'color': color,
            'wirelessconnection': wireless_connection,
            'baterytype': battery_type,
            'option':option
        }
        UplodedProduct_data.update(product_data)
        # print(product_data)
    elif(select_opt == 'Toys'):
        age = request.POST.get('age')
        waight = request.POST.get('Waight')
        chargable = request.POST.get('Chargable')
        size = request.POST.get('Size')
        material = request.POST.get('material')
        brand = request.POST.get('Brand')
        type_ = request.POST.get('Type')
        model = request.POST.get('Model')
        user = request.POST.get('User')
        option = select_opt
        product_data = {
            'age': age,
            'Waight': waight,
            'Chargable': chargable,
            'Size': size,
            'material': material,
            'Brand': brand,
            'Type': type_,
            'Model': model,
            'User': user,
            'option':option,
        }
        UplodedProduct_data.update(product_data)
        print(product_data)
    
    
    if (select_opt == 'Clothes' or select_opt == 'Shows' or select_opt == 'Laptop' or select_opt == 'mobile' or select_opt == 'Gagets' or select_opt == 'Toys'):
        # product_id="Pd"+Name[::3]+data['main_id'][::3]+str(productCount+1)+p_generated
        
        UplodedProduct_data.update({'product_id':product_id})
        UplodedProduct_data.update({'sellerId':sellerId})
        ok=database.collection('products').document(select_opt).collection('Products').document(product_id).set(UplodedProduct_data)
        ok=database.collection(select_opt).document(product_id).set(UplodedProduct_data)
        ok=database.collection('Products').document(product_id).set(UplodedProduct_data)
        print(ok)
        database.collection('Seller').document(s_data["Email"]).set(s_data)
    else :
        print("bal chal data push truy """"""""""""""""""""""""""""""""""""""")
    print("data uplod Succesfull")
    print(UplodedProduct_data)
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


# from firebase import storage

def upload_image_to_firebase(image_file):
    # Initialize Firebase Admin SDK
    # Make sure you have set up Firebase Admin SDK and initialized it properly
    
    # Upload image to Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob("images/" + image_file.name)
    blob.upload_from_string(image_file.read(), content_type=image_file.content_type)
    # Get public URL of the uploaded image
    return blob.public_url
    # path = "C:\\Users\\sayan\\Pictures\\Screenshots\\Screenshot 2024-04-27 200632.png"
    # path = "C:\Users\sayan\Pictures\Wallpaper\surgery-1807541.jpg"
    # upload_image_to_firebase(path)
    # storage.child("ok").child(f'sayan').put(path)
