import pygame
import Components
import MainPage
from Pages import Page


class RemotePage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([150, 100], 150, "Controls", ["red", "black"]),

            Components.Container.Container(512, 0, 1280, 512, [
                Components.Label.Label([100, 550], 60, "Remote Controls", ["red", "black"]),

                Components.Button.Button([500, 750], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),
        ]
        self.mouseSpeed = 4
