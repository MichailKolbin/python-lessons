#
# Это не получилось
# необрезаются пробелы, вообще.
text1 = ' python '
print(text1)
text1.rstrip()
print(text1)
text1.lstrip()
print(text1)
text1.strip()
print(text1)
print("-----------------")

# Здесь предположительно должно было обрезать начало ("https://"). Не получилось

url = "https://nostarch.com"
print(url)
url.removeprefix("https://")
print(url)