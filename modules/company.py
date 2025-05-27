class Company:
     """A simple attempt to repsesnt a company"""
     def __init__(self, budget, employees, projects):
          self.budget = budget
          self.employees = employees
          self.prjects = projects

     def company_budget(self):
          """Get budget info"""
          print(f"Current compant budget: {self.budget}")
     
     def company_employees(self):
          """Get budget info"""
          print(f"Current number of employees: {self.employees}")
     def company_projects(self, new_project):
          """verifying the number of projects , or updating it"""
          self.prjects += new_project
          print(f"The number of completed projects: {new_project}")