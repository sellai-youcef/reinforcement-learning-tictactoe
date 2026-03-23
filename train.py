from environment import TicTacToe
from agent import Agent

def train(episodes=50000):
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
    return agent

if __name__ =="__main__":
    trained_agent = train()
    print(f"Training done the agent knows {len(trained_agent.q_table)} states")