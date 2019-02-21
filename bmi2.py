class Bmi:
    
    ask1 = input("身長を入力してください\n")
    ask2 = input("体重を入力してください\n")

    bmi = float(ask2) / float(ask1) / float(ask1)

    def __init__(self,hei,wei):
        self.hei = hei
        hei = float(ask1) / 100
        self.wei = wei
        wei = float(ask2)
 

    def put(self):
        print(self.bmi)

out = bmi(hei,wei)
print(out.hei)
print(out.wei)
out.put()

