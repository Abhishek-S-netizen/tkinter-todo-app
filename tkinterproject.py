import tkinter as tk
from tkinter import messagebox

def function(Event=None):
    task_canvas.configure(scrollregion=task_canvas.bbox("all"))

    
root = tk.Tk()
root.config(background="#121212")
root.title("TO-DO")
root.geometry("600x750")

frame = tk.Frame(root)

task_canvas = tk.Canvas(frame,
                        background="#121212",
                        height=300,
                        width=450,
                        highlightthickness=0)

task_scroll = tk.Scrollbar(frame,
                           orient="vertical",
                           command=task_canvas.yview)

task_canvas.config(yscrollcommand=task_scroll.set)

task_canvas.pack(side="left")
task_scroll.pack(side="right",fill="y")

tasks_frame = tk.Frame(task_canvas,
                       background="#121212")

task_canvas.create_window((0,0),window=tasks_frame)
tasks_frame.bind("<Configure>",function)

frame_1 = tk.Frame(root)

button_frame = tk.Frame(frame_1,
                        background="#121212")

d = {}
task_index = 1
def add_task(Event=None):
    global task_index
    task = task_entry.get()

    if (len(d) == 0):
        task_index = 1

    if (task == ""):
        messagebox.showinfo("Warning","Please enter a task")
    else:
        temp = f"  {task_index}   :   " + task
            
        task_label = tk.Label(tasks_frame,
                              text=temp,
                              font=("Consolas",15),
                              background="#4a4a4a",
                              foreground="white",
                              width=40,
                              anchor="w")
        task_label.pack(pady=10)
        
        task_entry.delete(0,tk.END)
        d[task_index] = task_label
        task_index += 1
        print(d)
            
            
def mark_as_done():
    index = task_option_entry.get()

    if (index == ""):
        messagebox.showinfo("Warning","Please enter an ID number")
    else:
        try:
            label = d[int(index)]
            label.config(background="#00b894")
            task_option_entry.delete(0,tk.END)
        except KeyError:
            messagebox.showinfo("Warning","No task with ID " + index)
        except ValueError:
            messagebox.showinfo("Warning","Invalid ID")


    
def update_task():
    index = task_option_entry.get()

    if (index == ""):
        messagebox.showinfo("Warning","Please enter an ID")
    else:

        def confirm_update():
            updated_text = updated_task.get()

            if (updated_text == ""):
                messagebox.showinfo("Warning","Please enter updated task")
            else:
                temp = f"  {index}   :   " + updated_text
                label = d[int(index)]
                label.config(text=temp)
                popup.destroy()
                task_option_entry.delete(0,tk.END)
                
        try:
            label = d[int(index)]
            popup = tk.Toplevel(root)
            popup.geometry("300x150")
            popup.config(background="gray")

            updated_task = tk.Entry(popup,font=("Consolas",15))
            updated_task.pack(pady=20)

            updated_confirm = tk.Button(popup,
                                        text="Done",
                                        font=("Consolas",14),
                                        background="#ff0a16",
                                        foreground="white",
                                        activebackground="black",
                                        activeforeground="white",
                                        command=confirm_update)
            updated_confirm.pack(pady=10)
        except KeyError:
            messagebox.showinfo("Warning","No task with ID " + index)
        except ValueError:
            messagebox.showinfo("Warning","Invalid ID")


def remove_task():
    index = task_option_entry.get()

    if (index == ""):
        messagebox.showinfo("Warning","Please enter an ID")
    else:
        try:
            label = d[int(index)]
            label.destroy()
            del d[int(index)]
            task_option_entry.delete(0,tk.END)
        except KeyError:
            messagebox.showinfo("Warning","No task with ID " + index)
        except ValueError:
            messagebox.showinfo("Warning","Invalid ID")

    task_canvas.yview_moveto(0)

    
def maximise(Event=None):
    root.state("zoomed")

def minimise(Event=None):
    root.state("normal")

task_entry = tk.Entry(root,font=("Consolas",14),
                      background="gray",
                      foreground="white",
                      width=30)

task_entry.pack(pady=10)

task_submit = tk.Button(root,text="Add",
                        font=("Consolas",15),
                        background="#ff0a16",
                        foreground="white",
                        activebackground="black",
                        activeforeground="white",
                        command=add_task)

task_submit.pack(pady=10)
frame.pack()



frame_1.pack(pady=20)
frame_1.config(background="#121212")
task_option_entry = tk.Entry(frame_1,
                             font=("Consolas",14),
                             background="gray",
                             foreground="white",
                             width=10,
                             justify="center")
task_option_entry.pack()

task_done_button = tk.Button(button_frame,
                             text="Done",
                             font=("Consolas",15),
                             command=mark_as_done,
                             background="#ff0a16",
                             foreground="white",
                             activebackground="black",
                             activeforeground="white",
                             width=7)

task_update_button = tk.Button(button_frame,
                               text="Update",
                               font=("Consolas",15),
                               command=update_task,
                               background="#ff0a16",
                               foreground="white",
                               activebackground="black",
                               activeforeground="white",
                               width=7)


task_delete_button = tk.Button(button_frame,
                               text="Remove",
                               font=("Consolas",15),
                               command=remove_task,
                               background="#ff0a16",
                               foreground="white",
                               activebackground="black",
                               activeforeground="white",
                               width=7)


task_done_button.pack(side="left",padx=5)
task_update_button.pack(side="left",padx=5)
task_delete_button.pack(side="left",padx=5)

button_frame.pack(pady=10)

label_info = tk.Label(root,
                      text="F11 - Maximise\nF12 - Minimise\nReturn - Add task",
                      background="#121212",
                      foreground="white",
                      justify="left")
label_info.pack(pady=10)


root.bind("<Return>",add_task)
root.bind("<Key-F11>",maximise)
root.bind("<Key-F12>",minimise)

root.mainloop()
