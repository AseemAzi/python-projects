class Recipe_Book:
    def __init__(self,name,no_ingredients,no_description):
        self.name=name
        self.no_ingredients=no_ingredients
        self.no_description=no_description
        
        
    def recipe(self): 
            f= open(f'{self.name}.txt','w')
            f.write(f'name:{self.name}\n')
            f.close()
    def ingredients_(self):
            f=open(f'{self.name}.txt','a')
            f.write('ingredients:')
            f.close()
            with open(f'{self.name}.txt','a') as f:
                for i in range(1,int(self.no_ingredients)+1):
                    f.write(f'\n{i}.{input(f"ingredient{i}")}')
    
    def description_(self):
        f=open(f'{self.name}.txt','a')
        f.write('\ndescription::')
        f.close()
        with open(f'{self.name}.txt','a') as f:
                for i in range(1,int(self.no_description)+1):
                    f.write(f'\n{i}.{input(f"description{i}:")}')
try:              
    rp1=Recipe_Book(name=(input("enter a name:")),no_ingredients=int(input("enter the no:of ingredients:")),no_description=int(input("enter no:of description:")))
    rp1.recipe()
    rp1.ingredients_()
    rp1.description_()
except ValueError:
    print("invalid input")
