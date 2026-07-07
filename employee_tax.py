'''
package=float(input("Enter package:"))
if package<300000:
    print("No tax")
elif package>=300000 and package<500000:
    tax=package*0.05
    print("Tax rate:5%")
elif package>=500000 and package<700000:
    tax=package*0.10
    print("Tax rate:10%")
elif package>=700000 and package<1000000:
    tax=package*0.15
    print("Tax rate:15%")
elif package>1000000 and package<1500000:
    tax=package*0.20
    print("Tax rate:20%")
elif package>=1500000 and package<2000000:
    tax=package*0.25
    print("Tax rate:25%")
else:
    tax=package*0.30
    print("Tax rate:30%")
print("Annaul package:",package)
print("Tax amount:",tax)
print("Net salary after tax:",package-tax)
'''
