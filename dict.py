# looping through dictionary

usersList = [
    {
        'id': 1,
        'name': 'Hassan',
        'age': 30,
        'location': 'Sakarya'
    },
    {
        'id': 2,
        'name': 'Hussein',
        'age': 20,
        'location': 'London'
    },
    {
        'id': 3,
        'name': 'Alex',
        'age': 40,
        'location': 'Barcelona'
    }
]


for _, item in enumerate(usersList):
    print(f"{item['name']} is {item['age']} years from {item['location']}")
