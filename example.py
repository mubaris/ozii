import ozii as oz

texts = [
    "Hello World",
    "Barry Allen",
    "Barry",
    "Allen",
    "Iris West",
    "Iris",
    "West",
    "Cisco Ramon",
    "Cisco",
    "Ramon",
    "Barry Allen is The Flash",
    "The Flash",
    "Flash",
    "Batman",
    "I am Batman",
    "Time",
    "time",
    "Iris is dead",
    "Before and After",
    "ozii",
    "Human",
    "Humanity",
    "Cisco eats apple",
    "Weapon",
    "There is no linear time.",
    "Where is Cisco?"
]

for i, text in enumerate(texts):
    oz.generate_image(text, pixels=400, dir="examples")