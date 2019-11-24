# VinylPriceUI.py

import sys, time
from math import ceil

from tkinter import Tk, StringVar, IntVar, Button, Entry, Label, messagebox, Checkbutton

page = 0
HasFocus    = True
root        = Tk()
root.wm_title( "EBW Vinyl Pricing Tool")
IsGlitter   = IntVar()
HeightEntry = StringVar()
PiecesEntry = StringVar()
OurCost     = StringVar()
TheirCost   = StringVar()
TotalCost   = StringVar()

#----------------------------------------------------------------------


class VinylPricing( object ):
	def __init__( self, CostPSI, PricePSI ):
		self.CostPSI  = CostPSI
		self.PricePSI = PricePSI
		self.W_Glit   = 20
		self.W_nGlit  = 15
	
	def Price( self, Height, Pieces = 1, Glitter = False ):
		if Glitter:
			return ( self.W_Glit * (Height+2)*self.PricePSI/Pieces, 
                      self.W_Glit * (Height+2)*self.CostPSI/Pieces )
		else:
			return ( self.W_nGlit * (Height+2)*self.PricePSI/Pieces, 
                      self.W_nGlit * (Height+2)*self.CostPSI/Pieces )
                      
                      

def HideFrame1():
    Glit_Checkbox.grid_remove()
    Height.grid_remove()
    HeightLabel.grid_remove()
    Pieces.grid_remove()
    PiecesLabel.grid_remove()
    ContButton.grid_remove()
    QuitButton.grid_remove()
    root.withdraw()

def HideFrame2():
    OurResultLabel.grid_remove()
    OurResultEntry.grid_remove()
    TheirResultLabel.grid_remove()
    TheirResultEntry.grid_remove()
    FinishButton.grid_remove()
    NewPriceButton.grid_remove()
    TotalEntry.grid_remove()
    TotalLabel.grid_remove()
    root.withdraw()
    
def ShowFrame2():
    global page
    OurResultLabel.grid( row = 0, column = 0, pady = 5, padx = 5, columnspan = 2 )
    OurResultEntry.grid( row = 1, column = 0, pady = 5, padx = 5, columnspan = 2 )
    TheirResultLabel.grid( row = 2, column = 0, pady = 5, padx = 5, columnspan = 2 )
    TheirResultEntry.grid( row = 3, column = 0, pady = 5, padx = 5, columnspan = 2 )
    TotalLabel.grid( row = 4, column = 0, pady = 5, padx = 5, columnspan = 2 )
    TotalEntry.grid( row = 5, column = 0, pady = 5, padx = 5, columnspan = 2 )
    FinishButton.grid( row = 6, column = 1, pady = 5, padx = 5 )
    NewPriceButton.grid( row = 6, column = 0, padx = 5, pady = 5)
    root.update()
    root.deiconify()
    page = 1
    
def ShowFrame1():
    global page
    Glit_Checkbox.grid( row = 0, column = 0, 
                columnspan = 2, pady = 5, padx = 5 )
    HeightLabel.grid( row = 1, column = 0, 
                columnspan = 2, pady = 5, padx = 5 )
    Height.grid( row = 2, column = 0, 
                columnspan = 2, pady = 5, padx = 5 )
    PiecesLabel.grid( row = 3, column = 0,
                columnspan = 2, padx = 5, pady = 5 )
    Pieces.grid( row = 4,  column = 0,
                columnspan = 2, pady = 5, padx = 5 )

    ContButton.grid( row = 5, column = 1, pady = 5, padx = 5  )
    QuitButton.grid( row = 5, column = 0, pady = 5, padx = 5  )
    root.update()
    root.deiconify()
    page = 0
    
    
    
    
    
def ContinueButton():
    HideFrame1()
    try:
        H = float(HeightEntry.get())
        P = float(PiecesEntry.get())
        if IsGlitter.get() == 0:
            price = Vinyl.Price( H, P )
        else:
            price = Vinyl.Price( H, P, True )
        TheirCost.set( "{:.02f}".format( round(price[0],2)))
        OurCost.set( "{:.02f}".format(round(price[1],2)))
        TotalCost.set( "{:.02f}".format(round(price[0] * int(PiecesEntry.get()),2)))
        ShowFrame2()
        pass
    except ValueError:
        tkMessageBox.showerror("Invalid Values","Height and/or Piece Count are not numbers.")
        ShowFrame1()
        pass
        
def ask_quit( b = False ):
    if not b:
        if messagebox.askokcancel("Quit", "Are you sure?"):
            root.destroy()
    else:
        root.destroy()
        
def RestartApp():
    HideFrame2()
    IsGlitter.set(0)
    HeightEntry.set("")
    PiecesEntry.set("")
    OurCost.set("")
    TheirCost.set("")
    TotalCost.set("")
    ShowFrame1()
    
def EnterKeyPress( args ):
    if page == 0:
        return ContinueButton()
    elif page == 1:
        return RestartApp()
        
def SetFocused( args ):
    global HasFocus
    if HasFocus:
        HasFocus = False
    else:
        HasFocus = True

root.bind("<Return>", EnterKeyPress )
root.bind("<FocusIn>", SetFocused )
root.bind("<FocusOut>", SetFocused )
root.bind("<Escape>", ask_quit )
root.protocol("WM_DELETE_WINDOW", ask_quit )
Vinyl       = VinylPricing( 0.03, 0.10 )

Glit_Checkbox = Checkbutton(root, text = "Glitter", 
                                    variable = IsGlitter, onvalue = 1, 
                                    offvalue = 0, height = 2, width = 10)

Height           = Entry( root, textvariable = HeightEntry)
HeightLabel      = Label( root, text = "Height:" )
Pieces           = Entry( root, textvariable = PiecesEntry)
PiecesLabel      = Label( root, text = "No. of Pieces:" )
OurResultEntry   = Entry( root, textvariable = OurCost)
OurResultLabel   = Label( root, text = "Our Cost:" )
TheirResultEntry = Entry( root, textvariable = TheirCost)
TheirResultLabel = Label( root, text = "Price per Piece:")
TotalEntry       = Entry( root, textvariable = TotalCost)
TotalLabel       = Label( root, text = "Total Price:")
ContButton       = Button( root, height = 2, width = 10, text = "Continue", command = ContinueButton )
FinishButton     = Button( root, height = 2, width = 10, text = "Done!", command = lambda:ask_quit(True) )
QuitButton       = Button( root, height = 2, width = 10, text = "Quit", command = ask_quit )
NewPriceButton   = Button( root, height = 2, width = 10, text = "New Price", command = RestartApp )

if __name__=="__main__":
    ShowFrame1()
    root.mainloop()
