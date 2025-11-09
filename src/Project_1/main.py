class CustomerDataClass:
   """Класс клиентов.

   Выполняет рассчёт чего-то.
   """

   def __init__(self,customerId,customerName):
      self.CustomerId=customerId
      self.CustomerName=customerName
      self.Orders=[]

   def AddOrder(self,orderObject):
      """Метод Создания заказов.

      :arg orderObject: Заказ клиента.
      """

      self.Orders.append(orderObject)

   def GetTotalAmount(self):
      """Метод Рассчёта суммы заказов.

      :arg self: Атрибуты класса.
      """

      total=0
      for o in self.Orders:
         total = total + o.amount
      return total


class OrderDataClass:
   """Класс заказов.

   Описание заказа
   """

   def __init__(self,orderId,amount):
      self.orderId=orderId
      self.amount=amount


def CalculateDiscount(customerObj):
   """Функция рассчёта скидки.

   :arg customerObj: Заказ клиента.
   """

   totalAmount = customerObj.GetTotalAmount()
   if totalAmount > 1000:
      discount=totalAmount*0.1
   else:
      discount = 0
   return discount


def PrintCustomerReport(customerObj):
   """Функция печати.

   :arg customerObj: Заказ клиента.
   """

   print("Customer Report for:",customerObj.CustomerName)
   print("Total Orders:", len(customerObj.Orders))
   print("Total Amount:", customerObj.GetTotalAmount())
   print("Discount:",CalculateDiscount(customerObj))
   print("Average Order:",customerObj.GetTotalAmount()/len(customerObj.Orders))



def MainProgram():
   """Основная функция.

   Функция вызова
   """

   c1=CustomerDataClass(1,"SAP Customer")
   o1=OrderDataClass(101,500)
   o2=OrderDataClass(102,800)
   c1.AddOrder(o1)
   c1.AddOrder(o2)

   PrintCustomerReport(c1)


# Вызов основной функции
MainProgram()