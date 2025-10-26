# Класс1
class CustomerDataClass:
    """Это класс 1.

    Описание класса.
    """

    def __init__(self, customerId,customerName):
        self.CustomerId=customerId
        self.CustomerName=customerName
        self.Orders=[]

    def AddOrder(self,orderObject):
        """Метод 1.

        Описание метода
        """

        self.Orders.append(orderObject)

    def GetTotalAmount(self):
        total=0
        for o in self.Orders:
            total = total + o.amount
        return total

# Класс2
class OrderDataClass:
    """Это класс 2.

    Его описание.
    """

    def __init__(self,orderId,amount):
        self.orderId=orderId
        self.amount=amount

# Функция 1
def CalculateDiscount(customerObj):
    totalAmount = customerObj.GetTotalAmount()
    if totalAmount > 1000:
        discount=totalAmount*0.1
    else:
        discount = 0
    return discount

# Функция 2
def PrintCustomerReport(customerObj):
    print("Customer Report for:",customerObj.CustomerName)
    print("Total Orders:", len(customerObj.Orders))
    print("Total Amount:", customerObj.GetTotalAmount())
    print("Discount:",CalculateDiscount(customerObj))
    print("Average Order:",customerObj.GetTotalAmount()/len(customerObj.Orders))

# Функция 3
def MainProgram():
    c1=CustomerDataClass(1, "SAP Customer")
    o1=OrderDataClass(101,500)
    o2=OrderDataClass(102,800)
    c1.AddOrder(o1)
    c1.AddOrder(o2)

    PrintCustomerReport(c1)

MainProgram()