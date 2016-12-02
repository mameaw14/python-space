import arcade
from models import Ship
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)

        self.ship = Ship(100, 100)
        self.ship_sprite = arcade.Sprite('img/ship.png')
    
    def animate(self, delta):
        if self.ship_sprite.center_y > SCREEN_HEIGHT:
            self.ship_sprite.center_y = 0
        self.ship_sprite.set_position(self.ship_sprite.center_x, self.ship_sprite.center_y + 5)
    
    def on_draw(self):
        arcade.start_render()
        self.ship_sprite.draw()
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()