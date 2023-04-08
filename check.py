import re

def getDomain(url):
    try:
        # Регулярное выражение для поиска протокола
        protocol_regex = r"(https?://)"
        # Удаление протокола из URL
        domain = re.sub(protocol_regex, "", url)
        # Регулярное выражение для поиска домена
        domain_regex = r"([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}"
        # Извлечение домена из URL
        domain = re.search(domain_regex, domain).group()
        return domain
    except:
        return ["no", "Непредвиденная ошибка."]

def getListDomains(filename):
    # Открытие файла для чтения и чтение всех строк в переменную lines
    with open(filename, "r") as file:
        lines = file.readlines()

    # Создание пустого списка для хранения результатов
    result = []

    # Итерация по всем строкам файла
    for line in lines:
        # Очистка строки от символов переноса строки и добавление её в список результатов
        result.append(line.strip())

    # Возврат списка результатов
    return result

def checkDomain(domain):
    try:
        scam_domains = getListDomains("scam_domains.list")
        free_domains = getListDomains("free_domains.list")
        
        # Удаляем протокол из домена
        domain = getDomain(domain)

        if domain.lower() in free_domains:
            return ["ok", f"Домен {domain} является доверенным."]
        elif domain.lower() in scam_domains:
            return ["no", f"Домен {domain} является недоверенным."]
        else:
            return ["middle", f"Домена {domain} нет в нашем списке доверенных и недоверенных."]
    except:
        return ["no", "Непредвиденная ошибка."]