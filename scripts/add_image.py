import pygame

pygame.init()
white = (255, 255, 255)
height = 1200
width = 500
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Image')
image = pygame.image.load('/home/subham/Downloads/pygame_image.png')
done =False

while not done:
	screen.fill(white)
	screen.blit(image, (0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:

			done = True
	pygame.display.flip()
