from environment import TicTacToe
from agent import Agent
import pickle

def train(episodes=1000000):
    env = TicTacToe()
    agent = Agent()

    for episode in range(episodes):
        state = env.reset()

        while not env.done:
            available = env.get_available_actions()
            action = agent.choose_action(state, available)
            next_state, reward, done = env.step(action)
            next_actions = env.get_available_actions()
            agent.update(state, action, reward, next_state, next_actions, done)
            state = next_state
    
    with open("qtable.pkl", "wb") as f:
        pickle.dump(agent.q_table, f)
    print("q table is saved")
    return agent


if __name__ =="__main__":
    trained_agent = train()
    print(f"Training done the agent knows {len(trained_agent.q_table)} states")