import tornado.options
import tornado.web
from SettingsModule.settings import user_collection_name, jwt_secret
from SettingsModule.cors import cors
import jwt
from LoggingModule.logging import logger
from generate_keys import GenerateKeys
from faker import Faker
fake = Faker()

class UserRegistration(tornado.web.RequestHandler):

	def initialize(self):
			self.db = self.settings["db"]
			self.collection = self.db[user_collection_name]
			print (self.collection)

	@cors
	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def  get(self):
		self.set_status(401)
		self.finish()
		return 



			
	@cors
	@tornado.gen.coroutine
	def  post(self):
		"""
		Used to create a new user or update and existing one
		Request Param:
			user_type: admin, accessor, evaluator, superadmin
			username: 
			password: 
			newpassword:
		"""

		#print (self.request.body)

		#post_arguments = json.loads(self.request.body.decode("utf-8"))
		#print (post_arguments)
		self_image = self.get_body_argument("self_image", default=None, strip=False)

		adhaar_image = self.get_body_argument("adhaar_image", default=None, strip=False)



		##TODO: 
		"""

		Also post the ipfs config file
		Get image out of the adhaar card
		Get adhaar card number from the adhaar card
		Get other detail like address and phone number from the adhaar card
		Match self_image with adhaar card image
		
		

		Generate new key value pair and save that key in the database 
		For the time being, private keys will be stored as such for the users 
		Corresponding public keys will be used to decrypt public keys required for IPFs, BIGchaindb and Sawtooth etc keys 
		"""


		_class = GenerateKeys()
		(private_key, public_key) = __class.generate_keys()














		