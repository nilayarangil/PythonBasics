import phone

class AdvPhone(phone.Phone):
    def __init__(self):
        phone.Phone.__init__(self)
        self.standshape = ""
    def TakeVideo(self):
        print("taking videos with",self.brand)
'''
iphonexsmax = AdvPhone()
iphonexsmax.standshape="triangle"
iphonexsmax.brand = "apple"
iphonexsmax.TakeVideo()
'''
