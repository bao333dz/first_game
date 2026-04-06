# First Project - Ghost Game

A fun Pygame-based game where you control a player character and shoot lines to eliminate ghosts before they catch you!

## Features

- **Player Control**: Move left (A) and right (D), jump with Space or Up Arrow
- **Shooting Mechanic**: Click to draw a line that destroys ghosts on contact
- **Pause System**: Press P to pause/resume the game
- **Score Tracking**: Keep track of how many ghosts you've eliminated
- **Game Over**: Game ends when a ghost reaches you
- **Restart**: Press R on the game over screen to play again

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install required dependencies:
   ```bash
   pip install pygame
   ```

2. Ensure you have the required game assets in the `pygame/graphics/` directory:
   - `sky.png`
   - `ground.png`
   - `player.png`
   - `ghost.png`

## How to Run

```bash
python pygame/visual.py
```

## Controls

| Key | Action |
|-----|--------|
| A | Move left |
| D | Move right |
| Space / Up Arrow | Jump |
| Left Click | Shoot line to destroy ghosts |
| P | Pause/Resume |
| R | Restart (when game over) |

## Gameplay

1. Avoid the ghosts moving from right to left
2. Use your jumping mechanics to dodge incoming ghosts
3. Click to shoot lines and eliminate ghosts
4. Each ghost eliminated increases your score
5. Don't let a ghost catch you - game over!

## Game States

- **Active**: Play the game normally
- **Paused**: Game is frozen, press P to continue
- **Game Over**: Ghost caught you, press R to restart

## Project Structure

```
first_game/
├── pygame/
│   ├── visual.py          # Main game file
│   └── graphics/          # Game assets
│       ├── sky.png
│       ├── ground.png
│       ├── player.png
│       └── ghost.png
└── README.md              # This file
```
