class biscuits():
    def __init__(self,name,year,size,is_tasty):
        self.name=name
        self.year=year
        self.size=size
        self.is_tasty=True
    def flour(self):
        print(f'{self.name} is made of flour')
class cookies(biscuits):
    pass
purebliss=biscuits('Purebliss','2016','40g',True)
beloxxi=biscuits('crackers','2005','25g',False)
print(beloxxi.name)
print(beloxxi.__dict__)
beloxxi.flour()
purebliss.flour()
cookie=cookies('shortbread','2002','200g',True)
print(cookie.__dict__)
cookie.flour()