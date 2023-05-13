travel_log = [
{
    "country": "France",
    "cities_visited": ["Lyon", "Paris", "Lille"],
    "times_visited": 12,
},
{
    "country": "Germany",
    "cities_visited": ["Asdf", "Beds", "Caes"],
    "times_visited": 7,
}
]


def add_new_country(countryy, cities_v, times_v):
    new_country = {}
    new_country["country"] = countryy
    new_country["cities_visited"] = cities_v
    new_country["times_visited"] = times_v
    travel_log.append(new_country)

add_new_country("Brasil", ["Salvador", "Lauro"], 3)
print(travel_log)