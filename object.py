class Araba():
    def __init__(self,model,renk,atgucu):
        self.model=model
        self.renk=renk
        self.atgucu=atgucu
        print("init fonksonu calisdi")
araba1=Araba("BMW","qara",250)
print(araba1.model)
