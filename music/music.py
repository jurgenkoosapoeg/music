from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from random import choice

height = 650
width = 1000

def create_img(pos):
    _img = Image.open('neck.PNG')

    draw = ImageDraw.Draw(_img)
    draw.circle(xy=pos,
                radius=8,
                fill=(0, 255, 0),
                outline=(255, 0, 0),
                width=5)


    target_height = 630
    aspect_ratio = _img.width / _img.height
    new_width = int(target_height * aspect_ratio)

    _img = _img.resize((new_width, target_height), Image.Resampling.LANCZOS)

    return _img

noodid = {
    (135, 335): 'F', (134, 395): 'F#', (133, 449): 'G', (132, 502): 'G#', (131, 550): 'A',
    (130, 596): 'A#', (129, 641): 'B', (129, 681): 'C', (128, 720): 'C#', (128, 756): 'D',
    (127, 792): 'D#', (127, 825): 'E', (149, 336): 'A#', (148, 397): 'B', (149, 449): 'C',
    (149, 501): 'C#', (148, 551): 'D', (148, 597): 'D#', (148, 639): 'E', (148, 681): 'F',
    (148, 721): 'F#', (148, 756): 'G', (148, 792): 'G#', (148, 825): 'A', (165, 337): 'D#',
    (165, 394): 'E', (165, 448): 'F', (165, 502): 'F#', (166, 551): 'G', (166, 595): 'G#',
    (167, 639): 'A', (167, 680): 'A#', (167, 720): 'B', (168, 756): 'C', (168, 791): 'C#',
    (168, 824): 'D', (178, 336): 'G#', (179, 396): 'A', (180, 449): 'A#', (181, 501): 'B',
    (181, 550): 'C', (183, 596): 'C#', (184, 640): 'D', (184, 681): 'D#', (185, 720): 'E',
    (186, 757): 'F', (186, 792): 'F#', (187, 824): 'G'
}


root = tk.Tk()
root.minsize(width, height)
root.maxsize(width, height)

class Fretboard(tk.Frame):

    def __init__(self, parent, width, height):
        super().__init__(parent, width=width, height=height)
        self.place(x=0, y=0)

        tk.Label(self, text="Töötab").place(x=50, y=100)

        btn = tk.Button(self, text="Tagasi", command=menu)
        btn.place(x=100, y=200)


class Menu(tk.Frame):

    def __init__(self, parent, width, height):
        super().__init__(parent, width=width, height=height)
        self.place(x=0, y=0)

def kontrolli_nooti(noot, vajutatud_noot):
    if noot == vajutatud_noot:
        fretboard(1)
    else:
        fretboard(2)

def fretboard(value):
    frame2 = tk.Frame(root, width=width, height=height, bg="purple")
    frame2.place(x=0, y=0)

    btn = tk.Button(frame2, text="Tagasi", command=menu)
    btn.place(x=930, y=10)

    koordinaat = choice(list(noodid.keys()))
    noot = noodid[koordinaat]
    image = create_img(koordinaat)

    if value:
        if value == 1:
            tk.Label(frame2, text="Õige", font=("Helvetica", 48), bg="purple", fg="green").place(x=300, y=500)
        else:
            tk.Label(frame2, text="Vale", font=("Helvetica", 48), bg="purple",
                     fg="red").place(x=300, y=500)

    nupud = {
        "C": (400, 200), "C#": (450, 200), "D": (500, 200), "D#": (550, 200),
        "E": (400, 250), "F": (450, 250), "F#": (500, 250), "G": (550, 250),
        "G#": (400, 300), "A": (450, 300), "A#": (500, 300), "B": (550, 300)
    }

    for nupp in nupud:
        x = nupud[nupp][0]
        y = nupud[nupp][1]
        tk.Button(frame2, text=nupp, width=3, command=lambda idx=nupp: kontrolli_nooti(noot, idx)).place(x=x, y=y)

    img_tk = ImageTk.PhotoImage(image)
    label = tk.Label(frame2, image=img_tk)
    label.image = img_tk
    label.place(x=10, y=10)


def menu():
    frame = tk.Frame(root, width=width, height=height, bg="purple")
    frame.place(x=0, y=0)

    fretboard_btn = tk.Button(frame, text="Fretboard", justify="center", width=20, command=lambda: fretboard(0))
    fretboard_btn.place(x=300, y=200)

img = create_img((50, 50))
menu()
root.mainloop()