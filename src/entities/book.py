class Book:
    """
    Classe que representa um livro.

    Atributos:
        __title (str): Título do livro.
        __author (str): Autor do livro.
        __year (int): Ano de publicação do livro.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Inicializa uma nova instância da classe Book.

        Args:
            title (str): O título do livro.
            author (str): O autor do livro.
            year (int): O ano de publicação do livro.

        Raises:
            ValueError: Se o título ou o autor forem vazios, ou se o ano não for um número inteiro positivo.
        """
        self.setTitle(title)
        self.setAuthor(author)
        self.setYear(year)

    def setTitle(self, title: str):
        """
        Define o título do livro.

        Args:
            title (str): O título a ser definido.

        Raises:
            ValueError: Se o título for vazio.
        """
        if not title:
            raise ValueError("Titulo nao pode ser vazio")
        self.__title = title

    def setAuthor(self, author: str):
        """
        Define o autor do livro.

        Args:
            author (str): O autor a ser definido.

        Raises:
            ValueError: Se o autor for vazio.
        """
        if not author:
            raise ValueError("Autor nao pode ser vazio")
        self.__author = author

    def setYear(self, year: int):
        """
        Define o ano de publicação do livro.

        Args:
            year (int): O ano a ser definido.

        Raises:
            ValueError: Se o ano não for um número inteiro positivo.
        """
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Ano deve ser um numero inteiro positivo")
        self.__year = year

    def getTitle(self) -> str:
        """
        Retorna o título do livro.

        Returns:
            str: O título do livro.
        """
        return self.__title

    def getAuthor(self) -> str:
        """
        Retorna o autor do livro.

        Returns:
            str: O autor do livro.
        """
        return self.__author

    def getYear(self) -> int:
        """
        Retorna o ano de publicação do livro.

        Returns:
            int: O ano de publicação do livro.
        """
        return self.__year
