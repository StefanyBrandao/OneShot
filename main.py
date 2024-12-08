import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(
size=(800, 500)
)
print('Setup End')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Finalizando...')
            pygame.quit()  # close window
