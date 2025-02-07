#Defining a class
class book :
    #attribute
    
 def __init__(self, color, genre, pages):
        self.color = color    
        self.genre = genre    
 
 # Creating objects with unique attributes
book1 = book("blue","Thriller")
book2 = book("red","Romance")

print(book1.color)  
print(book2.color) 

#Showing inheritance
class book:
    def __init__(self, pages):
        self.pages = pages 
        
class Thriller(book):
    def __init__(self, pages):
        super()__init__(pages)
        
thriller = Thriller(20)
print(thriller.pages)  # Output: 20


#Polymorphism challenge
class Hen:
    def speak(self):
        return "clucks"
class Cow:
    def speak(self):
        return "mows"  
# Polymorphism in action
for animal in [Hen(), Cow()]:
    print(animal.speak())             
    

        

         


    


        
