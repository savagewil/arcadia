import pygame
import MainPage
import Components
from Pages import Page


class SafetyPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([210, 50], 100, "Safety 2015-and Beyond", ["red", "black"]),
            Components.Container.Container(250, 0, 1280, 924, [

                Components.Button.Button([1000, 475], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),

                Components.Label.Label([100, 270], 40, "", ["gray", "black"], file="TextDocs/Safety.txt")

            ], "grey")
        ]
