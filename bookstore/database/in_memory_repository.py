from bookstore.entities.book import Book


class InMemoryRepository:
    """
    Repositório em memória para armazenar objetos do tipo Book.

    Atributos:
        items (list): Lista de dicionários representando os livros.
    """

    def __init__(self):
        """Inicializa o repositório com uma lista vazia de itens."""
        self.items = []

    def serialize_book(self, item: Book):
        """
        Serializa um objeto do tipo Book em um dicionário.

        Args:
            item (Book): O objeto Book a ser serializado.

        Returns:
            dict: Um dicionário contendo os atributos do livro (título, autor e ano).
        """
        return {
            "title": item.getTitle(),
            "author": item.getAuthor(),
            "year": item.getYear(),
        }

    def add_book(self, item: Book):
        """
        Adiciona um livro serializado à lista de itens.

        Args:
            item (Book): O objeto Book a ser adicionado.
        """
        self.items.append(self.serialize_book(item))

    def get_book_by_title(self, title: str):
        """
        Busca um livro pelo título.

        Args:
            title (str): O título do livro a ser buscado.

        Returns:
            dict or None: O dicionário representando o livro encontrado ou None se não encontrar.
        """
        for book in self.items:
            if book["title"] == title:
                return book
        return None

    def list_all_books(self):
        """
        Lista todos os livros no repositório.

        Returns:
            list: Lista de dicionários representando todos os livros.
        """
        return [{"title": obj["title"], "author": obj["author"], "year": obj["year"]} for obj in self.items]

    def remove_book(self, title: str):
        """
        Remove um livro do repositório pelo título.

        Args:
            title (str): O título do livro a ser removido.

        Returns:
            bool: True se o livro foi removido com sucesso, False se o livro não foi encontrado.
        """
        book_to_remove = self.get_book_by_title(title)
        if book_to_remove:
            self.items.remove(book_to_remove)
            return True
        return False
