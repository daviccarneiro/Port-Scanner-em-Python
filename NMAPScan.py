import nmap

scanner = nmap.PortScanner()

ip = input("Digite o ip a ser varrido: ")
print("O ip digitado foi",ip)
type(ip)

menu = int(input("""\n Escolha o tipo de varredura a ser realizada: 
                        1 -> Varredura SYN
                        2 -> Varredura UDP
                        3 -> Varredura Intensa
                        Digite a opção desejada: """))

print("Versão do NMAP: ", scanner.nmap_version())

def scanPadrao():
    print(scanner.scaninfo())
    print("Status do ip: ",scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")

if menu == 1:
    scanner.scan(ip,'1-1024','-v -sS')
    scanPadrao()
    print("Portas abertas: ",scanner[ip,'tcp'].keys())

elif menu == 2:
    scanner.scan(ip,'1-1024','-v -sU')
    scanPadrao()
    print("Portas abertas: ",scanner[ip,'udp'].keys())

elif menu == 3:
    scanner.scan(ip, '1-1024','-v -sC')
    scanPadrao()
    print("Portas abertas: ",scanner[ip,'tcp'].keys())

else:
    print("Opção não identificada.")


