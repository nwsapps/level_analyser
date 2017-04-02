"""
This module contains features for working with a group of levels.
"""


class DuplicationsSearch:
    """
    Levels duplications search.
    It searches for duplications in a list of levels.
    """

    def __init__(self, levels):
        self.levels = levels
        self.__duplications = []

    def search(self):
        """
        Performs the duplication search.
        Returns a list containg duplication tuples.
        If not duplications were found returns an empty list.
        """
        self.__reset()
        self.__perform_search()
        return self.__duplications

    def __reset(self):
        self.__duplications.clear()

    def __perform_search(self):
        size = len(self.levels)
        for i in range(size):
            for j in range(i + 1, size):
                if self.levels[i] == self.levels[j]:
                    self.__duplications.append((self.levels[i], self.levels[j]))


class DuplicationSearch:
    """
    Duplication search.
    It searches a list for duplications for a given level.
    """

    def __init__(self, levels, level):
        self.levels = levels
        self.level = level
        self.__duplications = []

    def search(self):
        """
        Executes the searching.
        Returns a list containg the levels which duplicates the search criteria.
        If no duplications were found then it returns an empty list.
        """
        self.__reset()
        self.__perform_search()
        return self.__duplications

    def __reset(self):
        self.__duplications.clear()

    def __perform_search(self):
        for level in self.levels:
            if level == self.level:
                self.__duplications.append(level)


if __name__ == '__main__':
    from level import Level, Matrix

    LEVELS = [
        Level(1, Matrix([
            [2, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]), 2),
        Level(2, Matrix([
            [3, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2]
        ]), 2),
        Level(3, Matrix([
            [1, 4, 4, 2],
            [4, 1, 4, 4],
            [4, 4, 1, 4],
            [3, 4, 4, 1]
        ]), 2),
        Level(4, Matrix([
            [1, 4, 4, 3],
            [4, 1, 4, 4],
            [4, 4, 1, 4],
            [2, 4, 4, 1]
        ]), 2),
        Level(5, Matrix([
            [3, 3, 3, 5],
            [3, 3, 5, 3],
            [3, 5, 3, 3],
            [5, 3, 3, 3]
        ]), 2),
        Level(6, Matrix([
            [7, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 7]
        ]), 2)
    ]

    SEARCH = DuplicationsSearch(LEVELS)
    DUPLICATIONS = SEARCH.search()
    print(DUPLICATIONS)

    LEVEL = Level(7, Matrix([
        [9, 4, 4, 4],
        [4, 4, 4, 4],
        [4, 4, 4, 4],
        [4, 4, 4, 9]
    ]), 2)

    SEARCH = DuplicationSearch(LEVELS, LEVEL)
    DUPLICATIONS = SEARCH.search()
    print(DUPLICATIONS)

