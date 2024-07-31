class Library:
    """
    Classe que representa uma biblioteca, responsável por gerenciar um repositório de livros.

    Atributos:
        repository: O repositório utilizado para armazenar os livros.
    """

    def __init__(self, repository):
        """
        Inicializa uma nova instância da classe Library.

        Args:
            repository: O repositório de livros.
        """
        self.repository = repository

    def add_book(self, book):
        """
        Adiciona um livro ao repositório.

        Args:
            book (Book): O livro a ser adicionado.
        """
        self.repository.add_book(book)

    def get_books_by_title(self, title):
        """
        Obtém livros pelo título.

        Args:
            title (str): O título do livro a ser buscado.

        Returns:
            dict or None: O dicionário representando o livro encontrado ou None se não encontrar.
        """
        return self.repository.get_book_by_title(title)

    def list_books(self):
        """
        Lista todos os livros no repositório.

        Returns:
            list: Lista de dicionários representando todos os livros.
        """
        return self.repository.list_all_books()

    def remove_book(self, title):
        """
        Remove um livro do repositório pelo título.

        Args:
            title (str): O título do livro a ser removido.

        Returns:
            bool: True se o livro foi removido com sucesso, False se o livro não foi encontrado.
        """
        return self.repository.remove_book(title)
