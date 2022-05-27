var1 = input()
var2 = input()

print(f"Before:\na = {var1}\nb = {var2}")
var1, var2 = var2, var1
print(f"After:\na = {var1}\nb = {var2}")