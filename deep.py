from urllib.parse import urlparse

def getScamDomain(search_text):
    #парсим URL
    search_text = search_text.split("//")[-1].split("/")[0].split(".")[0]

    filename = "scam_domains.list"
    try:
        with open(filename, 'r') as file:
            # счетчик совпадений
            copy_array = []
            count = 0
            for line in file:
                if search_text in line:
                    copy_array.append(line.strip())
                    count += 1
            # проверяем количество совпадений и выводим соответствующее сообщение
            if count == 0:
                return ["middle", "Данный сайт, а так же его клоны и зеркала не внесены в реестр мошеннических сайтов."]
            elif count == 1:
                return ["no", "Мы предполагаем что данный сайт - это клон или зеркало мошеннического ресурса.", copy_array]
            else:
                return ["no", f"Мы предполагаем что данный сайт - это клон или зеркало мошеннического ресурса. В нашей базе - {count} похожих ресурсов.", copy_array]
    except FileNotFoundError:
        return ["no", f"Файл {filename} не найден"]
    except Exception as e:
        return ["no", f"Ошибка: {e}"]