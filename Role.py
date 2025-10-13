class Role:

    #constructor with fields
    def __init__(self, title, salary):

        #child-specific fields
        self.title = title
        self.salary = salary
    
    #POLYMORPHISM
    def __str__(self):
        return f"{self.title} (${self.salary})"