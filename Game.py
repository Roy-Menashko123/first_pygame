import pygame



def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    button1 = pygame.Rect(100, 200, 120, 50)
    button2 = pygame.Rect(300, 200, 120, 50)
    red = pygame.Color('red')
    green = pygame.Color('green')
    blue = pygame.Color('blue')
    lst = [red,green,blue]
    white = pygame.Color('white')
    finish = False
    count1 = 0
    count2 = -1
    img1 = pygame.image.load("img1.png")
    img2 = pygame.image.load("img2.png")
    im_lst = [img1,img2]
    im_lst[0] = pygame.transform.scale(im_lst[0], (150, 100))
    im_lst[1] = pygame.transform.scale(im_lst[1], (150, 100))
    while not finish:




        pygame.draw.rect(screen, white, button1)
        pygame.draw.rect(screen, white, button2)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    screen.fill(lst[count1%3])
                    count1 += 1
                    if count2 >= 0:
                        screen.blit(im_lst[count2 % 2], (500, 150))
                if button2.collidepoint(event.pos):
                    count2 += 1
                    screen.blit(im_lst[count2%2], (500, 150))



        pygame.display.flip()


if __name__ == "__main__":
    main()


