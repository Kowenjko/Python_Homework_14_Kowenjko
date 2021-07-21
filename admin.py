import psycopg2
from settings import *
from connection import Connection
import datetime


class Admin(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def register_self(self):
        self._register(self.login, self.password, 'admin')

    def login_self(self):
        return self._login_check(self.login, self.password, 'admin')

    def add_product(self, data):
        if self.login_self():
            table = 'product'
            result = self._postData(table, data)
        else:
            result = 'Incorrect login or password'
        return result

    def add_pr_category(self, data):
        if self.login_self():
            table = 'product_category'
            result = self._postData(table, data)
        else:
            result = 'Incorrect login or password'
        return result

    def add_employee(self, login, password, data):
        if self.login_self():
            self._register(login, password, 'employee')
            table = 'employee'
            result = self._postData(table, data)
        else:
            result = 'Incorrect login or password'
        return result

    def delete_product(self, selector):
        if self.login_self():
            table = 'product'
            selector = f"product_name = '{selector}'"
            result = self._deleteData(table,  selector)
        else:
            result = 'Incorrect login or password'
        return result

    def delete_pr_category(self, selector):
        if self.login_self():
            table = 'product_category'
            selector = f"category_name = '{selector}'"
            result = self._deleteData(table,  selector)
        else:
            result = 'Incorrect login or password'
        return result

    def delete_employee(self, selector):
        if self.login_self():
            table = 'employee'
            selector = f"first_name = '{selector}'"
            result = self._deleteData(table,  selector)
        else:
            result = 'Incorrect login or password'
        return result

    def delete_customer(self, selector):
        if self.login_self():
            table = 'customer'
            selector = f"first_name = '{selector}'"
            result = self._deleteData(table,  selector)
        else:
            result = 'Incorrect login or password'
        return result

    def edit_product(self, data, selector):
        if self.login_self():
            table = 'product'
            result = self._updateData(table, data, selector)
        else:
            result = 'Incorrect login or password'
        return result

    def edit_pr_category(self, data, selector):
        if self.login_self():
            table = 'product_category'
            result = self._updateData(table, data, selector)
        else:
            result = 'Incorrect login or password'
        return result

    def edit_employee(self, data, selector):
        if self.login_self():
            table = 'employee'
            result = self._updateData(table, data, selector)
        else:
            result = 'Incorrect login or password'
        return result

    def get_order_info(self, category='', selector='',):
        """
        category must be one of the item from the list:
        ['city_name','date_of_order', 'product_name']
        date format for selector: 2020-6-12
        """
        if self.login_self():
            categoryes = ['city_name', 'date_of_order', 'product_name']
            table = ('orders o',)
            fields = ("""o.id, concat(e.first_name,' ', e.last_name) as "employee", c.city_name,
                         o.date_of_order, concat(c2.first_name,' ', c2.last_name) as "customer", p.product_name, o.price """,)
            fieldNames = ["id", "employee", "city_name",
                          "date_of_order", "customer", "product_name", "price"]
            if category and category in categoryes and selector:
                where = f"""where {category} = '{selector}'"""
            else:
                where = ''

            selector = f""" inner JOIN employee e on e.id = o.employee_id 
                            inner JOIN city c on c.id = o.city_id 
                            inner JOIN customer c2 on c2.id = o.customer_id 
                            inner JOIN product p on p.id = o.product_id {where}"""
            # fieldNames = fields.split(',')
            result = self._getData(table, fields, selector)
            changeRes = []
            for item in result:
                cort = {}
                for index, element in enumerate(item):
                    cort[fieldNames[index]] = element
                changeRes.append(cort)
                # print()
        else:
            changeRes = 'Incorrect login or password'
        return changeRes


if __name__ == '__main__':
    admin1 = Admin('admin', 'admin')
    orders = admin1.login_self()
    print(orders)
    # ----------------------------------
    # data = [{
    #         'category_name': "Coca"
    #         }]
    # put = admin1.add_pr_category(data)
    # print(put)
    # ----------------------------------
    # data = [{
    #         'product_name': "Cola",
    #         'unit_price': 253,
    #         'country_id': 2,
    #         'product_catagery_id': 5
    #         }]
    # put = admin1.add_product(data)
    # print(put)
    # ----------------------------------
    # data = [{
    #         'first_name': "Roms",
    #         'last_name': "Lom",
    #         'date_of_birds': "1953-04-10",
    #         'city_id': 1,
    #         'chief_id': 2
    #         }]
    # put = admin1.add_employee(data)
    # print(put)
    # ----------------------------------
    # data = [{
    #         'login': "Coca556",
    #         'password': "coca3"
    #         }]
    # put = admin1.register_self(data)
    # print(put)
    # # ----------------------------------
    # idf = admin1._getNextId('login')
    # print(idf)
    # ----------------------------------
    # data = {
    #     'product_name': "Water",
    #     'unit_price': 153,
    #     'country_id': 3,
    #     'product_catagery_id': 1
    # }
    # edit = admin1.edit_product(data, "product_name = 'Cola'")
    # print(edit)
    # ----------------------------------
    # data = {
    #     'first_name': "lopes",
    #     'last_name': "Lodm",
    #     'date_of_birds': "2003-04-10",
    #     'city_id': 2,
    #     'chief_id': 1
    # }
    # edit = admin1.edit_employee(data, "first_name = 'Roms'")
    # print(edit)
    # ----------------------------------
    # data = {
    #     'category_name': "Water"
    # }
    # edit = admin1.edit_pr_category(data, "category_name = 'Coca'")
    # print(edit)
    # ----------------------------------
    # log = admin1._connectDb('admin', 'admin')
    # print(log)
    # ----------------------------------
    # dele = admin1.delete_pr_category('Water')
    # print(dele)
    # ----------------------------------
    # dele = admin1.delete_product('Cola')
    # print(dele)
    # ----------------------------------
    # dele = admin1.delete_employee('Roms')
    # print(dele)
    # ----------------------------------
    # dele = admin1.delete_customer('Rola')
    # print(dele)
