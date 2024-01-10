import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ROPE_WIDTH = 20
PLAYER_SPEED = 5


class TugOfWarGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.player_position = SCREEN_WIDTH // 4
        self.opponent_position = 3 * SCREEN_WIDTH // 4

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        # Draw the rope
        arcade.draw_line(SCREEN_WIDTH // 2 - ROPE_WIDTH // 2, 0,
                         SCREEN_WIDTH // 2 - ROPE_WIDTH // 2, SCREEN_HEIGHT, arcade.color.BLACK, ROPE_WIDTH)
        arcade.draw_line(SCREEN_WIDTH // 2 + ROPE_WIDTH // 2, 0,
                         SCREEN_WIDTH // 2 + ROPE_WIDTH // 2, SCREEN_HEIGHT, arcade.color.BLACK, ROPE_WIDTH)

        # Draw the player
        arcade.draw_circle_filled(
            self.player_position, SCREEN_HEIGHT // 2, 20, arcade.color.BLUE)

        # Draw the opponent
        arcade.draw_circle_filled(
            self.opponent_position, SCREEN_HEIGHT // 2, 20, arcade.color.RED)

    def update(self, delta_time):
        # Update opponent position randomly
        self.opponent_position += random.choice([-1, 1]) * PLAYER_SPEED

    def on_key_press(self, key, modifiers):
        # Handle key press events
        if key == arcade.key.LEFT:
            self.player_position -= PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_position += PLAYER_SPEED

        # Check for winner
        self.check_winner()

    def check_winner(self):
        if self.player_position <= SCREEN_WIDTH // 2 - ROPE_WIDTH // 2:
            arcade.draw_text("Congratulations! You won!", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2,
                             arcade.color.GREEN, 20, width=300, align="center")
            arcade.finish_render()
            arcade.pause(2)
            arcade.close_window()
        elif self.player_position >= SCREEN_WIDTH // 2 + ROPE_WIDTH // 2:
            arcade.draw_text("Oh no! You lost. Better luck next time.", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2,
                             arcade.color.RED, 20, width=400, align="center")
            arcade.finish_render()
            arcade.pause(2)
            arcade.close_window()


if __name__ == "__main__":
    window = TugOfWarGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Tug of War Game")
    arcade.run()
