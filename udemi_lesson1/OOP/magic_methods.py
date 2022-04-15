# __init__ вызывается автоматически при создании объекта

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # специальный метод __str__ строковое представление классе Book
    def __str__(self):
        return f'{self.author}'

    # метод для определения длины
    def __len__(self):
        return self.pages  # количество страниц в книге


b = Book('Руководство по Python', 'Влад', 100)
print(b)  # __str__
print(len(b))  # __len__



