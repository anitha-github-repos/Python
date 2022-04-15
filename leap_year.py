def is_year_leap(year):
    
    if(year %100 ==0):
        if (year %400 == 0):
            return True
        else:
            return False
    elif(year%4 == 0):
        return True
    else:
        return False
#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
    days = 0
    y = is_year_leap(year)
    
    if (month <=7 and month %2==0):
        if(month //2 == 1 and y):
            days = 29
        elif(month //2 ==1 and not y):
            days = 28
        else:
            days = 30
    elif (month <=7 and month %2!=0):
        days = 31
    elif (month >7 and month %2 ==0):
        days = 31
    else:
        days = 30
    return days
    
d = days_in_month(1900,2)
print(d)
#    days = 0
    
#     if(month % 10 ==0):
#         days = 30
#     elif(month % 2 ==0):
#         days = 29
#     else:
#         days = 31
#     return days

# d = days_in_month(1987,11)
# print(d)
#
# Write your new code here.
#

# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
# 	yr = test_years[i]
# 	mo = test_months[i]
# 	print(yr, mo, "->", end="")
# 	result = days_in_month(yr, mo)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")

print("practice")
