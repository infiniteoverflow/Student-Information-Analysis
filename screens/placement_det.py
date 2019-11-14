from tkinter import *

class PlacementDetails:
    def __init__(self,branch):
        self.branch = branch
        self.root = Tk()
        self.root.geometry("2000x1024")
        self.root.title("Placement Details for {}".format(branch))
        
        