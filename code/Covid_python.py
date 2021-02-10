from covid import Covid

covid=Covid()

s="PAKISTAN"
print(covid.get_status_by_country_name(s))

print("total case: ",covid.get_total_confirmed_cases())
print("total death: ",covid.get_total_deaths())
print("total recovered: ",covid.get_total_recovered())

