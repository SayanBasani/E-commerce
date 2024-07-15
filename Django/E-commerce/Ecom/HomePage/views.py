from django.shortcuts import render,redirect
from django.urls import reverse
from django.core import serializers
import json
from Seller.models import all_product
from .models import cart

field_names = [field.name for field in all_product._meta.get_fields()]
field_cart = [field.name for field in all_product._meta.get_fields()]

# Create your views here.
def HomePage(request):
    c_data = None
    print('c_data is : ')
    c_data = request.session.get('c_data')
    print(c_data)
    request.session['c_data']=c_data
    return render(request,'HomePage.html',{'c_data':c_data})

def product_list(request):
    c_data=request.session.get('c_data')
    # print(c_data)
    print('you are in produce list -------------------------------------------------------------')
    search = request.GET.get('search')
    print(f'User search {search}')
    # docs = database.collection("Products").stream()
    # print(docs)
    product = []
    {
    # for doc in docs:
        # p_data = doc.to_dict()
        # for key, value in p_data.items():
            # print(f'{key} --> {value}')
            # print(f'{value} ===== {search}\n')
            # if isinstance(value, str) and value.lower() == search.lower():
            # if value == "5":
                # print(f"{doc.id} => {doc.to_dict()} \n")
                # print(p_data['Name'])
                # product.append(p_data)
    }
    product = all_product.objects.filter(description__icontains=search)
    for data_part in product:
        s_data = {field: getattr(data_part, field) for field in field_names}
        print(s_data)
        print('\n\n\n')
    print("..................................")
    print(product)
    # print(product)
    print('.....................................................')
    # print(p_data)
    return render(request , "product_list.html",{'c_data':c_data,'products':product})


def product(request):
    print('you are in product ditels')
    c_data = None
    c_data = request.session.get('c_data')
    try :
        if request.session.get('id'):
            id = request.session.get('id')
        if request.GET.get('id'):
            id = request.GET.get('id')
        print(f'| product is : {id} | ')
        p_data = all_product.objects.filter(product_id = id)
        for data_part in p_data:
            p_data = {field: getattr(data_part, field) for field in field_names}
        # print(f'product data is {p_data}')
        return render(request , 'product.html',{'l_p_data':p_data,'id':id , 'c_data':c_data})
    except:
        id = None
        print(f'product data is ot found | id is {id}')
        return HomePage(request)
def addToCart(request):
    print("................................. you are into cart section .................................")
    c_data = None
    c_data = request.session.get('c_data')
    id = request.GET.get('id')
    print(f'id is {id}')
    try:
        request.session['id']=id
        print("session create is sucess")
    except:
        print("session create is faill")
    print(f'product id is {id}')
    # cartCount = 0
    import datetime
    carrentDate = str(datetime.datetime.now())
    print(carrentDate)
    if c_data != None :
        addCart = None
        addCart = {
                'customer_id':c_data['main_id'],
                'productId':id,
                'quentity':'1',
                'Time':carrentDate,
            }
        try :
            print("working in part 1 ................./////////////////////.....................")            
            
            print(f'have to send this cart data is :--->\n{addCart}')
            print(c_data['main_id'])
            # customer_old_cart = cart.objects.create(**addCart)
            customer_old_cart = cart.objects.filter(customer_id = c_data['main_id'])
            print('in to part 2 .....................')
            isPresent=False
            for data_part in customer_old_cart:
                serialized_data = serializers.serialize('json', [data_part])
                data = json.loads(serialized_data)[0]['fields']
                print(data)
                print(addCart)
                if(data['productId'] == addCart['productId']):
                    isPresent = True 
                    break
                    print('it is not eligable for add into cart')
                elif(data['productId'] != addCart['productId']):
                    isPresent = False
                    print('it is eligable to add in to cart data')
            if (isPresent == False):
                cart.objects.create(**addCart)
                print('it is eigable to update the data base')

        except:
            print('cart data uplode fail')
            # print("working in part 2 ................./////////////////////.....................")
        print("cart function is working")
    if (c_data == None):
        print('you have to login ..................................??')
        return redirect(reverse('customer:user_login'))
    return redirect(reverse('homepage:product'))

