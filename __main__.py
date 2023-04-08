import getssl
import swhois
import check
import analyze
import colored
import deep

#Получить сам домен
domain = input("Введите домен для проверки: ")
#Массив с данными о домене
domain_array = []

#Проверка
domain_array.append(swhois.swhois(domain)[0])
domain_array.append(getssl.getSsl(domain)[0])
domain_array.append(check.checkDomain(domain)[0])
domain_array.append(deep.getScamDomain(domain)[0])

#Показать сами резульаты проверки
print(colored.colored(swhois.swhois(domain)[1], "lightred_ex"))
print(colored.colored(getssl.getSsl(domain)[1], "lightmagenta_ex"))
print(colored.colored(check.checkDomain(domain)[1], "lightcyan_ex"))
print(colored.colored(deep.getScamDomain(domain)[1], "lightblue_ex"))

#Вернуть результат
print(colored.colored("Анализ сайта показал, что: "+analyze.analyze(domain_array), "lightgreen_ex"))