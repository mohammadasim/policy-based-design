from hr import PayrollSystem
from productivity import ProductivitySystem, ManagerRole
from employees import EmployeeDatabase


def run():
    productivity_system = ProductivitySystem()
    payroll_system = PayrollSystem()
    employee_database = EmployeeDatabase()
    employees = employee_database.employees
    productivity_system.track(employees, 40)
    payroll_system.calculate_payroll(employees)


if __name__ == '__main__':
    run()
