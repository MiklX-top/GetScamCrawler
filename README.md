# ScamCrawler - проверка ссылок на предмет мошенничества.
Данный проект предназначен для проверки ссылок на предмет мошенничества благодаря собственным алгоритмам аналитики. Он будет использоваться для поиска и предупрежедения пользователей о подозрительности ссылки, возможно связанной с мошенничеством.

## Цель
Основной целью данного проекта является продвинутая аналитика ссылки на предмет мошенничества и выдача пользователю рекомендаций о её дальнейшем использовании, а так же информация о проверке и обоснование выдачи таких результатов системой.

## Функциональность
* Проект автоматически проверяет ссылку на предмет мошенничества и предоставляет результаты проверки в виде подсвеченных строк данных.
* Данный проект пишет рекомендации по дальнейшим действиям со стороны пользователя, что бы не стать жертвой интернет мошенников.
* Проект анализирует ссылки по самым жестким и оптимизированым алгоритмам.
* Проект анализирует схожие ссылки (зеркала) ресурсов, даже те, которые незанесены в базу.
* Проект состоит из модулей, функционал которых может быть использован в рамках многих других проектов.

##Принцип работы
1. Выполняется проверка владельца ресурса в системе **whois**, если у сайта нет владельца, то результат этого этапа проверки отрицательный.
2. Выполняется проверка SSL сертификата ресурса (именно самого SSL на не просто доступности сайта по https). Идет проверка центра, который регистрировал SSL, все самоподписанные сертификаты не считаются. В случае отсутствия SSL сертификата или же его неизвестном происхождении, результат этого этапа проверки будет отрицательный.
3. Выполняется проверка данного ресурса (а именно его домена) в личной базе ресурсов, в которую уже занесены проверенные домены которым можно доверять и домены которые принадлежат мошенникам. Во втором случае результат проверки данного этапа будет отрицательный и резульат выданный пользователю в итоге будет строго отрицательный.
4. Выполняется проверка на зеркала - похожие адреса этого ресурса в базе данных мошеннических ресурсов, даже при условии что вводимый ресурс туда не занесён. При нахождении сходств, результат проверки данного этапа будет отрицательным.
5. Выполняется аналитика полученных данных, результат проверки и рекомендации по дальнейшим действиям выводятся на экран пользователю.

## Зависимости
Данный проект написан полностью на Python 3.9 и при его создании были использованы библиотеки из общедоступных источников. Я использовал PIP.
Ниже привидены команды, утсанавливающие зависимости. Для удобства и наглядности, я разбил их на отдельные.

**Установка модуля re**
```python3
	py -m pip install re
```

**Установка модуля colorama**
```python3
	py -m pip install colorama
```

**Установка модуля ssl**
```python3
	py -m pip install ssl
```

**Установка модуля socket**
```python3
	py -m pip install socket
```

**Установка модуля whois (python-whois)**
```python3
	py -m pip install python-whois
```

**Установка всех зависимостей сразу**
```python3
	py -m pip install re colorama ssl socket python-whois
```

## Пример выводов результатов программы 
**Проверка будет выполнена на сайте аккредитованного регистратора доменов - reg.ru** <br><br>
**Входные данные**
```
	> reg.ru
```
**Данные на выходе**
```
	> Имя регистратора: REGRU-RU
	> Сертификат для сайта reg.ru действителен и был выдан ((('countryName', 'BE'),), (('organizationName', 'GlobalSign nv-sa'),), (('commonName', 'GlobalSign Extended Validation CA - SHA256 - G3'),)).
	> Домен reg.ru является доверенным.
	> Данный сайт, а так же его клоны и зеркала не внесены в реестр мошеннических сайтов.
	> Анализ сайта показал, что: Данный ресурс полностью безопасен.
```

**Проверка будет выполнена на ресурсе заведомо принадлежащему мошенникам - appcash.app, мы категорически не рекомендуем посещать данный ресурс!** <br><br>
**Входные данные**
```
	> appcash.app
```
**Данные на выходе**
```
	> Имя регистратора: GoDaddy.com, LLC
	> Сертификат для сайта appcash.app действителен и был выдан ((('countryName', 'US'),), (('organizationName', 'Google Trust Services LLC'),), (('commonName', 'GTS CA 1P5'),)).
	> Домен appcash.app является недоверенным.
	> Мы предполагаем что данный сайт - это клон или зеркало мошеннического ресурса. В нашей базе - 2 похожих ресурсов.
	> Анализ сайта показал, что: Посещать данный ресурс категорически не стоит. Это фишинг или обман.
```
