import whois

# Функция для выполнения запроса WHOIS для указанного домена
def swhois(domain):
    try:
        # Выполнение запроса WHOIS с помощью функции whois.whois()
        whois_domain = whois.whois(domain)
        # Проверка, удалось ли выполнить запрос
        if whois_domain.status:
            # Получение имени регистратора из объекта, возвращенного функцией whois.whois()
            owner_name = whois_domain.registrar
            # Возвращение статуса 'yes' и имени регистратора
            return ['ok', f"Имя регистратора: {owner_name}"]
        else:
            # Возвращение статуса 'no' и сообщения о том, что домен не был найден в WHOIS-сервисах
            return ['no', "Данный домен не был обнаружен в whois сервисах."]
    except Exception as e:
        # Если возникла ошибка при выполнении запроса, возвращается статус 'no' и сообщение об ошибке
        return ["no", "Непредвиденная ошибка."];