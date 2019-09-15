"""
Description:
Author:qxy
Date: 2019-06-30 22:50
File: strategy_mode 
"""


from abc import ABC, abstractmethod
from collections import namedtuple


Customer = namedtuple('Customer', 'name fidelity')


class LineTtem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.proice = price

    def total(self):
        return self.quantity * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {.2f} due:{:2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """返回折扣金额（正值）"""


class FidelityPromo(Promotion): # 第一个具体策略

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion): # 第二个具体策略

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):

    def discount(self, order):
        distinct_item = {item.product for item in order.cart}
        if len(distinct_item) >= 10:
            return order.total() * .07
        return 0
