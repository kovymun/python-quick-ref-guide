# OBJECTED ORIENTATED PROGRAMMING IN PYTHON

# CREATING A CLASS
# Example: Football Players

class FootballPlayers:
  def __init__(self, name, nationality, goals_scored):
    self.name = name
    self.nationality = nationality
    self.goals_scored = goals_scored

  def __str__(self):
    return f"Player: {self.name}, Nationality: {self.nationality}, Goals Scored: {self.goals_scored}"

# OBJECT: INSTANTIATING AN INSTANCE OF A CLASS.

player_calvin_williams = FootballPlayers("Calvin Williams", "South Africa", goals_scored=34)
print(player_calvin_williams)
