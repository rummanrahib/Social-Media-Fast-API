from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
  return password_context.hash(password)


def verify(plainPassword, hashedPassword):
  return password_context.verify(plainPassword, hashedPassword)