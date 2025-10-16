from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])
persons = [Person('Timosha', 63, 193), Person('Eva', 47, 158),
           Person('Barsuсhok', 71, 172), Person('Alex', 45, 193),
           Person('Jeffry', 63, 193), Person('Ryanold', 41, 184),
           Person('Markus', 71, 172), Person('Alexey', 45, 193),
           Person('Jeffry', 63, 193), Person('Ryanold', 41, 184),
           Person('Arianatt', 28, 158), Person('Liam', 69, 193),
           Person('Eugene', 71, 172), Person('Alex', 45, 193),
           Person('Eugene', 63, 193), Person('Ryan', 41, 184),
           Person('Eugene', 28, 158), Person('Liam', 69, 193)]
group_iter = groupby(sorted(persons, key=lambda x: x[2]), key=lambda x: x[2])
for key, values in group_iter:
    print(f'{key}: {", ".join(sorted(list(map(lambda x: x[0], values))))}')
