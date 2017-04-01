import level


class TwoLevelsComparison:
    """Processing of comparing two levels"""

    def __init__(self, level_one_reader, level_two_reader):
        self.__level_one_reader = level_one_reader
        self.__level_two_reader = level_two_reader
        self.__level_one = None
        self.__level_two = None

    def execute(self):
        """Executes the processing"""
        self.read_levels()
        self.compare_levels()

    def read_levels(self):
        self.__level_one = self.__level_one_reader.read()
        self.__level_two = self.__level_two_reader.read()

    def compare_levels(self):
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
    COMPARISON = TwoLevelsComparison(
        JsonFileLevelReader("test/level_1.json"),
        JsonFileLevelReader("test/level_2.json"))
    COMPARISON.execute()
