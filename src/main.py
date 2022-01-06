import pygame
import sys
from start_menu import main_menu, terminate

main_menu()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			terminate()