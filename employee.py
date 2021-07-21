import psycopg2
from settings import *
from connection import Connection


class Employee(Connection):

    def __init__(self, first_name, last_name, date_of_birth, city, chief, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.city = city
        self.chief = chief
        self.login = login
        self.password = password

    def edit_self_info(self, data, selector):
        if self._login_check(self.login, self.password, 'employee'):
            table = 'employee'
            result = self._updateData(table, data, selector)
        else:
            result = 'Incorrect login or password'
        return result

    def change_order_status(self, data, selector):

        if self._login_check(self.login, self.password, 'employee'):
            table = ('orders',)
            result = self._updateData(table, data, selector)
        else:
            result = 'Incorrect login or password'
        return result


if __name__ == '__main__':
    employee = Employee('roma', 'romanich', '1953-02-03',
                        'London', 'Lok', 'roman', '1234')

    # data = {
    #     'first_name': "Roms",
    #     'last_name': "Lodm",
    #     'date_of_birds': "2003-04-10",
    #     'city_id': 2,
    #     'chief_id': 1
    # }
    # edit = employee.edit_self_info(data, "first_name = 'lopes'")
    # print(edit)
