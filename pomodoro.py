import time
from win10toast import ToastNotifier
import tkinter as tk
import threading

class pomodoro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("430x220")
        self.root.title("Pomodoro")

        self.time_manage = tk.Entry(self.root, font=("Helvetica, 28"))
        self.time_manage.grid(row=0, column=0, columnspan=2,padx=4,pady=4)

        self.startbutt = tk.Button(self.root,font=("Helvetica, 28"), text= "Kick ASS", command=self.start_thread )
        #that threat is to allow gthe user to stop the count when the time started
        self.startbutt.grid(row=1, column=0, padx=4,pady=4)

        self.stopbutt = tk.Button(self.root,font=("Helvetica, 28"), text= "Back OFF", command=self.stop )
        self.stopbutt.grid(row=1, column=1, padx=4,pady=4)

        self.time_label = tk.Label(self.root,font=("Helvetica, 28"), text= "Time: 00:00:00 " )
        self.time_label.grid(row=2, column=0,columnspan=2, padx=4,pady=4)

        self.stop_loop = False
        self.root.mainloop()
    def start_thread(self):
        t = threading .Thread(target=self.start)   
        t.start()

    def start(self):
        self.stop_loop = False
        hours, minutes, seconds = 0,0,0
        strin_split = self.time_manage.get().split(":")
        if len(strin_split) == 3:
            hours = int(strin_split[0])
            minutes = int(strin_split[1])
            seconds = int(strin_split[3])
        elif len(strin_split) == 2:
            minutes = int(strin_split[0])
            seconds = int(strin_split[1]) 
        elif len(strin_split) == 1:
            seconds = int(strin_split[0])
        else:
            print("Enter a valid time format.") 
            return          
        full_seconds = hours*3600 + minutes*60 + seconds
        while full_seconds > 0 and not self.stop_loop:
            full_seconds -= 1

            minutes, seconds = divmod(full_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            self.time_label.config(text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)

        if not self.stop_loop:  
            toast = ToastNotifier()
            toast.show_toast("Pomodoro is over!", duration=10)
             
    def stop(self):
        self.stop_loop = True
        self.time_label.config(text = "Time: 00:00:00")
        
pomodoro()      