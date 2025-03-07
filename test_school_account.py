import pytest

class SchoolAccount:
    def __init__(self, teacher_salary, staff_salary, student_fees, maintenance_cost=0, other_expenses=0):
        """
        Initializes the school account with salaries, student fees, and additional expenses.
        :param teacher_salary: Total salary for all teachers
        :param staff_salary: Total salary for non-teaching staff
        :param student_fees: Total fees collected from students
        :param maintenance_cost: School maintenance and infrastructure costs (default: 0)
        :param other_expenses: Additional operational costs (default: 0)
        """
        self.teacher_salary = teacher_salary
        self.staff_salary = staff_salary
        self.student_fees = student_fees
        self.maintenance_cost = maintenance_cost
        self.other_expenses = other_expenses
    
    def total_salary_expense(self):
        """Returns the total salary expenses for teachers and staff."""
        return self.teacher_salary + self.staff_salary
    
    def total_expenses(self):
        """Returns the total expenses including salary, maintenance, and other costs."""
        return self.total_salary_expense() + self.maintenance_cost + self.other_expenses
    
    def net_balance(self):
        """Calculates the net balance after all expenses are deducted from student fees."""
        return self.student_fees - self.total_expenses()

def test_total_salary_expense():
    account = SchoolAccount(teacher_salary=50000, staff_salary=20000, student_fees=80000)
    assert account.total_salary_expense() == 70000

def test_total_expenses():
    account = SchoolAccount(teacher_salary=50000, staff_salary=20000, student_fees=100000, maintenance_cost=15000, other_expenses=5000)
    assert account.total_expenses() == 90000

def test_net_balance_positive():
    account = SchoolAccount(teacher_salary=50000, staff_salary=20000, student_fees=100000, maintenance_cost=15000, other_expenses=5000)
    assert account.net_balance() == 10000

def test_net_balance_negative():
    account = SchoolAccount(teacher_salary=60000, staff_salary=30000, student_fees=80000, maintenance_cost=10000, other_expenses=5000)
    assert account.net_balance() == -25000

def test_no_additional_expenses():
    account = SchoolAccount(teacher_salary=40000, staff_salary=10000, student_fees=60000)
    assert account.net_balance() == 10000

if __name__ == '__main__':
    pytest.main()

"""
    ===================================================================== test session starts =====================================================================
platform linux -- Python 3.10.12, pytest-8.3.5, pluggy-1.5.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/shtlp_0170/Desktop/Python-101-
collected 5 items                                                                                                                                             

test_school_account.py::test_total_salary_expense PASSED                                                                                                [ 20%]
test_school_account.py::test_total_expenses PASSED                                                                                                      [ 40%]
test_school_account.py::test_net_balance_positive PASSED                                                                                                [ 60%]
test_school_account.py::test_net_balance_negative PASSED                                                                                                [ 80%]
test_school_account.py::test_no_additional_expenses PASSED                                                                                              [100%]

====================================================================== 5 passed in 0.01s ===================================================================
"""