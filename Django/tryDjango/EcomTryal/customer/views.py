from django.shortcuts import render,redirect
import firebase_admin
import firebase_admin,pyrebase
from firebase_admin import credentials , firestore
from firebase_admin import credentials, initialize_app, storage
from .models import user_singup 

firebaseConfig = {
    "apiKey": "AIzaSyAvOY6_emeY0ZsdhA1s8x2NG0wNF7riYgw",
    "authDomain": "e-commers-web-page2.firebaseapp.com",
    "projectId": "e-commers-web-page2",
    "storageBucket": "e-commers-web-page2.appspot.com",
    "messagingSenderId": "852097607313",
    "appId": "1:852097607313:web:20cb7cf9bebe7e493c8130",
    "measurementId": "G-9FHK9WTB15",
    'databaseURL':"https://e-commers-web-page2-default-rtdb.firebaseio.com/",
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
eservice={
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

cred=credentials.Certificate(eservice)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
database = firestore.client()
storage = firebase.storage()

# ####### singup

def Singup(request):
    print('you are in customer singup ')
    Name=request.POST.get('name')
    Mobile_number =request.POST.get('Mobile_number')
    Email=request.POST.get('Email')
    password=request.POST.get('password')
    if Name != None and Mobile_number != None and Email != None and password != None:
        main_id=Name[::2]+Mobile_number[::3]+Email[::4]
        customer_data={
            'Name':Name,
            'Mobile_number':Mobile_number,
            'Email':Email,
            'password':password,
            'Type':'Customer',
            'userId':main_id,
        }
        new_user = user_singup(user_name = Name,Mobile_number= Mobile_number,user_email = Email,user_password = password,user_id= main_id)
        print(new_user)
        new_user.save()
        print(f'account oppen & data uplod complet of {Name}')
        return render(request,"login_page.html",{"c_data":customer_data})
    try:
        print(customer_data)
    except:
        print("customer Account cant't open ")
    return render(request,'Singup.html')

############ login
def user_login(request):
    print('you are in customer login page ')
    c_data = None
    c_data = request.session.get('c_data')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(f'{email} {password}')
    c_data=database.collection('customer').document(email).get().to_dict()
    request.session['c_data'] = c_data
    if c_data  : 
        if(c_data["Email"] == email and c_data["password"]==password and c_data["Type"]=="Customer"):
            print(c_data["Email"])
            # core=auth.sign_in_with_email_and_password(email,password)
            print('sayan basani command have to be fllow \n \n \n ok ok ok ')
            page_T={
                'page_T':"Customer"
            }
            c_data.update(page_T)
            print(c_data)
            print("sucess to sign up")
            return redirect("homepage:HomePage")
    else:
        print(f"fail to sign in: {email}")
    return render(request,"login_page.html")
def logOutCustomer(request):
    print("try to log out")
    return redirect('customer:user_login')

def cart(request):
    c_data = request.session.get('c_data')
    # print(f'customer data is {c_data}')
    c_Email = c_data['Email']
    # print(f'customer mail is {c_Email}')
    userCartData = database.collection('cart').document(c_Email).get().to_dict()
    # print(f'cart data of {c_Email} is \n{userCartData}')
    cartDataLen = len(userCartData)
    print(f'cart data lenth is {cartDataLen}')
    allCardItems = {}
    for i in range (0,cartDataLen):
        p_id = userCartData[str(i+1)]['productId']
        print(f'{i}th product id is : {p_id}')
        CartProductData = database.collection('Products').document(p_id).get().to_dict()
        # print(f'item {i} --> {CartProductData} \n')
        allCardItems.update({f'{i}':CartProductData})
        print(allCardItems)
        print('\n')
    return render(request , "cart.html",{'cartItems':allCardItems})
def order(request):
    return render(request , "order.html")
def product_list(request):
    c_data=request.session.get('c_data')
    # print(c_data)
    print('you are in produce list -------------------------------------------------------------')
    search = request.GET.get('search')
    print(f'User search {search}')
    docs = database.collection("Products").stream()
    # print(docs)
    product = []
    for doc in docs:
        p_data = doc.to_dict()
        for key, value in p_data.items():
            # print(f'{key} --> {value}')
            # print(f'{value} ===== {search}\n')
            if isinstance(value, str) and value.lower() == search.lower():
            # if value == "5":
                # print(f"{doc.id} => {doc.to_dict()} \n")
                print(p_data['Name'])
                product.append(p_data)
    print(type(product))
    # print(product)
    print('.....................................................')
    # print(p_data)
    return render(request , "product_list.html",{'c_data':c_data,'products':product})

def uplod(path):
    storage.child("Images").child('img.png').put(path)
    url = storage.child("Images").child('img.png').get_url(firebaseConfig['storageBucket'])
    r_url = str(url)
    return r_url    
