from tkinter import *
import customtkinter
from PIL import Image,ImageTk




class Index:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1018+0+0")
        self.root.title("INVENTORY MANAGEMENT SYSTEM")

        #customtkinter.set_appearance_mode("light")
        left_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        left_frame.place(x=10,y=10,width=200,height=700)




        #active label
        active_ent=customtkinter.CTkLabel(left_frame,text="ACTIVE",font=("times new roman",25),text_color="black"
                                          )
        active_ent.place(x=50,y=10)
        enterprise_ent = customtkinter.CTkLabel(left_frame, text="ENTERPRISES", font=("times new roman", 25), text_color="black",
                                            anchor="center")
        enterprise_ent.place(x=20,y=40)

#for dashboard
        self.dashboard_btn=customtkinter.CTkButton(left_frame,text="Dashboard",font=("times new roman",22),cursor="hand2",text_color="black",command=lambda: self.change_button_state(self.dashboard_btn),
                                              hover_color="blue",fg_color="white",anchor="center",width=180,height=50,corner_radius=10)
        self.dashboard_btn.place(x=10,y=100)
#for Inventory
        self.Inventory_btn = customtkinter.CTkButton(left_frame, text="Inventory", font=("times new roman", 22),fg_color="white",text_color="black",
                                                cursor="hand2", hover_color="blue", anchor="center", width=180, height=50,
                                                corner_radius=10,command=lambda :self.change_button_state(self.Inventory_btn))
        self.Inventory_btn.place(x=10, y=155)
#for sales
        self.Sales_btn=customtkinter.CTkButton(left_frame,text="Sales",font=("times new roman",22),cursor="hand2",fg_color="white",text_color="black"
                                              ,hover_color="blue",anchor="center",width=180,height=50,corner_radius=10,command=lambda :self.change_button_state(self.Sales_btn))
        self.Sales_btn.place(x=10, y=210)

    def change_button_state(self, current_button):
        buttons = [self.dashboard_btn, self.Inventory_btn, self.Sales_btn]

        # Reset all buttons to their original state
        for button in buttons:
            button.configure(text_color="black", state="normal", corner_radius=10, fg_color="white")

        # Change the state of the clicked button
        current_button.configure(text_color="black", state="normal", corner_radius=10, fg_color="blue")


if __name__=="__main__":
    root=Tk()
    obj=Index(root)
    root.mainloop()

