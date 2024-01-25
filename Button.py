import pygame


class Button:
    def __init__(self, position, size, color, color_aim, color_down):
        # Если какой-либо цвет равен (1, 1, 1), то не будет отрисован
        self.color_down = color_down
        self.color_aim = color_aim
        self.color = color
        self.click = False
        self.mouse_position = (0, 0)
        self.size = size
        self.position = position
        self.button_pressed_left = False

    def check_aim(self):
        self.mouse_position = pygame.mouse.get_pos()
        if (self.mouse_position[0] >= self.position[0] and
                self.mouse_position[0] <= self.position[0] + self.size[0] and
                self.mouse_position[1] >= self.position[1] and
                self.mouse_position[1] <= self.position[1] + self.size[1]):
            return True
        return False

    def left_down(self):
        if self.check_aim() and pygame.mouse.get_pressed()[0]:
            return True
        return False

    def left_click(self):
        self.click = pygame.mouse.get_pressed()[0]
        if self.check_aim():
            if self.click:
                if not self.button_pressed_left:
                    self.button_pressed_left = True
            else:
                if self.button_pressed_left:
                    self.button_pressed_left = False
                    return True
        else:
            self.button_pressed_left = False
        return False

    def draw(self, screen):
        self.click = pygame.mouse.get_pressed()[0]
        if self.color != (256, 256, 256):
            pygame.draw.rect(screen, self.color,
                             (self.position[0], self.position[1], self.size[0], self.size[1]))
        if self.check_aim():
            if self.color_aim != (1, 1, 1):
                pygame.draw.rect(screen, self.color_aim,
                                 (self.position[0], self.position[1], self.size[0], self.size[1]))

            if self.click:
                if self.color_down != (1, 1, 1):
                    pygame.draw.rect(screen, self.color_down,
                                     (self.position[0], self.position[1], self.size[0], self.size[1]))
