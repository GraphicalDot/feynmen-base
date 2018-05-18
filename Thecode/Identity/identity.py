
from faker import Faker
fake = Faker()


class GenerateKeys(object):

    def generate_keys(self):
        """
        Generate public privatekeys
        """



class StoreDetails(object):

    def storedetails():
        """
        Store the Identity encrypted with Public key 
        and hashes signed by digital signature and store them on blockchainDB.
        """
        pass







class GetUserDetails:

    def __init__(self, identity_image, self_image):
        """
        to check if there is a match between the image of the person and get
        the relevant details from the adhaar 

        """
        self.identity_image = identity_image
        self.self_image = self
        
        
        
        
    def adhaar(self):
        """
        If the identity_image is of kind adhaar
        
        TODO: Use any thirdparty of write your own functions for convolution neural nets to get the 
        similirity between the two
        True if there is a match in the identities 
        """


        return (fake.credit_card_number(), fake.address(), fake.name(), True)




