class Phone:
    def call (self):
        print("You Can call")
    def message (self):
        print("You Can message")

class Samsung(Phone):
    def photo(self):
        print("You can take photo")
            
p=Phone()
p.message()
p.call()

s=Samsung()
s.message()
s.call()
s.photo()