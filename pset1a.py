# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:30:46 2024

@author: divya
"""

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the portion of your salary to be saved, in decimal:"))
total_cost = float(input("Enter the total cost of your dream home:"))

portion_down_payment = .25*total_cost
print("Total Down payment = ", portion_down_payment)


current_savings = 0
num_months = 0

r = 0.04

while current_savings <= portion_down_payment:
    num_months += 1
    current_savings += (current_savings * r / 12) + portion_saved*(annual_salary/12)
print("Num of months = ", num_months)

