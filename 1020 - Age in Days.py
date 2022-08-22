age = int(input())
year=age//365
print("{} ano(s)".format(year))
month=(age%365)//30
print("{} mes(es)".format(month))
day=(age%365)%30
print("{} dia(s)".format(day))