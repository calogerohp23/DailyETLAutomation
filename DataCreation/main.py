import pandas as pd
import random

# Predefined lists of first and last names
FIRST_NAMES = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez"]

# Function to generate random email
def generate_email(first_name, last_name):
    return f"{first_name.lower()}.{last_name.lower()}@company.com"

# Generate Employees Data Set
def create_employees_data(num_employees=100):
    employees = []
    for emp_id in range(1, num_employees + 1):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        email = generate_email(first_name, last_name)
        job_level = round(random.uniform(1.1, 9.0), 1)
        supervisor_id = random.randint(1, num_employees) if emp_id > 1 else None
        unit_id = random.randint(1, 10)
        department_id = random.randint(1, 5)
        employees.append({
            "EmployeeID": emp_id,
            "FirstName": first_name,
            "LastName": last_name,
            "EmailAddress": email,
            "JobLevel": job_level,
            "SupervisorID": supervisor_id,
            "UnitID": unit_id,
            "DepartmentID": department_id
        })
    return pd.DataFrame(employees)

# Generate Supervisor Table
def create_supervisor_table(employees_df):
    supervisors = employees_df[["EmployeeID", "FirstName", "LastName"]].rename(
        columns={"EmployeeID": "SupervisorID", "FirstName": "SupervisorFirstName", "LastName": "SupervisorLastName"}
    )
    return supervisors

# Generate Unit Table
def create_unit_table(num_units=10):
    units = [{"UnitID": unit_id, "UnitName": f"Unit{unit_id}"} for unit_id in range(1, num_units + 1)]
    return pd.DataFrame(units)

# Generate Department Table
def create_department_table(num_departments=5):
    departments = [{"DepartmentID": dept_id, "DepartmentName": f"Department{dept_id}"} for dept_id in range(1, num_departments + 1)]
    return pd.DataFrame(departments)

# Main execution
if __name__ == "__main__":
    # Create Employees Data Set
    employees_df = create_employees_data()

    # Create Supervisor Table
    supervisor_table = create_supervisor_table(employees_df)

    # Create Unit Table
    unit_table = create_unit_table()

    # Create Department Table
    department_table = create_department_table()

    # Save to CSV files
    employees_df.to_csv("Employees.csv", index=False)
    supervisor_table.to_csv("Supervisors.csv", index=False)
    unit_table.to_csv("Units.csv", index=False)
    department_table.to_csv("Departments.csv", index=False)

    print("Data creation completed. Files saved as CSV.")