import unittest
from client3 import *

#use the same data set
quotes = [
  {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
  {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
]

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):

    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       print(quote['stock'])
       self.assertEqual(getDataPoint(quote),(quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']/2) ) )

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       if quote['top_bid']['price']>quote['top_ask']['price']:
        print(quote['stock'])
        self.assertEqual(getDataPoint(quote),(quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']/2) ) )
  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    prices = {}
    for quote in quotes:
      #get dictionary {{'stock': (bid_price, ask_price, price)}
      prices[quote['stock']] = getDataPoint(quote)[1:]

    #print(prices)
    self.assertEqual(getRatio(prices["ABC"][2], prices["DEF"][2]), (prices["ABC"][2]/prices["DEF"][2]))

if __name__ == '__main__':
    unittest.main()
