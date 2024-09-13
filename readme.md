# Leitura e Gravação de Informações do Servidor

Este projeto é um script Python para leitura e escrita de um arquivo de configuração JSON que contém informações sobre um servidor, como nome, IP e senha.

## Pré-requisitos

- Python 3.x instalado
- Permissões de leitura e escrita no diretório onde o script será executado

## Estrutura do Projeto

config/
config.json
main.py
README.md

## Passo a Passo para Execução

1. **Clone o repositório ou baixe os arquivos necessários.**

2. **Navegue até o diretório do projeto.**

   ```sh
   cd caminho/para/o/diretorio/do/projeto
   ```

3. **Execute o script `main.py`.**

   ```sh
   python main.py
   ```

## Utilização

Ao executar o script, você verá o seguinte menu:

```
Escolha uma opção:
1- Read configuration
2- Write configuration
Digite sua escolha (1 ou 2):
```

### Opção 1: Leitura da Configuração

- Selecione `1` para ler a configuração existente no arquivo `config/config.json`.
- O script exibirá o conteúdo do arquivo JSON formatado.

### Opção 2: Escrita da Configuração

- Selecione `2` para escrever uma nova configuração no arquivo `config/config.json`.
- O script solicitará as seguintes informações:
  - Nome do servidor
  - IP do servidor (será validado)
  - Senha do servidor
- Após inserir as informações, o script salvará os dados no arquivo JSON e exibirá a nova configuração.

## Mensagens de Erro

- **Arquivo não existe:** Se o arquivo `config/config.json` não existir, uma mensagem será exibida e o script criará um arquivo vazio.
- **IP inválido:** Se o IP inserido não for válido, uma mensagem de erro será exibida e o script solicitará um novo IP.

## Exemplo de Execução

```sh
python main.py
Escolha uma opção:
1- Read configuration
2- Write configuration
Digite sua escolha (1 ou 2): 2
Informe o nome do servidor: MeuServidor
Informe o IP do servidor: 192.168.1.1
Informe a senha do servidor: minhaSenhaSegura
Informações salvas com sucesso!
{
    "server_name": "MeuServidor",
    "server_ip": "192.168.1.1",
    "server_password": "minhaSenhaSegura"
}
```
