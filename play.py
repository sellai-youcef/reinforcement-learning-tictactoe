from environment import TicTacToe
from agent import Agent

def play():
    env = TicTacToe()
    agent = Agent()
    agent.load_q_table("qtable.pkl")
    state = env.reset()
    env.print_board()
    

    while not env.done:
        available = env.get_available_actions()
        if env.current_player==1:
            move = int(input(f"your move{available}: "))
            state, reward, done = env.step(move)

        else:
            print("agent thinks..")
            action = agent.choose_action(state, available)
            state, reward, done = env.step(action)
        
        env.print_board()
    
    if env.check_winner(1):
        print("you win!")
    elif env.check_winner(-1):
        print("agent win!")
    else:
        print("its a draw!")

if __name__ == "__main__":
    play()