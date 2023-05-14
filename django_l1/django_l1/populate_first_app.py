from faker import Faker
import random
import django
import os

# populate db with fake data
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()

    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        topic_name = add_topic()

        # create the fake date for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_company = fakegen.company()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(
            topic=topic_name, url=fake_url, name=fake_company)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_l1.settings')
    django.setup()
    from first_app.models import Topic, Webpage, AccessRecord

    print('Populating data...')
    populate(20)
    print('Population complete.')
