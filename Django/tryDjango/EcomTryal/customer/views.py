from django.shortcuts import render,redirect
import firebase_admin
import firebase_admin,pyrebase
from firebase_admin import credentials , firestore
from firebase_admin import credentials, initialize_app, storage
from .models import user_singup 

firebaseConfig = {
    # firebase config
}
eservice={
    # fire base service.js 
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
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
