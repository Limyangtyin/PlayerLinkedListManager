from player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._next = None
        self._prev = None

    @property
    def player(self):
        return self._player

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node):
        self._prev = node

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"Player: {self._player}"