import ssl
import socket
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

def getSsl(url):
    url = getDomain(url)
    try:
        #Принимает URL сайта в формате http:// или https://: или просто домен сайта

        # Извлечение имени хоста и номера порта из ссылки
        match = re.search(r"(?P<protocol>https?://)?(?P<hostname>[^/:]+)(:(?P<port>[0-9]+))?(/.*)?", url)
        if not match:
            return ["no", "Неверный формат URL."];
            exit()
        hostname = match.group("hostname")
        port = int(match.group("port") or 80 if match.group("protocol") == "http://" else 443)

        context = ssl.create_default_context()
        context.check_hostname = True
        context.verify_mode = ssl.CERT_REQUIRED

        try:
            with socket.create_connection((hostname, port)) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                    cert = ssl_sock.getpeercert()
        except socket.gaierror:
            return ["no", "Не удалось соединиться с указанным хостом."];
            exit()
        except ConnectionRefusedError:
            return ["no", "Сервер отказал в соединении."];
            exit()
        except ssl.CertificateError:
            return ["no", "Сертификат недействителен."];
            exit()

        if cert:
            return ["ok", f"Сертификат для сайта {hostname} действителен и был выдан {cert['issuer']}."];
        else:
            return ["ok", f"Сертификат для сайта {hostname} не найден."];
    except:
        return ["no", "Непредвиденная ошибка."];