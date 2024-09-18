import arcade
import arcade.key
import arcade.key

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'PONG GAME'




class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.jpg', 0.5)

    def update(self):
        self.center_x += self.change_x


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.jpg', 0.3)
        self.change_x = 3
        self.change_y = 3

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_WIDTH:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y



class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 7
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    
    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta_time: float):
        self.ball.update()
        self.bar.update()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.bar.change_x = 2
        if symbol == arcade.key.LEFT:
            self.bar.change_x = -2
    
    def

if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()