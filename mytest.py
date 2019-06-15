class Phone:
    def __init__(self):
        self.numbertocall = ""
        self.color = ""
        self.carrier = []
        self.size = ""
        self.brand = ""
    def TakePicture(self):
        print("taking pictures with",self.brand,"phone")
    def Call(self):
        print("calling",self.numbertocall)
    def GetCarrier(self):
        return self.carrier

iphone = Phone()
iphone.carrier.append("att")
iphone.carrier.append("verizon")

print(iphone.carrier[0])
