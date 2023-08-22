"""
Wrapping of data in a single unit

Public
private
protected
"""

class bank:
    def __init__(self, bname, btrans):
        self._name = bname
        self.__transact = btrans
b = bank('SBI',12345)

class cust(bank):
    def bank_data(self):
        print(self._name)    #protected
        #print(self.__transact)  #private
obj =cust('SBI',12345)
obj.bank_data()