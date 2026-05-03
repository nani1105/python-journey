class Patient:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hi, My name is {self.name} and my age is {self.age}")
    def __str__(self):
        return f"Patient: {self.name}, Age: {self.age}"
p1=Patient('Giri',43)
p1.greet()

print(p1)
p2 = Patient("Ravi", 25)
p2.greet()
print(p2)
class EmergencyPatient(Patient):
    def __init__(self,name,age,severity):
        super().__init__(name,age)
        self.severity=severity
    def alert(self):
        print(f"Emergency {self.name} needs emergency attention! his severity is {self.severity}")
e1=EmergencyPatient("mahesh",51,"High")
e1.greet()
e1.alert()
print(e1)