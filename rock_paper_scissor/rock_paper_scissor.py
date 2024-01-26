import random
import sys

class RPS:
    def __init__(self):
        print("Welcome to Rock Paper Scissor with AI!")

        #moves for display
        self.moves = {"rock": "⛰️", "paper": "📜", "scissor": "✂"}
        self.valid_moves = list(self.moves.keys())

    def play_games(self):
        user_move = input("Rock, Paper, Scissor? >> ").lower()
        if user_move == "exit":
            print("Thanks for playing!")
            sys.exit()

        if user_move not  in self.valid_moves:
            print("Invalid move...")
            return self.play_games()
        
        ai_move = random.choice(self.valid_moves)
        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    def display_moves(self, user_move, ai_move):
        print("------")
        print(f"You: {self.moves[user_move]}")
        print(f"AI: {self.moves[ai_move]}")
        print("------")

    def check_moves(self, user_move, ai_move):
        if user_move == ai_move:
            print("It is a tie!")
        elif user_move == "rock" and ai_move == "scissor":
            print("You Win")
        elif user_move == "scissor" and ai_move =="paper":
            print("You win!")
        elif user_move =="paper" and ai_move =="rock":
            print("You win!")
        else:
            print("AI wins...")

if __name__ == "__main__":
    rps = RPS()
    
    while True:
        rps.play_games()
