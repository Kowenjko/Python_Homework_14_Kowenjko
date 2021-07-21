import psycopg2
from settings import *
from connection import Connection


class RegisteredCustomer(Connection):

    def __init__(self, first_name, last_name, city, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.login = email
        self.password = password

    def login_self(self):
        return self._login_check(self.login, self.password, 'customer')

    def get_self_info(self, selector=''):
        role = 'customer'
        if self.login_self():
            table = ('customer',)
            fields = ('*',)
            selector = ''
            result = self._getData(table, fields, selector)
        else:
            result = 'Incorrect login or password'
        return result

    def create_order(self, data):
        role = 'customer'
        if self.login_self():
            table = 'orders'
            result = self._postData(table, data)
        else:
            result = 'Incorrect login or password'
        return result

    def delete_order(self, selector):
        role = 'customer'
        if self.login_self():
            table = 'orders'
            selector = f"date_of_order = '{selector}'"
            result = self._deleteData(table,  selector)
        else:
            result = 'Incorrect login or password'
        return result

    def get_product_info(self, category='', selector='',):
        """
        category must be one of the item from the list:
        ['product_name','country_name', 'category_name']        
        """
        if self.login_self():
            categoryes = ['product_name', 'country_name', 'category_name']
            table = ('product p',)
            fields = (
                """p.id, p.product_name ,p.unit_price,c.country_name,pc.category_name """,)
            fieldNames = ["id", "product_name", "unit_price",
                          "country_name", "category_name"]
            if category and category in categoryes and selector:
                where = f"""where {category} = '{selector}'"""
            else:
                where = ''

            selector = f""" inner join country c on c.id =p.country_id                             
                                inner join product_category pc on pc.id =p.product_catagery_id {where}"""
            result = self._getData(table, fields, selector)
            changeRes = []
            for item in result:
                cort = {}
                for index, element in enumerate(item):
                    cort[fieldNames[index]] = element
                changeRes.append(cort)
        else:
            changeRes = 'Incorrect login or password'
        return changeRes


if __name__ == '__main__':
    cust = RegisteredCustomer('roma', 'romanich',
                              'London', 'kolis', '457')
    # -------------------------------
    # data = [{
    #         'employee_id': 1,
    #         'city_id': 2,
    #         'date_of_order': '2021-04-10',
    #         'customer_id': 2,
    #         'product_id': 2,
    #         'price': 252
    #         }]
    # put = cust.create_order(data)
    # print(put)
    # -------------------------------
    # orders = cust.get_product_info()
    # print(orders)
    # -------------------------------
    # orders = cust.get_self_info()
    # print(orders)
    # -------------------------------
    # idf = cust._getNextId('orders')
    # print(idf)
    # -------------------------------
    # dele = cust.delete_order('2021-04-10')
    # print(dele)
