class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, fais):
      self.name = name
      self.fais = fais
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Angkatan: ", self.fais)


#This would create first object of Employee class"
emp1 = Employee("Muh. fais", 2019)
#This would create second object of Employee class"
emp2 = Employee("aldo", 2020)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)