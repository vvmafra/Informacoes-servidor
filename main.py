import json
import os
import ipaddress

CONFIG_FILE_PATH = 'config/config.json'

# validação do IP
def validar_ip(endereco):
    try:   
        ip = ipaddress.ip_address(endereco)
        return True
    except ValueError as e:
        return False

# leitura do arquivo de configuração
def read_configuration():
    if not os.path.exists(CONFIG_FILE_PATH):
        print("O arquivo config.json não existe.")
        return

    with open(CONFIG_FILE_PATH, 'r') as file:
        try:
            data = json.load(file)
            if not data:
                print("O arquivo não contém informações.")
            else:
                print(json.dumps(data, indent=4))
        except json.JSONDecodeError:
            print("O arquivo não contém informações.")

# escrita do arquivo de configuração
def write_configuration():
    server_name = input("Informe o nome do servidor: ")
    
    while True:
        server_ip = input("Informe o IP do servidor: ")
        if validar_ip(server_ip):
            break
        else:
            print("Endereço IP inválido. Favor inserir IP válido.")
    
    server_password = input("Informe a senha do servidor: ")

    config_data = {
        "server_name": server_name,
        "server_ip": server_ip,
        "server_password": server_password
    }

    with open(CONFIG_FILE_PATH, 'w') as file:
        json.dump(config_data, file, indent=4)

    print("Informações salvas com sucesso!")
    print(json.dumps(config_data, indent=4))

# função principal
def main():
    if not os.path.exists('config'):
        os.makedirs('config')

    if not os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, 'w') as file:
            json.dump({}, file)

    print("Escolha uma opção:")
    print("1- Read configuration")
    print("2- Write configuration")
    choice = input("Digite sua escolha (1 ou 2): ")

    if choice == '1':
        read_configuration()
    elif choice == '2':
        write_configuration()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()