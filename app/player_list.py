class PlayerList:
    def __init__(self, head=None):
        self._head = head

    def add_at_head(self, player_node):
        if self.is_empty():
            self._head = player_node
        else:
            player_node.next = self._head
            self._head.prev = player_node
            self._head = player_node
    def is_empty(self):
        return self._head is None