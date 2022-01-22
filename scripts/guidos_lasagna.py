class Lasagna:
    EXPECTED_BAKE_TIME = 40

    def bake_time_remaining(self, elpased_time: int) -> int:
        '''
        Returns reamining baking time.
        Takes one parameter: elpased_time and substracts it from the default
        cookingt ime EXPECTED_BAKE_TIME
        '''
        return self.EXPECTED_BAKE_TIME - elpased_time

    def preparation_time_in_minutes(self, layers: int) -> int:
        '''
        Takes the number of layers user wants to add to the lasagna as an argument
        and returns how many minutes they would spend making them.
        Each layer takes 2 minutes to prepare.
        '''
        return layers*2

    def elapsed_time_in_minutes(self, number_of_layers: int, elapsed_bake_time: int) -> int:
        '''
        Returns elapsed cooking time.
        Takes two parameters:
        `number_of_layers` (the number of layers added to the lasagna); 
        `elapsed_bake_time` (the number of minutes the lasagna has been baking in the oven). 
        '''
        return elapsed_bake_time + self.preparation_time_in_minutes(number_of_layers)
