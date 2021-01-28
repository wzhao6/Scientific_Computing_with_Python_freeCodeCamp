class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0    

    
    def deposit(self, amt, des=None):
        if des == None:
            des = ''
        self.ledger.append({"amount": amt, "description": des})
        self.balance += amt

    def withdraw(self, amt, des=None):
        if des == None:
            des = ''
        if self.check_funds(amt):
            self.ledger.append({"amount": -amt, "description": des})
            self.balance -= amt
            return True
        return False


    def get_balance(self):
        return self.balance

    def transfer(self, amt, bud_cat):
        if self.check_funds(amt):
            self.ledger.append({"amount": -amt, "description": 'Transfer to '+ bud_cat.name})
            bud_cat.ledger.append({"amount": amt, "description": 'Transfer from ' + self.name})
            self.balance -= amt
            bud_cat.balance += amt
            return True

        return False 

    def check_funds(self, amt):
        if self.balance >= amt:
            return True
        return False
    #called when the object is printed or str():

    def __str__(self):
        s = '*'*((30-len(self.name))//2) + self.name
        s += '*'*(30-len(s)) + '\n'
        for x in self.ledger:
            s+= '{:<23}{:>7.2f}'.format(x['description'][:23], x['amount']) + '\n'
        s += 'Total: {}'.format(self.balance)
        return s

def r_down_tens_percent(ls):
    return [int(x*10)*10 for x in ls]


def create_spend_chart(categories):
    withdraw = []
    withdraw_tot = 0
    withdraw_rounded = []

    for x in categories:
        amt = 0
        for i in x.ledger:
            #add all the withdraws 
            if i['amount'] < 0:
                amt += -i['amount']
        withdraw.append(amt)

    withdraw_tot = sum(withdraw)
    withdraw_rounded = r_down_tens_percent([x/withdraw_tot for x in withdraw])
    s = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        s_percent=''
        for x in withdraw_rounded:
            if x >= i:
                s_percent += ' o '
            else: s_percent += '   '
        s += '{:>3}|{} \n'.format(i, s_percent)

    dash = '-'*(3*len(withdraw_rounded)+1)
    s += '{:>{w}}\n'.format(dash, w=len(dash)+4)
    name = []
    for category in categories:
        name.append(category.name)
    mlen = max([len(x) for x in name])

    s_name = ''
    for i in range(mlen):
        s_namel = ''
        for j in name:
            if i >= len(j):
                s_namel += '   '
            else: s_namel += ' {} '.format(j[i])
        if i == mlen-1:
            s_name += '{:>{w}} '.format(s_namel, w=len(dash)+3)
        else: s_name += '{:>{w}} \n'.format(s_namel, w=len(dash)+3)
    s += s_name
    return s











            
        
            


