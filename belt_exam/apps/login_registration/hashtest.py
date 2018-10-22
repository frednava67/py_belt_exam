import bcrypt

badpassword1 = "password"
badpassword2 = "abc123"

hash1 = bcrypt.hashpw(badpassword1.encode(), bcrypt.gensalt())
hash2 = bcrypt.hashpw(badpassword2.encode(), bcrypt.gensalt())

#hash2 = bcrypt.generate_password_hash(badpassword2)
print(hash1)
print(hash2)

print(bcrypt.checkpw(badpassword1.encode(), hash1))
print(bcrypt.checkpw(badpassword1.encode(), hash2))
#print(hash2)
#hash1 = bcrypt.generate_password_hash(badpassword1)
#hash2 = bcrypt.generate_password_hash(badpassword2)
#print(hash1)
#print(hash2)
#hash1 = bcrypt.generate_password_hash(badpassword1)
#hash2 = bcrypt.generate_password_hash(badpassword2)
#print(hash1)
#print(hash2)

#print(bcrypt.check_password_hash(hash1, badpassword1))
#print(bcrypt.check_password_hash(hash2, badpassword2))

#print(bcrypt.check_password_hash(hash2, badpassword1))
#print(bcrypt.check_password_hash(hash1, badpassword2))