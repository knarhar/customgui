from tkinter import *
import customtkinter

#-----------setting deafault theme as dark--------------------------------------------------------------------------------------
customtkinter.set_appearance_mode('dark')


#-------------------------------------------------------------------------------------------------------------------------------
def switch_event():
    print("switch toggled, current value:", switch_var.get())
    if switch_var.get()=='on':
        customtkinter.set_appearance_mode('dark')
    else:
        customtkinter.set_appearance_mode('light')

#-------------------------------------------------------------------------------------------------------------------------------
def sidebar_btn_event():
    print("sidebar_button click")

#-------------------------------------------------------------------------------------------------------------------------------
def open_input_dialog_event():
    dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
    print("CTkInputDialog:", dialog.get_input())


#--------------------creating window-----------------------------------------------------------------------------------------------------------------
window = customtkinter.CTk()
window.geometry('600x500')
window.title('Custom GUI by Knarik')

window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure((2,3), weight=0)
window.grid_rowconfigure((0,1,2), weight=1)

#---------creating sidebar frme with widgets--------------------------------------------------------------------------------------------------------- 
sidebar_frame = customtkinter.CTkFrame(master=window, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan= 4,sticky='nsew')
sidebar_frame.grid_rowconfigure(4, weight=1)
lbl_logo = customtkinter.CTkLabel(sidebar_frame, text='CustomTkinter', font=customtkinter.CTkFont(size=20, weight="bold"))
lbl_logo.grid(row=0, column=0, padx=20, pady=(20, 10))
btn_sidebar_1 = customtkinter.CTkButton(sidebar_frame, command=sidebar_btn_event)
btn_sidebar_1.grid(row=1, column=0, padx=20, pady=10)
btn_sidebar_2 = customtkinter.CTkButton(sidebar_frame, command=sidebar_btn_event)
btn_sidebar_2.grid(row=2, column=0, padx=20, pady=10)
btn_sidebar_3 = customtkinter.CTkButton(sidebar_frame, command=sidebar_btn_event)
btn_sidebar_3.grid(row=3, column=0, padx=20, pady=10)
switch_var = customtkinter.StringVar(value="on")
switch_mode = customtkinter.CTkSwitch(master=sidebar_frame, text="Dark mode", command=switch_event, variable=switch_var, onvalue="on", offvalue="off")
switch_mode.grid(row=6, column=0, padx=20, pady=10 )

#------------------creating entry and button --------------------------------------------------------------------------------------------------------
entry = customtkinter.CTkEntry(window, placeholder_text='Entry...')
entry.grid(row=3, column=1, columnspan=2, padx=(20,20),pady=(20,20), sticky ='nsew' )

btn_main = customtkinter.CTkButton(window, text='Submit', fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
btn_main.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

#-----------------creating textbox-------------------------------------------------------------------------------------------------------------------
textbox = customtkinter.CTkTextbox(window, width=200, font=('Ink Free', 15))
textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")


#----------------creating tabview--------------------------------------------------------------------------------------------------------------------
tabview = customtkinter.CTkTabview(window, width=250)
tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
tabview.add("Tabview")
tabview.add("Tab 2")
tabview.add("Tab 3")
tabview.tab("Tabview").grid_columnconfigure(0, weight=1)
tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
optionmenu_1 = customtkinter.CTkOptionMenu(tabview.tab("Tabview"), dynamic_resizing=False,values=["Value 1", "Value 2", "Value Long Long Long"])
optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
combobox_1 = customtkinter.CTkComboBox(tabview.tab("Tabview"),values=["Value 1", "Value 2", "Value Long....."])
combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
string_input_button = customtkinter.CTkButton(tabview.tab("Tabview"), text="Open InputDialog",command=open_input_dialog_event)
string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
label_tab_2 = customtkinter.CTkLabel(tabview.tab("Tab 2"), text="Label on Tab 2")
label_tab_2.grid(row=0, column=0, padx=20, pady=20)

#------------------creating radiobutton--------------------------------------------------------------------------------------------------------------------------------------
radiobutton_frame = customtkinter.CTkFrame(window)
radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
radio_var = IntVar(value=0)
label_radio_group = customtkinter.CTkLabel(master=radiobutton_frame, text="CTkRadioButton Group:")
label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
radio_button_1 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value=0)
radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
radio_button_2 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value=1)
radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
radio_button_3 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value=2)
radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")


#---------------creating slider and progressbar-----------------------------

slider_progressbar_frame = customtkinter.CTkFrame(window, fg_color='transparent')
slider_progressbar_frame.grid(row=1, column=1, padx=(20,0), pady=(20,0), sticky='nsew')
slider_progressbar_frame.grid_columnconfigure(0, weight=1)
slider_progressbar_frame.grid_rowconfigure(4, weight=1)
seg_button_1 = customtkinter.CTkSegmentedButton(slider_progressbar_frame)
seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
progressbar_1 = customtkinter.CTkProgressBar(slider_progressbar_frame)
progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")


























window.mainloop()