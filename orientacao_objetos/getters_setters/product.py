class Product:
    """Model of a product class
    
    Methods:
        __init__: initiate the attribute class
        discount: performs a discount through a percentage
    """
    
    def __init__(self, name, price) -> None:
        """initiate the attribute class

        Args:
            name (string): product's name
            price (float): price of the product
        """
        self._name = name
        self._price = price
    
    def discount(self, percent):
        """performs a discount through a percentage

        Args:
            percent (int): percentage of discount
        """
        self._price = (100 - percent)/100 * self._price
    
    # Getters
    
    @property
    def name(self):
        """Return the product's name

        Returns:
            str: name
        """
        return self._name
    
    @property
    def price(self):
        """Return price of the product

        Returns:
            float: price
        """
        return float(self._price)
    
    # Setters
    
    @name.setter
    def name(self, value):
        """Rename the product

        Args:
            value (str): products new name
        """
        self._name = value
    
    @price.setter
    def price(self, value):
        """reprice the product

        Args:
            value (float): products new price
        """
        if isinstance(value, str):
            value = float(value.replace('R$', ''))
        self._price = value