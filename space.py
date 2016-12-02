import arcade
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)

        self.ship = arcade.Sprite('img/ship.png')
        self.ship.set_position(100, 100)
    
    def animate(self, delta):
        if self.ship.center_y > SCREEN_HEIGHT:
            self.ship.center_y = 0
        self.ship.set_position(self.ship.center_x, self.ship.center_y + 5)
    
    def on_draw(self):
        arcade.start_render()
        self.ship.draw()
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()