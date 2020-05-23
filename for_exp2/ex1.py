
def city_country():
    # print(" Название страны: " + name_country )
    country = input("1")
    return country
`

# name = city_country(name_country=str(input("Введите значение страны : ")))


def city_country2():
    # print("Название города: " + name_city)
    city = input("2")
    return city

# name1= city_country2(name_city=str(input("Введите значение города : ")))


print("Название страны: " + city_country(),
      "Навзание города: " + city_country2())
