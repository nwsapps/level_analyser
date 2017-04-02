"""
The application module.
"""

import os
import level
import levels


class DuplicationFinder:
    """Processing for duplication finder"""

    def __init__(self, levels_reader, level_reader):
        self.__levels_reader = levels_reader
        self.__level_reader = level_reader
        self.__levels = []
        self.__level = None
        self.__duplications = []

    def execute(self):
        """Executes the processing"""
        self.__reset()
        self.__perform_search()

    def __reset(self):
        self.__duplications.clear()

    def __perform_search(self):
        self.__levels = self.__levels_reader.read()
        self.__level = self.__level_reader.read()
        self.__search_duplications()
        self.__show_results()

    def __search_duplications(self):
        search = levels.DuplicationSearch(self.__levels, self.__level)
        self.__duplications = search.search()

    def __show_results(self):
        if not self.__duplications:
            print("There are no duplications found.")
        else:
            duplications = ", ".join(str(e) for e in self.__duplications)
            print("The following duplications were found: " + duplications)


class DuplicationsFinder:
    """Processing for duplications finder"""

    def __init__(self, levels_reader):
        self.__levels_reader = levels_reader
        self.__levels = []
        self.__duplications = []

    def execute(self):
        """Executes the processing"""
        self.__reset()
        self.__perform_search()

    def __reset(self):
        self.__duplications.clear()

    def __perform_search(self):
        self.__levels = self.__levels_reader.read()
        self.__search_duplications()
        self.__show_results()

    def __search_duplications(self):
        duplications = levels.DuplicationsSearch(self.__levels).search()
        self.__duplications = duplications

    def __show_results(self):
        if self.__duplications:
            duplications = ", ".join(str(e) for e in self.__duplications)
            print("The following duplications were found: " + duplications)
        else:
            print("There are no duplications found.")


class JsonFilesLevelsReader:

    def __init__(self, levels_reader):
        self.__levels_reader = levels_reader

    def read(self):
        """Performs the reader"""
        levels_read = []
        for reader in self.__levels_reader:
            level_read = reader.read()
            levels_read.append(level_read)
        return levels_read


class JsonDirectoryInteractiveLevelsReader:

    def __init__(self, message='Enter with the directory which contains the levels files: '):
        self.__message = message

    def read(self):
        """Performs the reading"""
        directory = input(self.__message)
        return JsonDirectoryLevelsReader(directory).read()


class JsonDirectoryLevelsReader:

    def __init__(self, directory):
        self.__directory = directory

    def read(self):
        """Performs the reading"""
        files = os.listdir(self.__directory)
        levels_read = []
        for file in files:
            if file.endswith('.json'):
                reader = JsonFileLevelReader(self.__directory + '/' + file)
                level_read = reader.read()
                levels_read.append(level_read)
        return levels_read


class TwoLevelsComparison:
    """Processing of comparing two levels"""

    def __init__(self, level_one_reader, level_two_reader):
        self.__level_one_reader = level_one_reader
        self.__level_two_reader = level_two_reader
        self.__level_one = None
        self.__level_two = None

    def execute(self):
        """Executes the processing"""
        self.__read_levels()
        self.__compare_levels()

    def __read_levels(self):
        self.__level_one = self.__level_one_reader.read()
        self.__level_two = self.__level_two_reader.read()

    def __compare_levels(self):
        if self.__level_one == self.__level_two:
            self.__on_equals_levels()
        else:
            self.__on_different_levels()

    def __on_different_levels(self):
        print("The two levels are differents.")

    def __on_equals_levels(self):
        print("The two levels are equals.")


class JsonFileInteractiveLevelReader:
    """JSON File interactive level reader."""

    def __init__(self, message='Enter with a level path: '):
        self.message = message

    def read(self):
        level_path = input(self.message)
        return JsonFileLevelReader(level_path).read()


class JsonFileLevelReader:
    """JSON File direct level reader"""

    def __init__(self, level_path):
        self.level_path = level_path

    def read(self):
        level_file = open(self.level_path, 'r')
        return level.JsonLevelParse(level_file.read()).parse()


if __name__ == '__main__':
    FINDER = DuplicationsFinder(
        JsonDirectoryInteractiveLevelsReader())
    FINDER.execute()
