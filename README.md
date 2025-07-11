# 🏓 Python Pong

A classic Pong game reimagined in Python! Battle against an intelligent AI or challenge a friend in local multiplayer mode. Experience the nostalgia of one of the first video games ever created, now with smooth 60 FPS gameplay and modern touches.

## 🎮 Game Features

- **Single Player Mode**: Test your skills against a smart AI that tracks the ball
- **Local Multiplayer**: Challenge a friend on the same keyboard
- **Smooth Gameplay**: 60 FPS with responsive controls
- **Win Condition**: First player to reach 5 points wins
- **Countdown Timer**: 3-second countdown before each round starts
- **Clean UI**: Minimalist design with hover effects

## 🕹️ How to Play

### Starting the Game
1. Run the game with `python run.py`
2. Select your game mode from the main menu:
   - **Single Player**: You vs AI
   - **Multiplayer**: Two players on one keyboard

### Controls

#### Single Player Mode
- **Arrow Keys**: Move your paddle up and down
- The AI controls the left paddle automatically

#### Multiplayer Mode
- **Player 1 (Right Paddle)**: ↑ / ↓ Arrow Keys
- **Player 2 (Left Paddle)**: W / S Keys

### Gameplay
- Use your paddle to hit the ball back to your opponent
- Score a point when the ball passes your opponent's paddle
- First player to score **5 points** wins the game!
- After each point, there's a 3-second countdown before the next round

## 🚀 Quick Start

Make sure you have Python and Pygame installed:

```bash
pip install pygame
```

Then run the game:

```bash
python run.py
```

## 🎯 Game Mechanics

- **Ball Physics**: The ball bounces realistically off paddles and walls
- **AI Behavior**: The computer opponent intelligently tracks the ball's position
- **Paddle Movement**: Smooth, responsive paddle control with momentum
- **Scoring System**: Real-time score display with win detection
- **Game States**: Seamless transitions between menu, gameplay, and victory screens

## 🏆 Winning

Victory goes to the first player to score 5 points! After winning, you'll see a victory message and automatically return to the main menu to start a new game.

## 🛠️ Technical Details

- **Built with**: Python 3.8+ and Pygame
- **Resolution**: 1280x960 pixels
- **Frame Rate**: 60 FPS
- **Architecture**: Object-oriented design with separate classes for game objects

## 🎨 Game Objects

- **Ball**: Moves at consistent speed with realistic collision detection
- **Paddles**: Responsive player-controlled rectangles with AI capabilities
- **UI Elements**: Clean buttons with hover effects and game information display

---

*Relive the classic arcade experience with modern Python programming! Perfect for learning game development or just having fun.* 🎮✨