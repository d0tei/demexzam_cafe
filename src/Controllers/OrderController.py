from src.Models.Orders import *

from src.Models.Orders import *

class OrderController:
    def get(self):
        return Orders.select()
    def add(self,count_cliens, table_id,drink_id, food_id, shift_id):
        Orders.create(count_cliens = count_cliens, table_id = table_id, drink_id = drink_id, food_id = food_id, shift_id = shift_id,status_id = 3)



    @classmethod

    def update_order_pay(cls,order_id):
        Orders.update({Orders.status_id : 2}).where(Orders.id == order_id).execute()

    def update_order_ready(cls,order_id):

        Orders.update({Orders.status_id: 4}).where(Orders.id == order_id).execute()

    def update_oficiant(self,id_orders):
        Orders.update({Orders.status_id: 2}).where(Orders.id == id_orders).execute()

    @classmethod
    def show_1(cls,shift_id):
        return Orders.select().where(Orders.shift_id == shift_id)

    @classmethod
    def update_order_cooking(cls,order_id):
        Orders.update({Orders.status_id : 3}).where(Orders.id == order_id).execute()

    @classmethod
    def get_1(cls):
        return Orders.select()

if __name__ == '__main__':
    orders = OrderController()

    #OrderController.update_order_pay(2)
    for order in orders.get():
        print(order.id, order.count_cliens,order.table_id)
    print('-------------------')

    for row in orders.show_1(2):
        print(row.id, row.count_cliens, row.table_id.number, row.drink_id.name, row.food_id.name, row.shift_id.id, row.status_id.name)
    OrderController.update_order_cooking(2)



    print('-------------------')
    orders.add(1,1,1,1,1)

    for row in orders.get():
        print(row.id, row.count_cliens, row.table_id.number, row.drink_id.name, row.food_id.name, row.shift_id.id, row.status_id.name)




