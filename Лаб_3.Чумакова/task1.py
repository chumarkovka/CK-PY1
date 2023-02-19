class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name_new: str) -> None:
        if not isinstance(name_new, str):
            raise TypeError("Неправильное название книги")
        else:
            self._name = name_new

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author_new: str) -> None:
        if not isinstance(author_new, str):
            raise TypeError("Неправильное имя автора")
        else:
            self._author = author_new

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages_new: int) -> None:
        if not isinstance(pages_new, int):
            raise TypeError("Число страниц должно выражаться целым числом")
        elif not pages_new > 0:
            raise ValueError("Число страниц должно выражаться положительным числом")
        else:
            self._pages = pages_new

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Число страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration_new: float) -> None:
        if not isinstance(duration_new, float):
            raise TypeError("Продолжительность книги должна выражаться дробным числом")
        elif not duration_new > 0:
            raise ValueError("Продолжительность книги должна выражаться положительным числом")
        else:
            self._duration = duration_new

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"


BOOK = PaperBook("Мастер и Маргарита", "Булгаков", 256)
print(BOOK.__str__())