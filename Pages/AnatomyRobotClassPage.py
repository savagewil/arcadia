import pygame
import Components
import MainPage
from Pages import Page

class AnatomyRobotClassPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([150, 100], 150, "Anatomy of", ["red", "black"]),
            Components.Label.Label([100, 220], 150, "A Robot", ["red", "black"]),

            Components.Container.Container(512, 0, 1280, 512, [
                Components.Label.Label([50, 560], 40, "", ["gray", "black"], file="TextDocs/Anatomy.txt"),

                Components.Button.Button([100, 890], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),

            Components.PictureHolder.PictureHolder([800, 200], "Images/AnatomyOfRobot.jpg", scale=.150, rotate= -90)
        ]
