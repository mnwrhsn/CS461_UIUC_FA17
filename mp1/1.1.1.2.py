with open('1.1.1.2_value.hex') as f:
    file_content = f.read().strip()
    f.close()

print 'hex:', file_content

dec_value = int(file_content, 16)
print 'decimal:', dec_value

bin_value = bin(dec_value)
print 'bin_value:', bin_value

with open('sol_1.1.1.2_binary.txt', 'w') as f:
    f.write(bin_value[2:])
    f.close()

with open('sol_1.1.1.2_decimal.txt', 'w') as f:
    f.write(str(dec_value))
    f.close()
