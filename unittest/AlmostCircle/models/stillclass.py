class family:
    def __init__(self, firstborn, secondborn, lastborn):
        self.firstborn = firstborn
        self.secondborn = secondborn
        self.lastborn = lastborn
        
    def get_full_name(self):
        return f"{self.firstborn} {self.lastborn}"
        
    def names(self):
        return f"Hi. I'm {self.firstborn}  and I'm {self.secondborn} and am the {self.lastborn} of the family "

    @classmethod
    def create_fa(cls):
        return family('Aisah', 'AlAreef', 'AlAmeen')
create  = family.create_fa()
print(create.names()) 