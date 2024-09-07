from random import randint
import pgzrun
import pygame
WIDTH = 800
HEIGHT = 600
# Timer variables
time_limit = 60  # Seconds
time_elapsed = 0
# Score variables
fish_score = 0
plankton_score = 0
# Create actors
fish = Actor("fish")
fish.pos = (100, 100)
plankton = Actor("plankton")
plankton.pos = (randint(0, WIDTH), randint(0, HEIGHT))
def draw():
    screen.clear()
    screen.blit("background",(0,0))
    fish.draw()
    plankton.draw()
    screen.draw.text("Fish: " + str(fish_score), color="green", topleft=(10, 10))
    screen.draw.text("Plankton: " + str(plankton_score), color="blue", topleft=(10, 30))
    # Display game over message
    if time_elapsed >= time_limit:
        if fish_score > 20:
            screen.draw.text("You Win!", color="green", midtop=(WIDTH/2, HEIGHT/2 - 50), fontsize=60)
        else:
            screen.draw.text("You Lose!", color="blue", midtop=(WIDTH/2, HEIGHT/2 - 50), fontsize=60)
def update_timer():
    global time_elapsed
    time_elapsed += 1
def update():
    global fish_score, plankton_score
    # Move the fish
    if keyboard.left:
        fish.x -= 5
    if keyboard.right:
        fish.x += 5
    if keyboard.up:
        fish.y -= 5
    if keyboard.down:
        fish.y += 5
    # Check for collisions
    if fish.colliderect(plankton):
        fish_score += 1
        plankton.pos = (randint(0, WIDTH), randint(0, HEIGHT))
# Schedule the timer update function
clock.schedule_interval(update_timer, 1.0)  # Update timer every 1 second
pgzrun.go()
