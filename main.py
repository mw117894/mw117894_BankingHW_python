class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)


class Account:
    last_id = 0

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def deposit(self, amount):
        operation_successful = False
        if type(amount) not in [int, float] or amount < 0:
            print("Amount of wrong type or negative value. You can deposit only numbers bigger than 0")
        else:
            self._balance += amount
            print("{} units deposited on account {}. Current balance is: {}".format(amount, self.__repr__(),
                                                                                    self._balance))
            operation_successful = True
        return operation_successful

    def charge(self, amount):
        operation_successful = False
        if type(amount) not in [int, float] or amount < 0 or self._balance - amount < 0:
            print("Amount of wrong type, negative value or too big. You can charge only numbers bigger than 0 but "
                  "smaller than balance value")
        else:
            self._balance -= amount
            print("{} units charged on account {}. Current balance is: {}".format(amount, self.__repr__(),
                                                                                  self._balance))
            operation_successful = True
        return operation_successful

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.lastname, self._balance)


class SavingsAccount(Account):
    pass


class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.account_list = []
        self.customer_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer, is_savings=False):
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.account_list.append(a)
        return a

    def transfer(self, from_acc_id, to_acc_id, amount):
        if from_acc_id.charge(amount):
            to_acc_id.deposit(amount)
        pass

    def __repr__(self):
        return 'Bank[{},{}]'.format(self.customer_list, self.account_list)


b = Bank()
c = b.create_customer('Anne', 'Smith')
b.create_account(c)
c2 = b.create_customer('John', 'Brown')
b.create_account(c2, is_savings=True)

acc1 = b.account_list[0]
acc2 = b.account_list[1]

print("Trying to deposit a non-numeric value")
acc1.deposit("1")
print("\nTrying to deposit a negative value ")
acc1.deposit(-1)
print("\nTrying to deposit an acceptable value")
acc1.deposit(1000)

print("\n",b)

print("\nTrying to transfer a non-numeric value")
b.transfer(acc1,acc2,True)
print("\nTrying to transfer a negative value ")
b.transfer(acc1,acc2,-1)
print("\nTrying to charge acc1 a bigger value than its balance")
b.transfer(acc1,acc2,1001)
print("\nTrying to transfer an acceptable value")
b.transfer(acc1,acc2,500)

print("\n",b)
