# Avión de Basura (Que se yo)

This project is a simple 2D game created using Pygame, where the player controls a spaceship and must navigate through enemies while avoiding collisions. The game features a projectile system, enemies that shoot back, and a main menu with interactive buttons.

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

---

## Features
- **Player Movement**: Control the player with WASD keys, shoot with space, and rotate the ship.
- **Projectile System**: Players and enemies can shoot projectiles with collision detection.
- **Enemies**: Enemies track the player and attempt to shoot them.
- **Collision System**: Detect collisions between enemies, player, and projectiles.
- **Simple UI**: Button class for menus and interactions.
- **Debug Mode**: Option to show hitboxes for all sprites.

---

## Prerequisites
To run this project, you need:
- **Python 3.8+**
- **Pygame**: You can install it using:
    ```bash
    pip install pygame
    ```

---

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/username/avion-de-basura.git
    ```
2. Navigate to the project directory:
    ```bash
    cd avion-de-basura
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage
To run the game, execute the following command:

```bash
python main.py
```

### Controls
- **Move**: Use `W`, `A`, `S`, `D` to move up, left, down, and right.
- **Shoot**: Press `SPACE` to shoot projectiles.
- **Rotate**: Use the `LEFT` and `RIGHT` arrow keys to rotate the player character.

### Game Flow
- **Player Movement**: Control the player's position using velocity and acceleration, while avoiding enemies.
- **Enemies**: Enemies will chase the player and attempt to shoot.
- **Projectiles**: Both player and enemies can shoot projectiles that deal damage upon collision.

---

## Contributing
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License
This project is licensed under the MIT License.

---
