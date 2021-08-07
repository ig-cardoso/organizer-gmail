from getpass import getpass


def main() -> int:
    print('É necessário informar suas credenciais para se comunicar com a API')
    email = input('\tEmail: ')
    password = getpass('\tSenha: ')

    print(password)

    return 0

if __name__ == '__main__':
    main()