import pygame


class Button:
    def __init__(self, position: tuple, size: tuple, color: tuple, color_aim: tuple, color_down: tuple,
                 text=None, color_text=(255, 255, 255)):
        # Если какой-либо цвет равен (256, 256, 256), то не будет отрисован
        self.color_down = color_down
        self.color_aim = color_aim
        self.color = color
        self.color_text = color_text
        self.click = False
        self.mouse_position = (0, 0)
        self.size = size
        self.position = position
        self.button_pressed_left = False
        self.text = text

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

    def draw_left_click(self, display: pygame.surface.Surface):
        self.draw(display)
        return self.left_click()

    def draw(self, display):
        self.click = pygame.mouse.get_pressed()[0]
        if self.color != (256, 256, 256):
            pygame.draw.rect(display, self.color,
                             (self.position[0], self.position[1], self.size[0], self.size[1]))
        if self.check_aim():
            if self.color_aim != (256, 256, 256):
                pygame.draw.rect(display, self.color_aim,
                                 (self.position[0], self.position[1], self.size[0], self.size[1]))

            if self.click:
                if self.color_down != (256, 256, 256):
                    pygame.draw.rect(display, self.color_down,
                                     (self.position[0], self.position[1], self.size[0], self.size[1]))
        if self.text is not None:
            self.insert_text(display)

    def insert_text(self, display: pygame.surface.Surface):
        pygame.font.init()
        font = pygame.font.Font(None, 50)
        text = font.render(self.text, True, self.color_text)
        x = self.position[0] + self.size[0] / 2 - text.get_width() / 2
        y = self.position[1] + self.size[1] / 2 - text.get_height() / 2
        display.blit(text, (x, y))
