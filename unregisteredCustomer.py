import psycopg2
from settings import *
from connection import Connection


class UnregisteredCuctomer(Connection):

    def register_self(self, login, password, data):
        self._register(login, password, 'customer')
        table = 'customer'
        result = self._postData(table, data)
        return result

    def get_product_info(self, category='', selector='',):
        """
        category must be one of the item from the list:
        ['product_name','country_name', 'category_name']        
        """

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

        return changeRes


if __name__ == '__main__':
    regCust = UnregisteredCuctomer()
    orders = regCust.get_product_info()
    print(orders)
    # ----------------------------------

    # data = [{
    #     'city_id': 2,
    #     'first_name': "Loman",
    #     'last_name': "Mipol"
    # }]
    # put = regCust.register_self('Petro', 'Petrow', data)
    # print(put)
