from django.contrib.auth.hashers import make_password, check_password

from django.shortcuts import render, redirect
from django.views import View

from .models.Product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order




# Create your views here.
class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')

        print(product)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart',request.session['cart'])

        return redirect('homepage')

    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}

        product = None
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if category_id:
            product = Product.get_all_products_by_categoryid(category_id)
        else:
            product = Product.get_all_products()

        data = {}
        data['product'] = product
        data['categories'] = categories

        print('You are :', request.session.get('email'))

        return render(request, 'index.html', data)

# ------------------------------------ Index ------------------------------------------------------

'''def index(request):
    product = None
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    if category_id:
        product = Product.get_all_products_by_categoryid(category_id)
    else:
        product = Product.get_all_products()

    data = {}
    data['product'] = product
    data['categories'] = categories

    print('You are :', request.session.get('email'))

    return render(request,'index.html',data)'''
# ------------------------------------ Validate Customer ------------------------------------------------------
def validateCustomer(customer):
    error_message = None
    if not customer.first_name:
        error_message = 'First name required!.'
    elif len(customer.first_name) < 2:
        error_message = 'First name must be more than 2 character!.'
    elif not customer.last_name:
        error_message = 'Last name required!.'
    elif len(customer.last_name) < 2:
        error_message = 'First name must be more than 2 character!.'
    elif not customer.phone:
        error_message = 'Phone number is required!.'
    elif len(customer.phone) < 9:
        error_message = 'Phone number must be more than 9 numbers!.'
    elif not customer.email:
        error_message = 'Email required!.'
    elif not customer.password:
        error_message = 'Password required!.'
    elif customer.isExists():
        error_message = 'Email address already registered!.'

    return error_message
# ------------------------------------ Register User ------------------------------------------------------
'''def registerUser(request):
    postdata = request.POST
    first_name = postdata.get('firstname')
    last_name = postdata.get('lastname')
    phone = postdata.get('phone')
    email = postdata.get('email')
    password = postdata.get('password')
    customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
    error_message = validateCustomer(customer)
    print(error_message)
    value = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email
    }
    # ------------------------------ validation ----------------------------------------
    error_message = None
    if not first_name:
        error_message = 'First name required!.'
    elif len(first_name)<2:
        error_message = 'First name must be more than 2 character!.'
    elif not last_name:
        error_message = 'Last name required!.'
    elif len(last_name)<2:
        error_message = 'First name must be more than 2 character!.'
    elif not phone:
        error_message = 'Phone number is required!.'
    elif len(phone)<9:
        error_message = 'Phone number must be more than 9 numbers!.'
    elif not email:
        error_message = 'Email required!.'
    elif not password:
        error_message = 'Password required!.'
    elif customer.isExists():
        error_message = 'Email address already registered!.'
       

    print(first_name, last_name, phone, email, password)

    # saving

    if not error_message:
        customer.password = make_password(customer.password)

        customer.register()
        return redirect('homepage')
    else:
        data = {
            'error': error_message,
            'values': value
        }
        return render(request, 'accounts/signup.html', data)'''

class Signup(View):
    def get(self,request):
        return render(request,'accounts/signup.html')

    def post(self,request):

        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        error_message = validateCustomer(customer)
        print(error_message)
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }


        print(first_name, last_name, phone, email, password)

        # saving

        if not error_message:
            customer.password = make_password(customer.password)

            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'accounts/signup.html', data)






'''def signup(request):
    if request.method == 'GET':
        return render(request,'accounts/signup.html')
    else:
        return registerUser(request)
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        error_message = validateCustomer(customer)
        print(error_message)
        value = {
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email': email
        }
        #validation
        error_message = None
        if not first_name:
            error_message = 'First name required!.'
        elif len(first_name)<2:
            error_message = 'First name must be more than 2 character!.'
        elif not last_name:
            error_message = 'Last name required!.'
        elif len(last_name)<2:
            error_message = 'First name must be more than 2 character!.'
        elif not phone:
            error_message = 'Phone number is required!.'
        elif len(phone)<9:
            error_message = 'Phone number must be more than 9 numbers!.'
        elif not email:
            error_message = 'Email required!.'
        elif not password:
            error_message = 'Password required!.'
        elif customer.isExists():
            error_message = 'Email address already registered!.'
            

        print(first_name,last_name,phone,email,password)




        #saving

        if not error_message:
            customer.password = make_password(customer.password)

            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'accounts/signup.html',data)'''


class Login(View):
    def get(self,request):
        return render(request, 'accounts/login.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print(customer)
        print(email, password)
        # -------------------------------------------------------------------------------------------------------
        error_message = None
        if customer:
            flag = check_password(password, customer[0].password)
            if flag:
                request.session['customer'] = customer[0].id

                return redirect('homepage')
            else:
                error_message = 'Email or password Invalid!.'
        else:
            error_message = 'Email or password Invalid!.'
        return render(request, 'accounts/login.html', {'error': error_message})


'''def login(request):
    if request.method == 'GET':
        return render(request,'accounts/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print(customer)
        print(email,password)
        # -------------------------------------------------------------------------------------------------------
        error_message = None
        if customer:
            flag = check_password(password,customer[0].password)
            if flag:
                return redirect('homepage')
            else:
                error_message = 'Email or password Invalid!.'
        else:
            error_message = 'Email or password Invalid!.

        # -------------------------------------------------------------------------------------------------------

        return render(request,'accounts/login.html',{'error':error_message})'''

def logout(request):
    request.session.clear()
    return redirect('login')



class Cart(View):
    def get(self,request):
        try:
            ids = list(request.session.get('cart').keys())
            print(ids)
            products = Product.get_products_by_id(ids)
            print(products)


        except Exception as e:
            print(e)
        return render(request, 'cart/cart.html',{'products':products})

class CheckOut(View):

    def post(self,request):

        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        product = Product.get_products_by_id(list(cart.keys()))
        print(address,phone,customer,cart,product)
        for product in product:
            order = Order(customer = Customer(id=customer),
                          product = product,
                          price = product.price,
                          address = address,
                          phone=phone,
                          quantity = cart.get(str(product.id))
            )
            order.placeOrder()
            request.session['cart'] = {}
        return redirect('cart')

'''def OrderView(request):

    customer = request.session.get('customer')
    print(customer)

    orders = Order.get_orders_by_id(customer)
    print(orders)
    return render(request,'orders/orders.html',{'order':orders})'''

class OrderView(View):

    def get(self,request):
        customer = request.session.get('customer')
        print(customer)

        orders = Order.get_orders_by_id(customer)
        print(orders)
        return render(request, 'orders/orders.html', {'orders': orders})



def search(request):
    search = request.POST.get('search')
    print(search)
    product = Product.objects.filter(name__icontains=search)
    print(product)
    return render(request,'product/search.html',context={'product':product})

