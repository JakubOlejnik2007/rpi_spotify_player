import customtkinter as ctk


from screeninfo import get_monitors # !!! DEV


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #self.geometry("800x600")
        monitor_index = 0

        m = get_monitors()[monitor_index] # !!! DEV
        self.geometry(f"800x480+{m.x+1000}+{m.y}") # !!! DEV
        
        self.title("Eszutify")
        self.overrideredirect(True)
        self.resizable(False, False)
        
        self.bind("<Button-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)
        
    def start_move(self, event):
        """
            `self.overrideredirect(True)` completely disables native 
            support for draggable windows
        """
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        """
            `self.overrideredirect(True)` completely disables native 
            support for draggable windows
        """
        dx = event.x - self.x
        dy = event.y - self.y
        x = self.winfo_x() + dx
        y = self.winfo_y() + dy
        self.geometry(f"+{x}+{y}")
        
        
        

