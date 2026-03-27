import pandas as pd
from library_management.models import *

file = "library.xlsx"
df = pd.read_excel(file,header=0)      
records = df.to_dict('records')

for record in records:
    author,_ = Author.objects.get_or_create(name=record['AuthorName'])
    publisher,_ = Publisher.objects.get_or_create(name=record['PublisherName'])
    category,_ = Category.objects.get_or_create(name=record['Category'])
    book = Book.objects.filter(accession_number=record['AccessionNumber'])

    if not book:
        book = Book.objects.create(
            name = record['BookName'],
            keyword = record['Keywords'],
            classification_number = record['ClassificationNumber'],
            accession_number = record['AccessionNumber'],
            author = author,
            publisher = publisher,
            category = category
        )
    print(f"{record['AccessionNumber']} uploaded")