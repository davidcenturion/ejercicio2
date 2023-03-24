#
#
import requests

r = requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')

# print(r.headers)
# print (r.status_code)
# print(r.encoding)
# print(r.content)
# print(r.text)



texto1 = r.text.split("\r\n")
texto2 = texto1[len(texto1)-2]
print(texto2[0:23])