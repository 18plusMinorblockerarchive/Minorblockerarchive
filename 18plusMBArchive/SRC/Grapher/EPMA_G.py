from Domain.Instagram import Instagram
from Domain.Twitter import Twitter
from Domain.Facebook import Facebook

class EPMA_G:
    def __init__(self):
        self.Instagram = Instagram.Instagram_Grapher()
        self.Twitter = Twitter.Twitter_Grapher()
        self.Facebook = Facebook.Facebook_Grapher()
    
    def Get_Grapher_Attributes(self):
        self.Instagram.Ploter()
        self.Twitter.Ploter()
        self.Facebook.Ploter()