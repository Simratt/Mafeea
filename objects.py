from typing import List, Dict, Optional

class Player:
    
    ''' A player in a game of Mafia 

    === Attributes ===
    - is_alive: the status of this player
    - name: A player's discord username

    === Repersentation Invariants ===
    - name must be a valid name
    '''
    
    is_alive: bool
    name: str
    
    def __init__(self, name: str) -> None:
        ''' Initializes this player'''
        self.name = name
        self.is_alive = True



class Game:
    ''' A game of Mafia

    === Attributes ===
    - Players: All the players in this Game
    - Doctors: The Doctor for this Game 
    - Mafia: The Mafia(s) for this Game 
    - Sherrif: The Sherrif(s) for this Game
    - Villagers: The Villager(s) for this Game
    === Representation Invariants ===
    TBD 
    '''
    Players: List[Player]
    Doctors: List[Player]
    Mafia: List[Player]
    Sherrif: List[Player]
    Villagers: List[Player]

    def __init__(self, players: list) -> None:
        self.Players = players
        self.Doctors = list()
        self.Mafia = list()
        self.Sherrif = list()
        self.Villagers = list()
    
