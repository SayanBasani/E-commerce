from django.shortcuts import render,redirect
import firebase_admin
import firebase_admin,pyrebase
from firebase_admin import credentials , firestore
from firebase_admin import credentials, initialize_app, storage
from customer.models import user_singup

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
############ login
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

def cart(request):
    c_data = request.session.get('c_data')
    c_Email = c_data['Email']
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
def product_list1(request):
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

def allOrders(request):
    return render(request , "allOrders.html")

def aboutOrder(request):
    return render(request,'aboutOrder.html')