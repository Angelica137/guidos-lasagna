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

    def elapsed_time_in_minutes(self, number_of_layers: int, elapsed_bake_time: int) -> int:
        '''
        Takes two parameters:
        `number_of_layers` (_the number of layers added to the lasagna_); 
        `elapsed_bake_time` (_the number of minutes the lasagna has been baking
        in the oven_). 
        Returns the total number of minutes user has been cooking.
        '''
        return elapsed_bake_time + self.preparation_time_in_minutes(number_of_layers)
