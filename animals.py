
animal1 = {
    'name': 'Dog',
    'group': 'mammals',
    'number_of_legs': 4,
    'skills': ['running', 'barking','bitting','eating']
    
}

animal2 = {
    'name': 'Cat',
    'group': 'mammals',
    'number_of_legs': 4,
    'skills': ['sleeping', 'climbing',]
}

animal3 = {
    'name': 'Parrot',
    'group': 'birds',
    'number_of_legs': 2,
    'skills': ['flying', 'mimicking','talking']
}
animal4 = {
    'name': 'Spider',
    'group': 'arachnids',
    'number_of_legs': 8,
    'skills': ['web spinning', 'climbing']
}
animal5 = {
    'name': 'Snake',
    'group': 'reptiles',
    'number_of_legs': 0,
    'skills': ['slithering', 'hunting']
}

animals = [animal1, animal2, animal3, animal4, animal5]

for animal in animals:
    print(animal)