from Bank import bank

class BankAccount():

    def _init_(self):
        pass

    def create_acc(self,accType,name,balance,pin,interestrate):
        self._pin = pin
        self._accNo = 999
        self._accType = accType
        self._name = name
        self._interest = interestrate
        if self._accType == "SA":
            if balance>=5000:
                self._balance = balance
            else:
                print("less balance to start the account")
                self._accType = None
                self._name = None
        elif self._accType == "ODA":
            self._eStatement = list()
            self._eStatement.append(balance)
            self._balance = balance
        else:
            self._balance = balance

    def withdraw(self,amt):
        if self._accType == "SA":
            if self._balance-amt>=5000:
                self._balance = self._balance-amt
            else:
                print(f'Not able to withdraw {amt}')
        elif self._accType == "ODA":
            maximum_bal = max(self._eStatement)
            limit = self._balance+maximum_bal*0.1
            if  limit-amt>=0:
                    print("Limit:",limit)
                    print("state",self._eStatement)
                    odFee = 0
                    if self._balance-amt<0:
                        odFee = (self._balance-amt)*0.01
                        print(f'odFee:{odFee}')
                    self._balance = self._balance - amt + odFee
            else:
                print("The witdraw amount is off Limit")
        else:
            if self._balance - amt>=0:
                self._balance = self._balance - amt
            else:
                print(f'Low Balance')



    def deposit(self,amt):
        self._balance = self._balance + amt
        if self._accType=="ODA":
            self._eStatement.append(self._balance)
         
    def transfer(self,senderACC,amt,pin):
        if self._accType == "SA" and self._pin == pin:
            if self._balance-amt>=5000:
                 senderACC._balance += amt
                 self._balance = self._balance-amt
            else:
                print(f'Low balance')
        elif self._accType == "ODA"and self._pin == pin:
            maximum_bal = max(self._eStatement)
            limit = self._balance+maximum_bal*0.1
            if  limit-amt>=0:
                    print("Limit:",limit)
                    print("state",self._eStatement)
                    odFee = 0
                    if self._balance-amt<0:
                        odFee = (self._balance-amt)*0.01
                        print(f'odFee:{odFee}')
                    self._balance = self._balance - amt + odFee
                    senderACC._balance = amt
            else:
                print("The witdraw amount is off Limit")
        elif self._pin == pin:
            if self._balance - amt>=0:
                self._balance = self._balance - amt
                senderACC._balance += amt

            else:
                print(f'Low Balance')
        else:
            print("Invalid Pin")


    def creditInterest(self):
        if self._accType == "SA":
            self._balance = self._balance + self._balance*self._interest/100
        elif self._accType == "ODA":
            if self._balance > 0:
                self._balance = self._balance + self._balance*self._interest/100
        else:
            print("No Interest on Current Account")
class atm(bank,BankAccount):
    def _init_(self, bname, address, ifsc):
        bank._init_(self,bname, address, ifsc)
        BankAccount._init_(self)

    def create(self,accType,name,balance,pin,interestrate):
        super().create_acc(accType,name,balance,pin,interestrate)

    def withdraw(self, amt):
        return super().withdraw(amt)
    
    def deposit(self, amt):
        return super().deposit(amt)
    
    def creditInterest(self):
        return super().creditInterest()

    def info(self):
        print("*"*100)
        print(f'ACCNUM:{self._accNo}\tNAME:{self._name}\nAccType:{self._accType}\tBALANCE:{self._balance}')
        print("_"*100)            