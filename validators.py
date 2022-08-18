# re module provides support for regular expressions
import re
# importing "keyword" for keyword operations
import keyword
import datetime


class Validators:

    def check_valid_identifier(self, identifier):
        """
            Um identificador deve começar com um alfabeto ou sublinhado,
            não pode começar com um dígito ou qualquer outro caractere especial, além disso,
            dígitos podem vir depois e deve conter no mínimo 3 e no máximo 10 caracteres

            :param identifier: String
            :return: True ou False
            """
        # regex = '^[A-Za-z_][A-Za-z0-9_]*'
        print(type(identifier))
        # if type(identifier) in [int, float]:
        #		raise TypeError("Tipo não é string")

        regex = '^[A-Za-z_][A-Za-z0-9_]{2,9}$'
        # pass the regular expression
        # and the string in search() method
        if re.search(regex, identifier):
            print("Identificador Válido")
            return True
        else:
            print("Identificador Inválido")
            return False

    def check_email(self, email):
        """
        Um email é uma string (um subconjunto de caracteres ASCII) separada em
        duas partes pelo símbolo @, um “personal_info” e um domínio, que é personal_info@domain.
        """
        # Make a regular expression
        # for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # pass the regular expression
        # and the string into the fullmatch() method

        if (re.fullmatch(regex, email)):
            print("Email Válido")

        else:
            print("Email Inválido")

    def check_keywords_python(self, keys):
        """
        Python em sua linguagem define um módulo embutido “palavra-chave” que
        lida com certas operações relacionadas a palavras-chave. Uma função “iskeyword()”
        verifica se uma string é uma palavra-chave ou não.
        Retorna true se uma string for uma palavra-chave, senão retorna false.
        """
        # initializing strings for testing while putting them in an array
        # keys = ["for", "while", "tanisha", "break", "sky",
        #		"elif", "assert", "pulkit", "lambda", "else", "sakshar"]

        for i in range(len(keys)):
            # checking which are keywords
            if keyword.iskeyword(keys[i]):
                print(keys[i] + " é uma keyword python")
            else:
                print(keys[i] + " não é uma keyword python")

    def check_password(self, password):
        """
        Neste programa, tomaremos uma senha como uma combinação de caracteres alfanuméricos junto com caracteres
        especiais e verificaremos se a senha é válida ou não com a ajuda de algumas condições.

        Condições primárias para validação de senha:
        1. Mínimo de 8 caracteres.
        2. Os alfabetos devem estar entre [a-z]
        3. Pelo menos um alfabeto deve ser de maiúsculas [A-Z]
        4. Pelo menos 1 número ou dígito entre [0-9].
        5. Pelo menos 1 caractere de [ _ ou @ ou $ ].
        :param password: String
        :return: 0 Válido ou -1 Inválido
        """

        flag = 0
        while True:
            if (len(password) < 8):
                flag = -1
                break
            elif not re.search("[a-z]", password):
                flag = -1
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                break
            elif not re.search("[0-9]", password):
                flag = -1
                break
            elif not re.search("[_@$]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0
                print("Password Válido")
                break

        if flag == -1:
            print("Password Inválido")

        return flag

    def check_age_for_work(self, age):
        """
        Exemplo: sistema recursos humanos – empregar pessoas com base na idade
            0-16 - Não empregar.
            17-18 - Pode ser empregado Parcial.
            19-55 - Pode ser empregado Integral.
            56-99 - Não empregar.

        :param age: int
        :return: Não Empregar, Empregado Parcial, Empregado Integral
        """
        status = {
            0: "Não Empregar",
            1: "Empregado Parcial",
            2: "Empregado Integral",
            3: "Empregado Como Múmia"
        }
        if 0 < age <= 16:
            result = status.get(0)
            print(result)
        elif 17 <= age <= 18:
            result = status.get(1)
            print(result)
        elif 19 <= age <= 55:
            result = status.get(2)
            print(result)
        elif age > 100:
            result = status.get(3)
            print(result)
        else:
            result = status.get(0)
            print(result)

            return result

    def years_in_election(self, birth_date, election_date=None):
        if election_date is None:
            election_date = datetime.now()
        else:
            election_date = datetime.date(day=26, month=9, year=2022)

        # birth_date = datetime.date(day=25, month=9, year=1990)

        diff = election_date - birth_date
        # 0.25 = 1/4 (anos bissexto)
        years = diff.days // 365.25
        print(years)
        return years

    def check_brazilian_voter(self, years):
        status = {
            0: "Facultativo",
            1: "Obrigatório",
            2: "Não Vota"
        }
        if 16 <= years <= 17 or 70 < years:
            # if years >= 16 and years <= 17
            print(status.get(0))
            result = status.get(0)
        elif 18 <= years < 70:
            print("Obrigatório")
            result = status.get(1)
        else:
            print("Não vota")
            result = status.get(2)

        return result

    def idade_caboco(self, dt, dt2, analfa):
        return None
