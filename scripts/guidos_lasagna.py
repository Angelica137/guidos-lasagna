class Lasagna:
    EXPECTED_BAKE_TIME = 40

    def bake_time_remaining(self, time: int) -> int:
        return self.EXPECTED_BAKE_TIME - time

    def preparation_time_in_minutes(self, layers: int) -> int:
        '''
        Takes the number of layers user wants to add to the lasagna as an argument
        and returns how many minutes they would spend making them.
        Each layer takes 2 minutes to prepare.
        '''
        return layers*2
