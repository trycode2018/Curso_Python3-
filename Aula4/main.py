a = 'AAAA'
b = 'BBBB'
c = 1.1

string = 'a = {}, b = {}, c = {}'.format(a, b, c)
print(string)

string_param = 'b = {p2}, a = {p1}, c = {p3}'
print(string_param.format(p1=a, p2=b, p3=c))


