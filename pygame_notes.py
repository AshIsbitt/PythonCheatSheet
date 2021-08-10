# Pygame in 90 minutes - Tech with Tim
# https://www.youtube.com/watch?v=jO6qQDNa2UY

#Pygame needs installing in terminal first
# > pip3 install pygame

import pygame
import os
#initialise fonts library and sound engine
pygame.font.init()
pygame.mixer.init()

#Pygame is a "2d graphics library that allows you to make simple projects"

#Create the main window and tell it what size to be
#all caps beacuse these are constants (even if the user changes the window size)
WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#set title bar name
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
FPS = 60
VELOCITY = 5
BULLET_VELOCITY = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

#sounds
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

#Define the font at what size
HEALTH_FONT = pygame.font.SysFont('Ubuntu', 40)
WINNER_FONT = pygame.font.SysFont('Ubuntu', 100)

#custom user events with IDs
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#Import spaceship graphics plus rotate/resize
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "space.png")), (WIDTH, HEIGHT))

#redirect from main() to draw on the screen
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
	#Set a background colour in the window
	#WIN.fill(WHITE)
	WIN.blit(SPACE, (0,0))

	#black border between the two sides of the screen using a different draw method
	pygame.draw.rect(WIN, BLACK, BORDER)

	#Draw graphics - "blit" creates surfaces (text or images)
	WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
	WIN.blit(RED_SPACESHIP, (red.x, red.y))

	#draw health text (always use that 1 for anti-alias)
	red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
	yellow_heath_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
	WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
	WIN.blit(yellow_heath_text, (10, 10))

	#draw bullets
	for bullet in red_bullets:
		pygame.draw.rect(WIN, RED, bullet)

	for bullet in yellow_bullets:
		pygame.draw.rect(WIN, YELLOW, bullet)

	#Update the display after making a change
	pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
	if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0: # LEFT
		yellow.x -= VELOCITY
	if keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < BORDER.x: # RIGHT
		yellow.x += VELOCITY
	if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0: # UP
		yellow.y -= VELOCITY
	if keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.width < HEIGHT: # DOWN
		yellow.y += VELOCITY

def red_handle_movement(keys_pressed, red):
	if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x + BORDER.width: # LEFT
		red.x -= VELOCITY
	if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH: # RIGHT
		red.x += VELOCITY
	if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0: # UP
		red.y -= VELOCITY
	if keys_pressed[pygame.K_DOWN]and red.y + VELOCITY + red.width < HEIGHT: # DOWN
		red.y += VELOCITY

#handle bullet movement and collsion
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
	for bullet in yellow_bullets:
		bullet.x += BULLET_VELOCITY

		if red.colliderect(bullet):
			#handle events created above
			pygame.event.post(pygame.event.Event(RED_HIT))
			yellow_bullets.remove(bullet)
		elif bullet.x > WIDTH:
			yellow_bullets.remove(bullet)

	for bullet in red_bullets:
		bullet.x -= BULLET_VELOCITY

		if yellow.colliderect(bullet):
			#handle events created above
			pygame.event.post(pygame.event.Event(YELLOW_HIT))
			red_bullets.remove(bullet)
		elif bullet.x < 0:
			red_bullets.remove(bullet)

def draw_winner(text):
	draw_text = WINNER_FONT.render(text, 1, WHITE)
	WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT//2 - draw_text.get_height()/2))
	pygame.display.update()
	pygame.time.delay(5000)

#This creates the main game code, IE updating a score, redrawing window, checking for collisions
def main():
	#Create a square to represent the spaceships
	red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	red_bullets = []
	yellow_bullets = []
	red_health = 10
	yellow_health = 10

	#This creates a clock for FPS
	clock = pygame.time.Clock()
	run = True
	while run:
		#This handles Frames per Second
		clock.tick(FPS)
		#check the various events happening here
		for event in pygame.event.get():
			
			#If the user quits the game
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				print("User quit")

			#Check which button is being pressed
			#if event.type == pygame.KEYDOWN:
  			#	print(pygame.key.name(event.key))

			#check for bullet firing keys
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LALT and len(yellow_bullets) < MAX_BULLETS:
					#draw the bullet as a rectangle
					bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
					yellow_bullets.append(bullet)
					#play a sound
					BULLET_FIRE_SOUND.play()
				if event.key == pygame.K_RMETA and len(red_bullets) < MAX_BULLETS:
					bullet = pygame.Rect(red.x, red.y + red.height// - 2, 10, 5)
					red_bullets.append(bullet)
					BULLET_FIRE_SOUND.play()

			if event.type == RED_HIT:
				red_health -= 1
				BULLET_HIT_SOUND.play()
			if event.type == YELLOW_HIT:
				yellow_health -= 1
				BULLET_HIT_SOUND.play()

		#Handle health and win condition
		winner_text = ""

		if red_health <= 0:
			winner_text = "Yellow Wins!"

		if yellow_health <= 0:
			winner_text = "Red Wins!"

		if winner_text != "":
			draw_winner(winner_text)
			break

		print(red_bullets)
		print(yellow_bullets)

		# Check what keyboard keys are being pressed and handle movement
		keys_pressed = pygame.key.get_pressed()
		yellow_handle_movement(keys_pressed, yellow)
		red_handle_movement(keys_pressed, red)

		handle_bullets(yellow_bullets, red_bullets, yellow, red)

		draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

	#Instead of quitting the game, restart by re-calling main
	#pygame.quit()
	main()

#Only run main() if this code is run from this page and not imported as a library
if __name__ == "__main__":
	main()