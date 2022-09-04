import sys
from morse_transformer import morse_transformer
from morse_plotter import plotter


if sys.platform == "win32":
    print("Win32")
    from sound_player import sound_player
elif sys.platform == "darwin":
    print("Mac")
    import pygame
else:
    print("Not defined")


# message = input('Enter your message: ')
message = "sos"

plotter(morse_transformer(message))

if sys.platform == "win32":
    print("Win32")
    sound_player(morse_transformer(message))

elif sys.platform == "darwin":
    print("Mac")

    pygame.init()

    gameDisplay = pygame.display.set_mode((640, 480))

    pygame.mixer.init()
    # pygame.mixer.music.load("morse_sound_long.wav")
    pygame.mixer.music.load(morse_transformer(message))
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
