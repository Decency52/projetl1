import random
import time

class Spaceship:
    def __init__(self, x, y, symbol="^"):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.lives = 3
        self.score = 0

class Enemy:
    def __init__(self, x, y, symbol="V"):
        self.x = x
        self.y = y
        self.symbol = symbol

class Bullet:
    def __init__(self, x, y, symbol="|"):
        self.x = x
        self.y = y
        self.symbol = symbol

def display_game(player, enemies, bullets, width, height):
    # Create empty game board
    board = [[" " for _ in range(width)] for _ in range(height)]
    
    # Place player
    board[player.y][player.x] = player.symbol
    
    # Place enemies
    for enemy in enemies:
        if 0 <= enemy.y < height and 0 <= enemy.x < width:
            board[enemy.y][enemy.x] = enemy.symbol
    
    # Place bullets
    for bullet in bullets:
        if 0 <= bullet.y < height and 0 <= bullet.x < width:
            board[bullet.y][bullet.x] = bullet.symbol
    
    # Display board
    print("\033[2J\033[H")  # Clear screen
    print("Space Shooter Game - Use A/D to move, S to shoot, Q to quit")
    print(f"Lives: {player.lives} | Score: {player.score}")
    print("-" * width)
    
    for row in board:
        print("".join(row))
    
    print("-" * width)

def main():
    width, height = 30, 20
    player = Spaceship(width // 2, height - 2)
    enemies = []
    bullets = []
    enemy_spawn_rate = 0.1
    game_over = False
    
    print("Space Shooter Game!")
    print("Controls: A - Move Left, D - Move Right, S - Shoot, Q - Quit")
    print("Press any key to start...")
    input()
    
    while not game_over:
        # Handle user input
        try:
            import msvcrt  # Windows-specific
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'a' and player.x > 0:
                    player.x -= 1
                elif key == 'd' and player.x < width - 1:
                    player.x += 1
                elif key == 's':
                    bullets.append(Bullet(player.x, player.y - 1))
                elif key == 'q':
                    game_over = True
        except ImportError:
            # Non-Windows systems
            pass
        
        # Move bullets
        for bullet in bullets[:]:
            bullet.y -= 1
            if bullet.y < 0:
                bullets.remove(bullet)
        
        # Move enemies
        for enemy in enemies[:]:
            enemy.y += 1
            if enemy.y >= height:
                enemies.remove(enemy)
                player.lives -= 1
                if player.lives <= 0:
                    game_over = True
        
        # Check for collisions
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.x == enemy.x and bullet.y == enemy.y:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    player.score += 10
                    break
        
        # Spawn new enemies
        if random.random() < enemy_spawn_rate:
            enemies.append(Enemy(random.randint(0, width - 1), 0))
        
        # Display game
        display_game(player, enemies, bullets, width, height)
        
        # Check for game over
        if player.lives <= 0:
            game_over = True
        
        time.sleep(0.2)
    
    print(f"Game Over! Final Score: {player.score}")

if __name__ == "__main__":
    main()
