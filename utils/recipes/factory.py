# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_recipe():
    # Gera uma URL de imagem aleatória usando loremflickr
    width, height = rand_ratio()
    image_url = f'https://placehold.co/{width}x{height}?text=Food+Image'
    
    return {
        'id': fake.random_int(min=1, max=9999),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': image_url,
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())