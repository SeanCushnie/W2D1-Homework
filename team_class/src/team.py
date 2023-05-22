class Team:
    def __init__(self, player_name, player_list, coach_name):
        self.name = player_name
        self.players = player_list
        self.coach = coach_name

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, input_player):
        for player in self.players:
            if (player == input_player):
                return True
        
        return False