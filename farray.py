def wrap_file_contents(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    result = []
    for line in lines:
        # Добавление очищенной строки в список результатов
        result.append(line.strip())

    return result

result = wrap_file_contents("filename.txt")
print(result)