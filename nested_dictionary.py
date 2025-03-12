#Nestting List inside a dictionary

testing_dictionary = {
    "France": ["Paris", "Pfianf", "aurian"],
    "Germany": ["Berlin", "ainiae", "kjnfia"]
}

print(testing_dictionary)

#Nested dictionary inside a list of a dictionary

testing_list = {
    "France": {"Citiies": ["Paris", "Pfianf", "aurian"]},
    "Germany": {"City": ["Berlin", "ainiae", "kjnfia"]}
}

print(testing_list)

#Nested dictionary inside a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Little", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visted": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5}
]

print(travel_log)
