#write a program that will create the following employees (Table 1) as well as the payroll deductions (Table 2):

import EmployeeClass as ec
import PayrollDeductionClass as pdc

#employee name, id, dep, job, salary
#jimmy smith, 58475, info sys, developer, $6800.00


emp_jim= ec.Employee('Jimmy Smith', '58475', 'Information Systems', 'Developer', '6800.00')
print('Employee Class')
print(emp_jim)
print()
print(emp_jim.get_name(), emp_jim.get_id(), emp_jim.get_department(), emp_jim.get_title(), emp_jim.get_salary())




pay_fc1= pdc.Payroll('Food Court        ', "8/14/2022 ", '22.50  ', '39119')
pay_gc= pdc.Payroll('Gift contribution ', "8/12/2022 ", '25.00  ', '58475')
pay_fc2=pdc.Payroll('Food Court        ', '8/17/2022 ', '15.25  ', '21547')
pay_vc1=pdc.Payroll('Vending Machine   ', '8/22/2022 ', '3.00   ', '58475')
pay_vc2=pdc.Payroll('Vending Machine   ', '8/5/2022  ', '2.75   ', '58475')


jim_pay1= pay_vc1.get_charge()
jim_pay2= pay_vc2.get_charge()
jim_pay3=pay_gc.get_charge()


jim_totalpay= float(jim_pay1) + float(jim_pay2) + float(jim_pay3)



jim_netpay= float(emp_jim.get_salary())-float(jim_totalpay)

netpay= '$'+ str(jim_netpay)

print()



print('Payroll Deductions')

print("Description      ", "Date     ", 'Charge', 'EmployeeID')
print(pay_fc1)
print(pay_gc)
print(pay_fc2)
print(pay_vc1)
print(pay_vc2)
print()
print('***Employee Pay***')
print("Name:", emp_jim.get_name())
print("ID Number:", emp_jim.get_id())
print("Department:", emp_jim.get_department())
print("Gross Pay:", '$'+emp_jim.get_salary())
print("Net Pay:", netpay)
