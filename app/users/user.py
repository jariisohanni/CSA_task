from enum import Enum

from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives.asymmetric import rsa  
from cryptography.hazmat.primitives import serialization  

class Role(Enum):
  Admin = 1
  Supervisor = 2
  Agent = 3

class User:

  def __init__(self, username, password, role):
    self.username = username
    self.password = password
    self.role = role
    self.private_key = None
    self.public_key = None

  def create_keys(self):
    self.private_key = rsa.generate_private_key(  
        public_exponent=65537,  
        key_size=2048,  
        backend=default_backend()  
    )
    self.public_key = self.private_key.public_key()

  def __str__(self):
    return "Username: %s\nPassword: %s\nPublic Key: %s" % (self.username, self.password, self.public_key.public_bytes(
        serialization.Encoding.OpenSSH,
        serialization.PublicFormat.OpenSSH))
