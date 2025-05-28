import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    """
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
""" 
    @pytest.mark.parametrize('book_name', ["Книга","Книга40символов_________________________"])
    def test_add_new_book_adds_valid_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.books_genre == {book_name: ''}

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_genre_true(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)
        assert collector.get_book_genre('Книга') == genre

    def test_get_book_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'
    
    @pytest.mark.parametrize('book_name, genre', [('Книга', 'Фантастика'),('Книга2', 'Ужасы')])
    def test_get_books_with_specific_genre_returns_a_list(self,book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    def test_get_books_with_specific_genre_returns_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Комедии')
        collector.set_book_genre('Книга2', 'Фантастика')
        assert collector.get_books_with_specific_genre('Комедии') == ['Книга1']
    
    def test_get_books_genre_returns_a_dict(self):
         collector = BooksCollector()
         collector.add_new_book('Книга')
         collector.set_book_genre('Книга','Фантастика')
         assert collector.get_books_genre() == {'Книга':'Фантастика'}

    @pytest.mark.parametrize('book_name, genre', [('Фантастическая', 'Фантастика'), ('Ужасная', 'Ужасы')])
    def test_get_books_for_children_returns_approved_list(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        if book_name == 'Фантастическая':
            assert book_name in collector.get_books_for_children()
        if book_name == 'Ужасная':
            assert book_name not in collector.get_books_for_children()

    @pytest.mark.parametrize('book_name', ['Книга', 'Книга2'])
    def test_add_book_in_favorites_adds_a_book_to_a_list(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('book_name', ['Книга', 'Книга2']) 
    def test_delete_book_from_favorites_deletes_book_from_the_favorites_books(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('book_name', ['Книга', 'Книга2'])    
    def test_get_list_of_favorites_books_returns_a_list(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert type (collector.get_list_of_favorites_books()) is list