from modules.company import Company

# Create a company instance
company = Company(budget=50000, employees=0, projects=0)  # Initialize with required parameters

# Show initial budget
company.company_budget()

# Let user add the new revenue
revenue = float(input("Add the amount of revenue: "))

# Update the company's budget
company.budget += revenue

# Show updated budget
company.company_budget()