#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount= 0,total = 0,):
    self.discount = discount
    self.total = total
    self.items = []
    self.added_items = []
    self.last_item = 0
   

  def add_item(self,title,price,mod = 1):
    k = 0
    while k <mod:
      self.items.append(title)
      k += 1
   
      
    self.total += (mod * price)
    self.added_items.append(title)
    self.last_item = (price*mod)
    return self.added_items
    
    

  def apply_discount(self):
    
    if(self.discount == 0):
      print("There is no discount to apply.")
    else:
      self.total -= (self.total*(self.discount*.01) )
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= self.last_item
    
  
