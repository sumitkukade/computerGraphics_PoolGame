import pygame
## this file should contain code which is ONLY Check current
## system is fulfill the requirement to run this game or not,
## please make requirement is False if something went wrong
requirementFlag = True
def checkSystem():
    print "current pygame version :-",pygame.ver
    try:
        if pygame.font is None:
            print "The font module is not available!"
            requirementFlag = False

        if pygame.cdrom is None:
            print "The cdrom module is not available!"
            requirementFlag = False

        if pygame.cursors is None:
            print "The cursers module is not available!"
            requirementFlag = False

        if pygame.display is None:
            print "The display module is not available!"
            requirementFlag = False

        if pygame.draw is None:
            print "The draw module is not available!"
            requirementFlag = False

        if pygame.event is None:
            print "The event module is not available!"
            requirementFlag = False

        if pygame.font is None:
            print "The font module is not available!"
            requirementFlag = False

        if pygame.image is None:
            print "The image module is not available!"
            requirementFlag = False

        if pygame.joystick is None:
            print "The joystick module is not available!"
            requirementFlag = False

        if pygame.key is None:
            print "The key module is not available!"
            requirementFlag = False

        if pygame.mixer is None:
            print "The mixer module is not available!"
            requirementFlag = False

        if pygame.mouse is None:
            print "The mouse module is not available!"
            requirementFlag = False

        if pygame.movie is None:
            print "The movie module is not available!"
            requirementFlag = False

        if pygame.music is None:
            print "The music module is not available!"
            requirementFlag = False

        if pygame.overlay is None:
            print "The overlay module is not available!"
            requirementFlag = False

        if pygame is None:
            print "install pygame"
            requirementFlag = False

        if pygame.rect is None:
            print "The rect module is not available!"
            requirementFlag = False

        if pygame.sndarray is None:
            print "The sndarray module is not available!"
            requirementFlag = False

        if pygame.sprite is None:
            print "The sprite module is not available!"
            requirementFlag = False

        if pygame.surface is None:
            print "The surface module is not available!"
            requirementFlag = False

        if pygame.surfarray is None:
            print "The surfarry module is not available!"
            requirementFlag = False

        if pygame.time is None:
            print "The time module is not available!"
            requirementFlag = False

        if pygame.transform is None:
            print "The transform module is not available!"
            requirementFlag = False
    except AttributeError as E:
        requirementFlag = False
        print E
    return requirementFlag

