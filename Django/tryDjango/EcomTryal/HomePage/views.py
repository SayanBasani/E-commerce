from django.shortcuts import render,redirect,HttpResponse,HttpResponsePermanentRedirect,HttpResponseRedirect
from firebase_admin import credentials , storage , firestore
import firebase_admin , firebase ,pyrebase,json
from django.urls import reverse
import time

firebaseConfig = {
    # firebase config
}
eservice={
    # fire base service.js 
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
if not firebase_admin._apps:
    print("firebase_admin.initialize_app(cred) have to ineasealize ")
    cred = credentials.Certificate(eservice)
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

 