from kasutajad import Kasutajad
class Admin(Kasutajad):
    privileegid = []
    def naita_priv(self):
        print(self.privileegid)