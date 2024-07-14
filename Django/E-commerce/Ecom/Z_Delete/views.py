from django.shortcuts import render,redirect
from django.urls import reverse
import firebase,pyrebase,firebase_admin
from firebase_admin import credentials , firestore
import json

firebaseConfig = {
  'apiKey': "AIzaSyA1l6YTxtr8Xx7KcdPytaKs2YsGblMMNJk",
  'authDomain': "e-commers-web-page.firebaseapp.com",
  'projectId': "e-commers-web-page",
  'storageBucket': "e-commers-web-page.appspot.com",
  'messagingSenderId': "620595830414",
  'appId': "1:620595830414:web:9456fb464b28906f7d73df",
  'measurementId': "G-XQFMT37DGZ",
  'databaseURL':" ",
}
service={
  "type": "service_account",
  "project_id": "e-commers-web-page",
  "private_key_id": "cd7097f68e100d1f20e677f5d52d434852f1fd8e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDUvkUac1UUrBwm\nqxjLN8boYw6mJNKscNvC1uQ3ZWgzw2tabLKeWjHGJFULaJFocRqc3qi90qI4OG0u\n7ejg/UJFz05GrWHo/+J4+RoHH2Y0aO1CoOIawzW3ar5bbU0YUiDI5f1XG7doU/1t\nbhVZlcYTjoCEtHyepZO8hU4wIVGycp1x+uenrQO5geYWBeNAiLB4udTkOeaiA6HE\nK5X8gVY87OYJldzQSSB2PiwFczMYwShvuS/+qi2IjhxBjUapFLGyr64BGfDWWAll\nki/PQE6Ex+oqXQBYHk/1Zn9YUkh13H1UFWKfhoVh7GH2FBgLs5kefoCh5aasdJIA\nFSQ2vrxdAgMBAAECggEABlpMK/cHsl9VU95GFkNrICNdG57734RbO505IWJY0zrh\nqMiYKNxeoiERnQ6ZUPoXplmLxmdUysL8l6spChbl9Lm1B61DwDZr59rgaRgJ8ES1\n2Qh+1/e+UeTRHF/OLoy9R+J+RyyftHDVn3/rCUrMqGbX9Z6CHiapm7aLWCqWivKN\nSjDaIqGx3URL6crhRC0Hnb5ba4P5PgwObKvk8CdCeHdHbWmTzJQblkRbdLpnZaz4\nv2nUW6zEj8Ey5/dXRwVkWlzfcRwxhOgZ1FOu6slqpN5DqyAGiTUNHwVtCdgEMw0o\nUhhhH/VzY5cb4eRjeUmTyrZ80JoRLH2m+/eqET/q4QKBgQDubhPlimuJda5BR0MP\n2aZBVunSZaKNEz8P8yhLOhxTAvNDP5qmH7+7L19iQsgZEmSQHp6tZfI9hkzlvMKt\nOKJDcKSFB1Gdj4y6w5CBkFx7sBxduFXodzHyP5o71HrYq7VCaV/2CRxDkZzA+aNg\nSRo+CPujdvgP2cZ7GNvzLMYX5QKBgQDka5473r/oi32tKwLJD3aKgGS43R38zxao\ne4z1M6b9xKtLDd9Sqb8jTF8mwcVg6jBTMox6ShVwAYBPFwHms7pUIKgpG9dqz0gB\nh0D2QwhDjcggV+e+HF28zSRK75+0dRQVNbQWVoDXlrA8yJpmLPFh2SuLAXnZdt9X\n9314mshbGQKBgQDT2Zz2LHqGZbjSKbZtg+8USVxy5Hl9LievTVd1GAoIvCtXilEn\n4Dfk4x+2WC4hENWntH07BsUpY4Y57vFvJk4O7CxSQwGCpQTfAVsJtDJoeD+MCnjS\nl+4aF+c71/zbPh5NBwILw2aIpv4H/QfsSqf1jNfCE7gvpUmVIK52MEdG/QKBgQDY\nEl0qMTnEFj+aEXefDfuKZI3iuXfmb1b1pXnfcS7kGqgWZVb9cQkXsOTJWr8FQELa\nUJTGEVJaE3F2X0MzIox9jC7GREnwBYgNug3fZeVpUbMftUfIdDjPohZUtHuUTrPi\npFxoTQev6CFqPjCfup/TeYVRBuJmraX0Jm8QKQqh8QKBgD+kIN8OJupy+OmFtgI4\nVYPQb4Jua6pCYJZOS6G4TloXdbchMejn67O0VB/k3s3JBG3neoD72n/RiX/Hno3U\nQxrxUYJw6r53tMSv4oDui7hS4dnJ7PNVdH+Wi1WGP+CC2BFi2qtnfpDhxgtk/1F0\nWBnLvrTbyQ+Z5xtf6GVIxe+S\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-1uno3@e-commers-web-page.iam.gserviceaccount.com",
  "client_id": "110276546586494629783",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1uno3%40e-commers-web-page.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


cred = credentials.Certificate(service)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
database = firestore.client()
# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()

# Create your views here.
def HomePage(request):
    return render(request,'SellerHom.html')

def Seller_Singup(request):
    Name=request.POST.get('name')
    Mobile_number=request.POST.get('Mobile_number')
    Email=request.POST.get('Email')
    password=request.POST.get('password')
    customer_data={
        'Name':Name,'Mobile_number':Mobile_number,'Email':Email,'password':password,'Type':'Seller',
    }
    try:
        main_id="Sell"+Name[::2]+Mobile_number[::3]+Email[::4]
        customer_data['main_id']=main_id
        database.collection('Seller').document(Email).set(customer_data)
        print(f'Seller account oppen & data uplod complet of {Name}')
        return render(request,'Seller-login_page.html',{ "data" :customer_data })
    except:
        print("Account cant't open")
    return render(request,'Seller-Singup.html')


def Seller_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    # email='1st@g.com'
    password='123456'
    print(f'{email} {password}')
    data=database.collection('Seller').document(email).get().to_dict()
    
    if data  : 
        if(data["Email"] == email and data["password"]==password ):
            print(data)
            print("Seller sucess to sign up")
            request.session['data'] = data
            # return sellerHome(request, data)
            return render(request,'sellerHome.html',{'data':data})
    else:
        print(f"fail to sign in: {email}")
    return render(request,'Seller-login_Page.html')



def sellerHome(request):
    data = 11
    if data is None:
        data = request.session.get('data', {})
    print("..................................................")
    print(data)
    # print(data['Name'])
    print("..................................................")
    seller_id = data['main_id']
    print(seller_id)
    return render(request,"sellerHome.html",{'seller_id':seller_id,'data':data})
# def sellerHome(request,data ):
#     print("..................................................")
#     print(data)
#     # print(data['Name'])
#     print("..................................................")
#     seller_id = data['main_id']
#     print(seller_id)
#     return render(request,"sellerHome.html",{'seller_id':seller_id,'data':data})
{            # def sellerHome(request , data):
            #     seller_id = data['main_id']
            #     return render(request,"sellerHome.html",{'seller_id':seller_id,'data':data})
}

# def sellerUplod(request ):
#     Name = request.POST.get('name')
#     print('\n \n \n')
#     data = request.GET
#     print(data)
#     print("data uplod Succesfull")
#     for i in data.items():
#         print(i)
#     print("the first type *********************")  
#     print(data['data'])
#     # for key, value in data.items():
#     #     print(value)
        
#     if Name != None:
#         return render(request,'UplodSuccesfull.html',{'Name':Name,'data':data})
#     else:
#         print("It uploding not complit")
#     return render(request,'sellerUplod.html',{'s':data,'data':data})




def sellerUplod(request ):
    # main_id = request.GET.get('i')
    email = request.GET.get('email')
    print('...............................................................................')
    print(email)
    
    data = database.collection('Seller').document(email).get().to_dict()
    # main_id = data['main_id']
    print(data)
    # print(main_id + " " + email+" \n")
    Name = request.POST.get('name')
    price = request.POST.get('price')
    descreption = request.POST.get('descreption')
    UplodedProduct_data= {
        'Name':Name,'price':price,'descreption':descreption
    }
    select_opt = request.POST.get('hidden_data')
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
            'User':User,'waight':waight,"option":option
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
    ok=database.collection('Products').document(select_opt).collection('Products').document(Name).set({
        'UplodedProduct_data':UplodedProduct_data,
        'Seller_data':data,
    })
    print(ok)
    print("data uplod Succesfull")
    print(UplodedProduct_data)
    if Name != None:
        return render(request,'UplodSuccesfull.html',{'Name':Name,'data':data})
        # return uplodSucessFull(request,Name)
    else:
        print("It uploding not complit")
    return render(request,'sellerUplod.html',{'s':email,'data':data})




def uplodSucessFull(request,Name):
    print(" after sucessfull uplod name is "+Name)
    return render(request,'UplodSuccesfull.html')