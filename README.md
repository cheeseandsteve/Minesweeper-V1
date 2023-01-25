# Minesweeper-V1


Window start at top left with coordinates of (0, 0)

if you place a shape at (20, 20) the top left corner of the shape will be at (20, 20)

    --> btn1 = Button(center_frame, bg="blue", text="first button") <creates a button>
    --> btn1.place(x=0, y=0) <Places the button in the (0, 0) coordinate of the center_frame frame not (0, 0) of the whole window>
    --> width=utils.width_prct(100), height=utils.height_prct(25) <Is using the def in utils and passing 25 means the
        height of the top frame will be 25% of the height of the window>
    --> highlightbackground="white" <Sets the colour of the border>
    --> highlightthickness=5 <Sets the thickness of the border to 5>
    --> "<Button-1>" <When left mouse button is pressed>
    --> "<Button-3>" <When right mouse button is pressed>


NOTE :

    --> {settings.WIDTH}x{settings.HEIGHT} <There must not be any spaces either side of the x or else it doesnt work>
    
    --> width=utils.width_prct(100), height=utils.height_prct(25) <Is using the def in utils and passing 25 means the height
        of the top frame will be 25% of the height of the window>
        
    --> highlightbackground="white" <Sets the colour of the border>
    
    --> highlightthickness=5 <Sets the thickness of the border to 5>
    
    --> "<Button-1>" <When left mouse button is pressed>
    
    --> "<Button-3>" <When right mouse button is pressed>

Video :

    --> https://www.youtube.com/watch?v=OqbGRZx4xUc&list=WL&index=1
    
    --> This is the youtube video i watched and all credits go to him
