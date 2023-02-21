import urllib.request

mi_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

with open("hola.txt", "r") as file:
    i = 0
    lines = file.readlines()
    for line in lines:
        if line.find("\tA\t") != -1:
            lines[i] = f"@   IN  A    {mi_ip}\n"
        i += 1

with open('hola.txt', 'w') as file:
    file.writelines(lines) 