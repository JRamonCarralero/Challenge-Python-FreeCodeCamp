class Category:
    
    def __init__(self, name):
        self.ledger = []
        self.name = name
    
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, budget):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {budget.name}')
            budget.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        output = [] 
        output.append(f'{self.name:*^30}')
        for item in self.ledger:
            description = item['description']
            description = description[:23].ljust(23)
            amount = item['amount']
            formatted_amount_str = f'{amount:.2f}'
            if len(formatted_amount_str) > 7:
                formatted_amount_str = formatted_amount_str[:7] 
            formatted_amount = formatted_amount_str.rjust(7)

            output.append(f'{description}{formatted_amount}')
        
        total = self.get_balance()
        output.append(f'Total: {total:.2f}')

        return '\n'.join(output)


def create_spend_chart(categories):
    output = ['Percentage spent by category']
    total_spent = 0
    spent_by_category = {}
    len_names = 0
    names = []
    percentage_by_category = {}

    for category in categories:
        spent_by_category[category.name] = 0
        if len_names < len(category.name):
            len_names = len(category.name)
        names.append(category.name)
        movements = category.ledger
        for move in movements:
            if move['amount'] < 0:
                spent_by_category[category.name] += abs(move['amount'])
                total_spent += abs(move['amount'])

    for key, value in spent_by_category.items():
        if total_spent == 0: 
            percentage = 0
        else:
            percentage = (value / total_spent) * 100
        percentage = (int(percentage) // 10) * 10
        percentage_by_category[key] = percentage

    for pct in range(100, -1, -10):
        final_str = str(pct).rjust(3) + '|'
        for value in percentage_by_category.values():
            if value >= pct:
                final_str += ' o '
            else:
                final_str += '   '
        final_str += ' '
        output.append(final_str)
    
    horizontal_line = '    ' + ('---' * len(names)) + '-'
    output.append(horizontal_line)

    for i in range(len_names):
        final_str = '    '
        for name in names:
            if i < len(name):
                final_str += f' {name[i]} '
            else:
                final_str += '   '
        final_str += ' '
        output.append(final_str)

    return '\n'.join(output)