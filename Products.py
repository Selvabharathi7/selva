from Payment import payment
import itertools

import abc
class Food(metaclass=abc.ABCMeta): 

    @abc.abstractmethod 
    def breakfast(self): 
        pass

class item(Food):
    def breakfast(self):
        item = ["Idli","Poori","Dosa","Pongal","Coffee"]
        price = [40,50,50,60,30]
        quantity = [0,0,0,0,0]
        for (count,i) in enumerate(zip(item,itertools.cycle('-'),price)):
            print(count+1,*i)
        total_sum = 0
        choice = 1
        while(choice != 0):
            while True:
                try:
                    choice = int(input("Enter the Product No: "))
                    if(choice == 0 ):
                        break
                    total_sum += price[choice -1]
                    quantity[choice -1] +=1
                except Exception:
                    print("Provide Valid Input")
        for j in  range(len(quantity)):
            if quantity[j] > 0:
                print(item[j],quantity[j])
        print("The Total Price - ",total_sum)
        payment.pay()   
        
    def dinner(self):
        Item = ["Paratha","Chapathi","Noodles","Fried Rice"]
        Price = [50,40,60,80]
        Quantity = [0,0,0,0]
        for (count,i) in enumerate(zip(Item,itertools.cycle('-'),Price)):
            print(count+1,*i)
        total_Sum = 0
        Choice = 1
        while(Choice != 0):
            try:
                while True:
                    Choice = int(input("Enter the Product No: "))
                    if(Choice == 0):
                        break
                    total_Sum += Price[Choice -1]
                    Quantity[Choice -1] +=1
            except Exception:
                    print("Provide Valid Input")
        for z in  range(len(Quantity)):
            if Quantity[z] > 0:
                print(Item[z],Quantity[z])
        print("The Total Price - "+ str(total_Sum))
        payment.pay()
        
item()

