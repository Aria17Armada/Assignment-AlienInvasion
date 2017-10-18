--snip--
def run_game():
    --snip--
    pygame.display.set_caption("Alien Invasion")
# Set the background color.
u bg_color = (230, 230, 230)
# Start the main loop for the game.
while True:
# Watch for keyboard and mouse events.
--snip--
# Redraw the screen during each pass through the loop.
v screen.fill(bg_color)
# Make the most recently drawn screen visible.
pygame.display.flip()
run_game()
