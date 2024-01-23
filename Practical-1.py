fh = open('Practical-1.txt', 'w')
fh.write('50 Fahrenheit = ')
fahrenheit = 50
celsius = (fahrenheit - 32) * 5 / 9
fh.write(str(celsius) + ' Celsius\n')

fh.write('50 Celsius = ')
celsius = 50
fahrenheit = (celsius * 9 / 5) + 32
fh.write(str(fahrenheit) + ' Fahrenheit\n')
fh.close()
