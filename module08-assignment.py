# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services

services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "Technical Support": 95
}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}

customer1 = {
    "company_name": "Lesko Funeral Services",
    "contact_person": "John Rock",
    "email": "johnrock@gmail.com",
    "phone": "203-555-1248"
}

customer2 = {
    "company_name": "Lingos Powerwashing",
    "contact_person": "Jason Lingo",
    "email": "jasonlingo@gmail.com",
    "phone": "203-555-3492"
}

customer3 = {
    "company_name": "Yussuf's Keyboard Company",
    "contact_person": "Yussuf Solis",
    "email": "yussufskeyboardcompany@gmail.com",
    "phone": "203-555-6821"
}

customer4 = {
    "company_name": "Pick's Ski Rentals",
    "contact_person": "Kip Pick",
    "email": "pickskirentals@gmail.com",
    "phone": "203-555-7713"
}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}

customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information

for customer_id, customer_info in customers.items():
    print(customer_id)
    for key, value in customer_info.items():
        print(f"  {key}: {value}")
    print()

# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here

c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print(f"C002 Info: {c002_info}")
print(f"C003 Contact Person: {c003_contact}")
print(f"C999 Info: {c999_info}")

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here

customers["C001"]["phone"] = "203-555-8888"
customers["C002"]["industry"] = "Cleaning Services"

print(f"Updated C001: {customers['C001']}")
print(f"Updated C002: {customers['C002']}")

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here

project1 = {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000}
project2 = {"name": "Security Audit", "service": "Cybersecurity", "hours": 60, "budget": 13200}
project3 = {"name": "Sales Dashboard", "service": "Data Analysis", "hours": 80, "budget": 14000}
project4 = {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 90, "budget": 18000}
project5 = {"name": "Help Desk Setup", "service": "Technical Support", "hours": 50, "budget": 4750}
project6 = {"name": "Analytics Upgrade", "service": "Data Analysis", "hours": 70, "budget": 12250}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4, project5],
    "C004": [project6]
}

for customer_id, project_list in projects.items():
    print(customer_id)
    for project in project_list:
        print(f"  {project}")
    print()

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here

for customer_id, project_list in projects.items():
    for project in project_list:
        rate = services[project["service"]]
        cost = rate * project["hours"]
        print(f"{customer_id} - {project['name']}: ${cost:.2f}")

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here

customer_ids = list(customers.keys())
customer_companies = [customer["company_name"] for customer in customers.values()]
total_customers = len(customers)

print(f"Customer IDs: {customer_ids}")
print(f"Customer Companies: {customer_companies}")
print(f"Total Customers: {total_customers}")

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here

service_counts = {}

for project_list in projects.values():
    for project in project_list:
        service_name = project["service"]
        if service_name in service_counts:
            service_counts[service_name] += 1
        else:
            service_counts[service_name] = 1

for service, count in service_counts.items():
    print(f"{service}: {count}")

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here

all_projects = []
for project_list in projects.values():
    for project in project_list:
        all_projects.append(project)

total_hours = sum(project["hours"] for project in all_projects)
total_budget = sum(project["budget"] for project in all_projects)
avg_budget = total_budget / len(all_projects)
max_budget = max(all_projects, key=lambda project: project["budget"])
min_budget = min(all_projects, key=lambda project: project["budget"])

print(f"Total Hours: {total_hours}")
print(f"Total Budget: ${total_budget:.2f}")
print(f"Average Project Budget: ${avg_budget:.2f}")
print(f"Most Expensive Project: {max_budget['name']} (${max_budget['budget']:.2f})")
print(f"Least Expensive Project: {min_budget['name']} (${min_budget['budget']:.2f})")
