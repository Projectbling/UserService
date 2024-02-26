import random
import string

class GenerateUniqueCode:
    @staticmethod
    def generateRandomCode(size=8, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for k in range(size))

