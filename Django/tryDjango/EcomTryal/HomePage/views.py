from django.shortcuts import render,redirect,HttpResponse,HttpResponsePermanentRedirect,HttpResponseRedirect
from firebase_admin import credentials , storage , firestore
import firebase_admin , firebase ,pyrebase,json
from django.urls import reverse
import time

firebaseConfig = {
    "apiKey": "AIzaSyAvOY6_emeY0ZsdhA1s8x2NG0wNF7riYgw",
    "authDomain": "e-commers-web-page2.firebaseapp.com",
    "projectId": "e-commers-web-page2",
    "storageBucket": "e-commers-web-page2.appspot.com",
    "messagingSenderId": "852097607313",
    "appId": "1:852097607313:web:20cb7cf9bebe7e493c8130",
    "measurementId": "G-9FHK9WTB15",
    'databaseURL':" ",
}
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

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
if not firebase_admin._apps:
    print("firebase_admin.initialize_app(cred) have to ineasealize ")
    cred = credentials.Certificate(service)
    firebase_admin.initialize_app(cred)
database = firestore.client()
# print(auth)


# Create your views here.
def HomePage(request):
    c_data = None
    print('c_data is : ')
    c_data = request.session.get('c_data')
    print(c_data)
    request.session['c_data']=c_data
    return render(request,'HomePage.html',{'c_data':c_data})
def produc(request):
    c_data = None
    c_data = request.session.get('c_data')
    # print(c_data)
    type = request.GET.get('type')
    id = request.GET.get('id')
    print(f'| product type is {type} | product is : {id} | ')
    p_data = database.collection(type).document(id).get().to_dict()
    print(f'data is {p_data}')
    return render(request , 'product.html',{'l_p_data':p_data})

def product(request):
    c_data = None
    c_data = request.session.get('c_data')
    # print(f'customer data is {c_data}')
    try :
        if request.session.get('id'):
            id = request.session.get('id')
        if request.GET.get('id'):
            id = request.GET.get('id')
        print(f'| product is : {id} | ')
        p_data = database.collection('Products').document(id).get().to_dict()
        # print(f'product data is {p_data}')
        return render(request , 'product.html',{'l_p_data':p_data,'id':id , 'c_data':c_data})
    except:
        id = None
        print(f'product data is ot found | id is {id}')
        return HomePage(request)
def addToCart(request):
    print("................................. working started .................................")
    id = request.GET.get('id')
    try:
        request.session['id']=id
        print("session create is sucess")
    except:
        print("session create is faill")
    print(f'product id is {id}')
    c_data = None
    # cartCount = 0
    c_data = request.session.get('c_data')
    import datetime
    carrentDate = str(datetime.datetime.now())
    print(carrentDate)
    if c_data != None :
        c_cart_data = database.collection('cart').document(c_data['Email']).get().to_dict()
        if c_cart_data != None:
            cartCount = len(c_cart_data)
            print(f'cart data is :{c_cart_data}\ncart value is {cartCount}')
        addCart = None
        if c_cart_data != None:
            print("working in part 1 ................./////////////////////.....................")
            # print(f'cart count is {c_cart_data['cartCount']}')
            print("sayan")
            addCart = {
                str(cartCount+1):{
                    'cartCount':cartCount+1,
                    'productId':id,
                    'Time':carrentDate,
                }
            }
            print(f'have to send this --->\n{addCart}')

            c_cart_data.update(addCart)
            print(f'have to send this data into database {c_cart_data != None}')
            i=0
            i_check = True
            while(i<cartCount):
                # print(f'count is{c_cart_data[str(i+1)]['productId']}')
                if c_cart_data[str(i+1)]['productId'] == addCart[str(cartCount+1)]['productId'] :
                    print("they are same")
                    i_check = False
                    break
                i+=1
            if (i_check):
                database.collection('cart').document(c_data['Email']).set(c_cart_data)
                print('uplod complit')
                c_data=database.collection('customer').document(c_data['Email']).get().to_dict()
                print(f' user data is : {c_data}')
                c_data.update({'cartCount':cartCount})
                database.collection('customer').document(c_data['Email']).set(c_data)
                print(f'newly user data is seted data is : {c_data}')
            else:
                print("it already into the cart")
            # data i add in user basic ditels (only the cart total product)
            # c_data=database.collection('customer').document(c_data['Email']).set(c_data)

            c_cart_data.update(addCart)
        else:
            print("working in part 2 ................./////////////////////.....................")
            cartCount = "1"
            addCart ={
                cartCount : {
                'cartCount':cartCount,
                'productId':id,
                'Time':carrentDate,
                }
            }
            print(f'have to send this --->\n{addCart}')
            # previous approtch
            # database.collection('cart').document(c_data['Email']).collection(cartCount).document('productData').set(addCart)
            # try new 
            database.collection('cart').document(c_data['Email']).set(addCart)
        print("cart function is working")
    if (c_data == None):
        print('you have to login ..................................??')
        return redirect(reverse('customer:user_login'))
    return redirect(reverse('homepage:product'))

 