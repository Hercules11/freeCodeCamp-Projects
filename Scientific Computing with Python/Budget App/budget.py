class Category:

    def __init__(self, cate=""):
        self.total = 0
        self.ledger = []
        self.cate = cate

    def check_funds(self, amount):
        if amount > self.total:
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        self.total += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.total -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def get_name(self):
        return self.cate

    def get_ledger(self):
        return self.ledger

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, description=f"Transfer to {category.get_name()}")
            category.deposit(amount, description=f"Transfer from {self.get_name()}")
            return True
        else:
            return False

    def __str__(self):
        head_line = self.cate.center(30, '*')
        content_line = ''.join(
            [el["description"][:23].ljust(23) + str("%.2f" % el["amount"]).rjust(7) + '\n' for el in
             self.ledger])
        tail_line = f"Total: {self.total}"
        return head_line + '\n' + content_line + tail_line


def max_length(arith):
    max_len = 0
    for el in arith:
        if len(el) > max_len:
            max_len = len(el)
    return max_len


def create_spend_chart(categories):
    cate_name = [el.get_name() for el in categories]
    cate_cost = []
    for el in categories:
        total = 0
        for entry in el.get_ledger():
            if entry["amount"] < 0:
                total += entry["amount"]
        cate_cost.append(total)
    cost_percentage = [int(el / sum(cate_cost) * 10) for el in cate_cost]
    circle_notation = [('o' * (el + 1) + ' ' * (11 - el)) for el in cost_percentage]
    name_axios = [(el + ' ' * (max_length(cate_name) - len(el))) for el in cate_name]
    head_Line = "Percentage spent by category"
    up_axios = ""
    for i in range(10, -1, -1):
        line = ''.join([' ' + el[i] + ' ' for el in circle_notation]) + ' '
        up_axios += (str(i * 10).rjust(3) + '|' + line + '\n')
    delimiter_line = ' ' * 4 + '-' * len(cate_name) * 3 + '-'
    down_axios = ""
    for i in range(max_length(cate_name)):
        line = ''.join([' ' + el[i] + ' ' for el in name_axios])
        down_axios += (' ' * 4 + line + ' ' + '\n')
    print(head_Line + '\n' + up_axios + delimiter_line + '\n' + down_axios)
    return head_Line + '\n' + up_axios + delimiter_line + '\n' + down_axios.rstrip('\n')
