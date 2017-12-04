"""
Create a Dodging game.
Ellipses will start at the top of the screen and 
fall downwards. 
The Player controls the movement of an ellipse 
at the bottom of the screen using the mouse.
The player must dodge the falling ball

Detailed steps are in the README.md file
"""

# GLOBAL VARIABLES
# Get your color scheme from https://coolors.co/
bg_color = "#F58F29"
primary_color = "#A4B0F5"
secondary_color = "#4464AD"

def setup():
    size(600, 800)

def draw():
    background(bg_color)
    
    # Draw Player
    noStroke()
    fill(primary_color)
    ellipse(50, 50, 50, 50)
    
    # Draw Falling ball
    fill(secondary_color)
    ellipse(100, 100, 30, 30)
