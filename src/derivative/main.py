import re


class Derivative:

    def __init__(self, f):
        self.f = f
        self.terms = self.split()

    @staticmethod
    def replace_space(s: str | list):

        if isinstance(s, str):
            return s.replace(' ', '')

        return list(map(lambda x: x.replace(' ', ''), s))

    def split(self):
        # Split the function into a list of terms by: '+', '-', '*', '/'
        terms = re.split(r'([+\-/*])', self.f)

        # Remove spaces from the list
        terms = self.replace_space(terms)

        # Merge all the terms that are part of the same term
        temp = []
        res = []
        flag = False

        for i in terms:

            if i.startswith('('):
                temp.append(i)
                flag = True

            elif flag:
                temp.append(i)
                if i.endswith(')'):
                    flag = False

                    temp = Derivative(' '.join(temp)[1:-1]).split()
                    res.append(temp)
                    temp = []
            else:
                res.append(i)

        return res

    def power_rule(self):
        # Apply the root rule to the terms
        res = []

        for i in self.terms:

            if isinstance(i, list):
                res.append(Derivative(' '.join(i)).power_rule())

            elif "^" in i:
                argument, power = i.split('^')
                res.append(f'{power}{argument}^{int(power) - 1}')

            else:
                res.append(i)

        return res

    def constant_rule(self):
        res = []

        for i in self.terms:

            if isinstance(i, list):
                res.append(Derivative(' '.join(i)).constant_rule())

            elif i.isnumeric():
                res.append('0')

            elif i.isalpha():
                res.append('1')

            elif i.isalnum():
                constant = re.findall(r'(\d+)', i)[0]
                res.append(constant)

            else:
                res.append(i)

        return res


string = '(x^2 + 20x) + 1 + x'
d = Derivative(string)
print(d.power_rule())
print(d.constant_rule())
