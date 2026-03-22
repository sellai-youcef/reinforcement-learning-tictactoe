class TicTacToe:

    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [0,0,0,0,0,0,0,0,0]
        self.current_player=1
        self.done= False

    def print_board(self):
        symbols ={0: ".", 1:"X", -1: "O"}
        for r in range(3):
            print(" ".join(symbols[self.board[r*3+c]] for c in range(3)))

    def get_available_actions(self):
        return[c for c in range (9) if self.board[c]==0]
    
    def check_winner(self, player):
        lines=[
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6],
        ]
        return any(all(self.board[i] == player for i in line)for line in lines)
    
    def step(self, action):
        self.board[action]= self.current_player
        if(self.check_winner(self.current_player)==True):
            self.done=True
            return tuple(self.board), 1, True
        elif not self.get_available_actions():
            self.done=True
            return tuple(self.board), 0.5, True
        else:
            self.current_player*= -1
            return tuple(self.board), 0, False
        
if __name__=="__main__":
    game=TicTacToe()
    game.print_board()
    game.step(0)
    game.step(4)
    game.print_board()