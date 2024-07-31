from src.entities.book import Book


class BookBuilder:
    """
    Construtor de objetos Book com valores padrão.

    Atributos:
        title (str): Título do livro.
        author (str): Autor do livro.
        year (int): Ano de publicação do livro.
    """

    def __init__(self):
        """Inicializa o BookBuilder com valores padrão."""
        self.title = "Clean Code"
        self.author = "Robert C. Martin"
        self.year = 2012

    def with_title(self, title: str):
        """
        Define o título do livro.

        Args:
            title (str): O título a ser definido.

        Returns:
            BookBuilder: A própria instância de BookBuilder.
        """
        self.title = title
        return self

    def with_author(self, author: str):
        """
        Define o autor do livro.

        Args:
            author (str): O autor a ser definido.

        Returns:
            BookBuilder: A própria instância de BookBuilder.
        """
        self.author = author
        return self

    def with_year(self, year: int):
        """
        Define o ano de publicação do livro.

        Args:
            year (int): O ano a ser definido.

        Returns:
            BookBuilder: A própria instância de BookBuilder.
        """
        self.year = year
        return self

    def build(self) -> Book:
        """
        Constrói um objeto Book com os valores definidos.

        Returns:
            Book: Uma nova instância de Book com os atributos definidos.
        """
        return Book(self.title, self.author, self.year)
