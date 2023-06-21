# importataan pandas kirjasto
import pandas

# Luetaan data .csv tiedostosta
data = pandas.read_csv("squirrel.csv")
# Valitaan kaikki joiden turkin väri on harmaa
gray_squirrels = data[data['Primary Fur Color'] == "Gray"]
#Valitaan kaikki joiden turkin väri on musta
black_squirrels = data[data['Primary Fur Color'] == "Black"]
#Valitaan kaikki joiden turkin väri on punainen
red_squirrels = data[data['Primary Fur Color'] == "Cinnamon"]

# print(len(gray_squirrels))
# Muodostetaan uusi dictionary turkin värin perusteella
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    # Luvut tulevat aijemmin muodostetuista listoista
    # (yksinkertaisesti otetaan listan pituus len() funktiolla)
    "Count": [len(gray_squirrels), len(red_squirrels), len(black_squirrels)]
}

# Muodostetaan uusi DataFrame objekti diktionarysta
data_format = pandas.DataFrame(data_dict)
print(data_format)

# Tulos:
#   Fur Color  Count
# 0      Gray   2473
# 1  Cinnamon    392
# 2     Black    103


# Tulostetaan tiedot .csv tiedostoon
data_format.to_csv("squirrel_count.csv")

