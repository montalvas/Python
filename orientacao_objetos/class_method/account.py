class Account():
    """Model of a account class
    
    Args:
        total_accounts (int): Total of accounts registered
    
    Methods:
        __init__: Initiate instance attributes
        get_info_account: Gets the information of a registered account
        get_total_accounts: Gets the total of accounts registered
    """
    
    total_accounts = 0
    
    def __init__(self, number, name, balance=0):
        """Initiate the instance attributes
        
        Args:
            number (str): The id account
            name (str): The name of the account owner
            balance (float): The balance on the account
        """
        self.number = number
        self.name = name
        self.balance = balance
        Account.total_accounts += 1
    
    def get_info_account(self):
        """Gets the information of a registered account"""
        print(f"\nAccount N. {self.number}:")
        print(f"\tName: {self.name}")
        print(f"\tBalance: {self.balance:.2f}")
    
    @classmethod
    def get_total_accounts(cls):
        """Gets the total of accounts registered"""
        return cls.total_accounts