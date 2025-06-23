class Category:
    
    def __init__(self, name):
        """
        Initializes a new Category object.

        Parameters:
            name (str): The name of the Category as a string.
        """
        self.ledger = []
        self.name = name
    
    def deposit(self, amount, description = ''):
        """
        Adds a deposit to the ledger.

        Parameters:
            amount (int): The amount to add as an integer.
            description (str, optional): A description of the deposit as a string.
                Defaults to an empty string.
        """
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        """
        Withdraws a given amount from the budget category when the budget has enough funds.

        Parameters:
            amount (int): The amount to withdraw as an integer.
            description (str, optional): A description of the withdrawal as a string.
                Defaults to an empty string.

        Returns:
            bool: A boolean indicating whether the withdrawal was successful.
        """
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        """
        Calculates and returns the current balance of the budget category.

        Returns:
            float: The current balance as a floating-point number.
        """
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, budget):
        """
        Transfers a given amount from the current budget category to the specified budget category
        if the current budget has enough funds.

        Parameters:
            amount (int): The amount to transfer as an integer.
            budget (Category): The budget category to transfer funds to.

        Returns:
            bool: A boolean indicating whether the transfer was successful.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {budget.name}')
            budget.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        """
        Checks whether the budget category has enough funds for a given amount.

        Parameters:
            amount (int): The amount to check against the budget category's balance.

        Returns:
            bool: A boolean indicating whether the budget category has enough funds.
        """
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        """
        Returns a string representation of the budget category.

        The returned string includes the category name, followed by a table of
        all transactions in the ledger, with the description left-aligned and
        the amount right-aligned. The total balance is displayed after the
        table.

        Returns:
            str: A string representation of the budget category.
        """
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
    """
    Creates a bar chart representing the percentage of total spending by category.

    The function takes a list of Category objects as input and returns a string
    containing the bar chart.

    The bar chart will have a title, a horizontal line with tick marks, and
    vertical bars representing the percentage spent in each category. The
    vertical bars will be labeled with the category name and the percentage
    of total spending will be displayed above each bar.

    The returned string will be suitable for printing to the console.

    Parameters:
        categories (list): A list of Category objects.

    Returns:
        str: A string containing the bar chart.
    """
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