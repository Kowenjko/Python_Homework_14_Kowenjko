from admin import Admin
from unregisteredCustomer import UnregisteredCuctomer
from registeredCustomer import RegisteredCustomer
from pprint import pprint
from custom import respprint
import datetime


admin1 = Admin('admin', 'admin')
orders = admin1.get_order_info()
# orders = admin1.get_order_info(category='city_name', selector='London')
# orders = admin1.get_order_info(category='date_of_order', selector='2020-6-12')
respprint(orders)
regCust = UnregisteredCuctomer()
orders = regCust.get_product_info(category='country_name', selector='France')
respprint(orders)
cust = RegisteredCustomer('roma', 'romanich',
                          'London', 'kolis', '457')
product = cust.get_product_info(
    category='category_name', selector='Fruits')
respprint(product)
