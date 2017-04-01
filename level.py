"""Level module"""

import json


class JsonLevelParse:
    """Parse from JSON to Level object."""

    def __init__(self, json_data):
        self.json_data = json_data

    def parse(self):
        """Parses the JSON into a Level object"""
        data = json.loads(self.json_data)
        return Level(data['id'], Matrix(data['matrix']), data['shuffle_size'], data['version'])


class Level:
    """Level representation."""

    def __init__(self, level_id, matrix, shuffle_size, version):
        self.level_id = level_id
        self.matrix = matrix
        self.shuffle_size = shuffle_size
        self.version = version

    def __eq__(self, other):
        return self.matrix == other.matrix


class Matrix:
    """Level matrix pattern."""

    def __init__(self, values):
        self.values = values

    def __eq__(self, other):
        return Pattern(self) == Pattern(other)


class Pattern:
    """Represents a matrix pattern."""

    def __init__(self, matrix):
        values = []
        for row in matrix.values:
            for value in row:
                values.append(value)
        self.values = values

    def __eq__(self, other):
        if len(self.values) != len(other.values):
            return False
        else:
            return self.__compare(other)

    def __compare(self, other):
        size = len(other.values)
        for i in range(size):
            for j in range(i + 1, size):
                if not self.__compare_next(other, i, j):
                    return False
        return True

    def __compare_next(self, other, i, j):
        first = self.values[i] == self.values[j]
        second = other.values[i] == other.values[j]
        return first == second


if __name__ == '__main__':
    LEVEL_ONE = JsonLevelParse("""
    {
        "id": 1,
        "matrix": [
            [2, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ],
        "shuffle_size": 2,
        "version": 2
    }
    """).parse()

    LEVEL_TWO = JsonLevelParse("""
    {
        "id": 2,
        "matrix": [
            [3, 4, 4, 4],
            [4, 4, 4, 4],
            [4, 4, 4, 4],
            [4, 4, 4, 4]
        ],
        "shuffle_size": 3,
        "version": 2
    }
    """).parse()

    LEVEL_THREE = JsonLevelParse("""
    {
        "id": 2,
        "matrix": [
            [3, 2, 2, 7],
            [2, 3, 2, 2],
            [2, 2, 3, 2],
            [7, 2, 2, 3]
        ],
        "shuffle_size": 2,
        "version": 2
    }
    """).parse()

    assert LEVEL_ONE == LEVEL_TWO
    assert LEVEL_ONE != LEVEL_THREE
    print("Success!")
