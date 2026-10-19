import csv
from xml.dom import minidom
books = []

with open("books-en(2).csv", "r", encoding="latin1", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")

    for row in reader:
        books.append(row)
        
long_title_count = 0

for book in books:
    if len(book["Book-Title"]) > 30:
        long_title_count = long_title_count + 1

print("Количество названий длиннее 30 символов:", long_title_count)

author_name = "stephen king"  # Пример автора, у которого есть книги дешевле 200 рублей.
print("\nКниги Стивена Кинга стоимостью до 200 рублей:")
found_book = False

for book in books:
    author = book["Book-Author"].lower()
    price = float(book["Price"].replace(",", "."))

    if author_name in author and price <= 200:
        print(book["Book-Author"] + ". " + book["Book-Title"] + " - " + book["Year-Of-Publication"])
        print("Цена:", price)
        found_book = True

if found_book == False:
    print("Подходящие книги не найдены.")

output_file = open("bibliography.txt", "w", encoding="utf-8")
number = 1

for book in books:
    author = book["Book-Author"].strip()
    title = book["Book-Title"].strip()
    year = book["Year-Of-Publication"].strip()

    if author != "" and title != "" and year.isdigit():
        reference = str(number) + ". " + author + ". " + title + " - " + year
        output_file.write(reference + "\n")
        number = number + 1

    if number > 20:
        break

output_file.close()
print("\nБиблиографические ссылки сохранены в файле bibliography.txt")

xml_document = minidom.parse("currency.xml")
currencies = xml_document.getElementsByTagName("Valute")
currency_dictionary = {}

for currency in currencies:
    num_code = currency.getElementsByTagName("NumCode")[0].firstChild.data
    char_code = currency.getElementsByTagName("CharCode")[0].firstChild.data
    currency_dictionary[num_code] = char_code

print("\nСловарь NumCode - CharCode:")
print(currency_dictionary)


# Издательства без повторений
publishers = []

for book in books:
    publisher = book["Publisher"].strip()

    if publisher not in publishers:
        publishers.append(publisher)

print("\nИздательства без повторений:")
for publisher in publishers:
    print(publisher)


# 20 самых популярных книг
# Популярность определяется количеством загрузок.
popular_books = []

for book in books:
    downloads = int(book["Downloads"])
    title = book["Book-Title"]
    popular_books.append([downloads, title])

popular_books.sort(reverse=True)

print("\n20 самых популярных книг:")
number = 0

for book in popular_books:
    print(book[1], "- загрузок:", book[0])
    number = number + 1

    if number == 20:
        break