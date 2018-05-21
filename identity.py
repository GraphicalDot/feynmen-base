
from faker import Faker
fake = Faker()
from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
import base64
import ipfsapi
import json
##https://media.readthedocs.org/pdf/python-ipfs-api/latest/python-ipfs-api.pdf


class GenerateKeys(object):


    def __init__(self, generate=False):
        self.private_key_str = None 
        self.public_key_str = None
        self.private_key = None 
        self.public_key = None
        self.private_filename = "privatekey.pem"
        self.public_filename = "publickey.pem"
        if not generate:
            ##TODO: pass on the path of private and public keys
            try:
                self.private_key = self.load_private_key(self.private_filename)
                self.public_key = self.load_public_key(self.public_filename)
            except Exception as e:
                print(e)
                raise StandardError("Please generate new public private keys for Encryption")
        else:
            self.generate_keys()


    def generate_keys(self):
        """
        Generate public privatekeys
        https://sawtooth.hyperledger.org/docs/core/releases/1.0/_autogen/sdk_submit_tutorial_python.html
        context = create_context('secp256k1')
        private_key = context.new_random_private_key()
        signer = CryptoFactory(context).new_signer(private_key)
        self.private_key_hex =  private_key.as_hex()
        self.signer_public_key=signer.get_public_key().as_hex(),
        return (private_key_hex, signer_public_key)
        """
        # generate private/public key pair
        self.private_key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, key_size=2048)

        # get public key in OpenSSH format
        self.public_key = self.private_key.public_key()
        
        
        pem_public = self.public_key.public_bytes(serialization.Encoding.OpenSSH, serialization.PublicFormat.OpenSSH)

        # get private key in PEM container format
		pem = self.private_key.private_bytes(encoding=serialization.Encoding.PEM, 
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption())

		with open(self.private_filename, 'wb') as pem_out:
			pem_out.write(pem)

		with open(self.public_filename, 'wb') as pem_out:
			pem_out.write(pem_public)




	    # decode to printable strings
        self.private_key_str = pem.decode('utf-8')
        self.public_key_str = pem_public.decode('utf-8')

        #print(self.private_key_str)
        #print(self.public_key_str)
        return 



    def load_private_key(filename):
        with open(self.private_filename, 'rb') as pem_in:
            pemlines = pem_in.read()
        private_key = load_pem_private_key(pemlines, None, default_backend())
        return private_key

    def load_public_key(self):
        ##load public and private keys from BIGchainB
        with open(self.public_filename, 'rb') as pem_in:
            pemlines = pem_in.read()
        public_key = load_pem_public_key(pemlines, None, default_backend())
        return public_key

    def encrypt_object(self, message):
    	#https://medium.com/@raul_11817/rsa-with-cryptography-python-library-462b26ce4120
        message = message.encode('ascii')
        ciphertext = self.public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None
                )
            )

        ciphertext  = str(base64.b64encode(ciphertext), encoding='utf-8')

        data_to_sign = bytes(message, encoding='utf8') if not isinstance(message, bytes) else message

        signer = self.private_key.signer(
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
        hashes.SHA256()
            )

        signer.update(data_to_sign)
        signature = str(
                base64.b64encode(signer.finalize()),
            encoding='utf8'
        )


        return (ciphertext, signature)

    def test_keys(self):
        """
        Test if the encryption and decryption process
        """


    def decrypt_object(self, ciphertext):
        ciphertext_decoded = base64.b64decode(ciphertext) if not isinstance(ciphertext, bytes) else ciphertext

        plain_text = raul_private_key.decrypt(ciphertext_decoded,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None))
        return plain_text


    def verify_signature(self, plain_text, signature):
        try:
            plain_text_bytes = bytes(
            plain_text, 
            encoding='utf8') if not isinstance(plain_text, bytes) else plain_text
            signature = base64.b64decode(signature) if not isinstance(signature, bytes) else signature


            verifier = self.public_key.verifier(
                signature,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256())
            verifier.update(plain_text_bytes)
            verifier.verify()
            return true

        except InvalidSignature:
            return False



class StoreDetails(object):
    ##https://github.com/ipfs/py-ipfs-api
    
    
    @staticmethod
    def storedetails(data):
        """
        Store the Identity encrypted with Public key 
        and hashes signed by digital signature and store them on blockchainDB.
        TODO: Encrypt this data, with the public key of this user, May be bigchaindb public key of this user
        TODO: You somehow force this file to be stored by atleast three other peers. If one of the peer goes down
            It should stores all the files to some other peers.
        """


        api = ipfsapi.connect('127.0.0.1', 5001)
        res = api.add_json({"cipher_text": data[0], "signature": data[1]})
        ##res{'Hash': 'QmWxS5aNTFEc9XbMX1ASvLET1zrqEaTssqt33rVZQCQb22', 'Name': 'test.txt'}
        print (res)
	return res



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



if __name__ == "__main__":
    _instance = GenerateKeys()
    _instance.generate_keys()
    (ciphertext, signature) = _instance.encrypt_object("hey now, Dude how are you")
    print (ciphertext, signature)
    ipfs_object_hash = StoreDetails.storedetails((ciphertext, signature))

