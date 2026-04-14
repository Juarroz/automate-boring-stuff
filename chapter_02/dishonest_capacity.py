print('Enter TB or GB for the advertised unit: ')
unit = input('>').lower()

#Calculate the amount that the advertised capacity lies:
if unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
advertised_capacity = float(input('>'))

# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated:
real_capacity = round(advertised_capacity * discrepancy, 2)

#print('The actual capacity is:' +  real_capacity + '' + unit)

print('The actual capacity is:', real_capacity, unit)
print(f'The actual capacity is: {real_capacity} {unit}')