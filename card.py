from flet import *

def main(page:Page):
    page.window_width = 350
    page.window_height = 600
    page.window_always_on_top = True
    # page.bgcolor = 'lightblue'

    card = Card(
        content=Container(
            content=Text(value="this card"),
            alignment=alignment.center,
            padding=10,
        ),
    width=200,
    height=200,
    elevation=10,
    margin=20 # that is from outer side spacing
    )
    
    page.add(card)



app(target=main)