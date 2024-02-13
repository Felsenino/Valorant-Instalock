import tkinter as tk

#main window
window = tk.Tk() 
window.geometry("1280x720")
window.title("Valorant Instalocker v0.1 by Felsen")
window.resizable(False, False)
window.configure(background="black")

def log():
    print("Works")

#select button
select_button = tk.Button(

    text = "Select",
    
    

)

select_button.grid(row=0, column=0)



#Main
if __name__ == "__main__":
    window.mainloop()