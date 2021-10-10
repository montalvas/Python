'''
public -> full access of the attributes and methods
_protected -> only the class and subclass can access
__private -> only the class
'''

class DataBase:
    """Model of a database
    
    Methods:
        __init__: Initiate the attributes
        insert_client: Register the client in database
        clients_list: Show the list of clients
        delete_client: Delete a customer via id
    """
    
    def __init__(self):
        """Initiate the attributes"""
        self._data = {}
    
    @property
    def data(self):
        return self._data

    def insert_client(self, id, name):
        """Register the client in database

        Args:
            id (int): client's id
            name (str): client's name
        """
        if 'clients' not in self.data:
            self.data['clients'] = {id: name}
        else:
            self.data['clients'].update({id: name})
    
    def clients_list(self):
        """Show the list of clients"""
        if self.data['clients']:
            print("\nList of clients:")
            for id, name in bd.data['clients'].items():
                print(f"\tID: {id} | Name: {name}")
        else:
            print(f"\nNo registered customer.")
    
    def delete_client(self, id):
        """Delete a customer via id"""
        if self.data['clients']:
            if 1 <= id <= len(self.data['clients']):
                del self.data['clients'][id]
            else:
                print("Invalid id.")
                
        else:
            print(f"\nNo registered customer to delete.")      


bd = DataBase()
bd.insert_client(1, 'Lucas')
bd.insert_client(2, 'Miguel')
bd.insert_client(3, 'Adriana')
bd.clients_list()

bd.delete_client(3)
bd.clients_list()
