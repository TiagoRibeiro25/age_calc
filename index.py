from tkinter import *
from tkinter import messagebox
from datetime import datetime
from time import strftime
import webbrowser
import os

#load settings
with open('settings.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        param = line.split(" - ")
        if param[0] == "theme":
            global theme
            theme = param[1]        #can only be dark or light
        if param[0] == "log":
            global save_log
            save_log = param[1]

if theme == "dark":
    window_background_color = "black"
    background_color = "LightSteelBlue4"
    box_color = "LightSteelBlue4"
    letter_color_box = "white"
    letter_color = "white"

if theme == "light":
    window_background_color = "snow2"
    background_color = "white"
    box_color = "black"
    letter_color_box = "white"
    letter_color = "black"

window = Tk()  
window.geometry('400x650')
window.resizable(0,0)
window.iconbitmap("calc.ico")
window.title('Program')
window.configure(background=window_background_color)

def main_calc():
    #top painel
    top_painel = PanedWindow(window, width = 380, height= 29, background=box_color)
    top_painel.place(x = 10, y = 10)


    #clock
    def clock():
        tack = strftime("%H:%M:%S")
        relogio_label.config(text= tack)
        relogio_label.after(500, clock)
    relogio_label = Label(top_painel,font=("calibri", 17), fg = letter_color_box,background = box_color)
    relogio_label.place(x=287, y=-3)
    clock() 

    def info():
        webbrowser.open_new_tab("https://github.com/TiagoRibeiro25/age_calc")

    def settings():
        main_painel.destroy()

        btn_settings.configure(state=DISABLED)
        btn_main.configure(state=NORMAL)
        btn_info.configure(state=NORMAL)

        global settings_painel
        settings_painel = PanedWindow(window, width = 380, height= 630, background=background_color)
        settings_painel.place(x = 10, y = 60)

        lbl_change_theme = Label(settings_painel, text = 'Change Theme', fg=letter_color, font = ('Arial', 15), background=background_color)
        lbl_change_theme.place(x = 15, y = 15)

        theme_selected = StringVar()
        Light = Radiobutton(settings_painel, text='Light', font = ('Arial', 13), background = background_color, variable= theme_selected, value='light')
        Dark = Radiobutton(settings_painel, text='Dark', font = ('Arial', 13), background = background_color, variable= theme_selected, value='dark')
        Light.place(x = 10, y = 50)
        Dark.place(x = 150, y = 50)
        theme_selected.set(theme)  
        #theme_selected.get() - get the value

        def apply_theme():
            global theme

            with open("settings.txt", "r", encoding="UTF-8") as f:
                newText=f.read().replace(theme, theme_selected.get())
            with open("settings.txt", "w", encoding="UTF-8") as f:
                f.write(newText)

            theme = theme_selected.get()
            window.destroy()
            os.system('index.py')

        btn_apply_theme = Button(settings_painel, text = 'Apply Theme', font = ('Arial', 10), fg = letter_color, relief='raised', background = background_color, command=apply_theme)
        btn_apply_theme.place(x = 10, y = 90)






    def calc():
        settings_painel.destroy()
        create_main_painel()

        btn_main.configure(state = DISABLED)
        btn_settings.configure(state=NORMAL)
        btn_info.configure(state=NORMAL)

        #current date
        current_time_label = Label(main_painel, text = 'Current Date', fg=letter_color, font = ('Arial', 15), background=background_color)
        current_time_label.place(x = 125, y = 15)
        current_time_entry = Entry(main_painel, width = 19, fg='white', font = ('Arial', 15),background="grey")
        current_time_entry.place(x = 80, y = 60)
        current_time_entry.insert('0', datetime.today().strftime('%d-%m-%Y'))
        current_time_entry.configure(state=DISABLED)
        
        #custom date
        custom_time_label = Label(main_painel, text = 'Custom Date', fg=letter_color, font = ('Arial', 15), background=background_color)
        custom_time_label.place(x = 120, y = 115)
        custom_time_entry = Entry(main_painel, width = 19, fg='white', font = ('Arial', 15),background="grey")
        custom_time_entry.insert("0", "xx-yy-zzzz")
        custom_time_entry.configure(state=DISABLED)
        custom_time_entry.place(x = 80, y = 160)

        def custom_date():
            custom_date_info = custom_confirmation.get()
            if custom_date_info == 1:
                custom_time_entry.configure(state=NORMAL)
            elif custom_date_info == 0:
                custom_time_entry.configure(state=DISABLED)

        custom_confirmation = IntVar(0)    
        btn_custom_time = Checkbutton(main_painel, text = "Use custom date", font = ('Arial', 7), fg=letter_color, background = background_color, variable= custom_confirmation, command=custom_date)
        btn_custom_time.place (x = 125,y = 190)

        #Day of birth input
        bday_date_label = Label(main_painel, text = 'Date of Birth', fg=letter_color, font = ('Arial', 15), background=background_color)
        bday_date_label.place(x = 120, y = 230)
        bday_date_entry = Entry(main_painel, width = 19, fg='white', font = ('Arial', 15),background="grey")
        bday_date_entry.place(x = 80, y = 270)


        #Calculate Age Button + function
        def calc_age_function():
            custom_date_info = custom_confirmation.get()            #0 -> Use current Date  1 -> Use custom Date
            #current date value = current_time_entry.get()
            #custom date value = custom_time_entry.get()
            #day of birth value = bday_date_entry.get()

            def verify_date():
                Loading_label.configure(text = "Status: Loading (0%)")
                verify_I = ["a","b","c","d","e","f","g","h","i"]
                verify_II = ["j","k","l","m","n","o","p","q","r"]
                verify_III = ["s","t","u","v","x","y","w","z","ç"]
                verify_IV = ["A","B","C","D","E","F","G","H","I"]
                verify_V = ["J","K","L","M","N","O","P","Q","R"]
                verify_VI = ["S","T","U","V","X","Y","W","Z","Ç"]
                verify = 1
                next = 1

                if next == 1:
                    for i in range(len(verify_I)-1):
                        if (custom_time_entry.get().find(verify_I[i]) != -1) or (bday_date_entry.get().find(verify_I[i]) != -1):
                            verify = 0
                            next = 0
                    Loading_label.configure(fg=letter_color, text = "Status: Loading (10%)")
                    print("Verify Status: 10%")
                if next == 1:
                    for i in range(len(verify_II)-1):
                        if (custom_time_entry.get().find(verify_II[i]) != -1) or (bday_date_entry.get().find(verify_II[i]) != -1):
                            verify = 0
                            next = 0
                    Loading_label.configure(fg=letter_color, text = "Status: Loading (30%)")
                    print("Verify Status: 30%")
                if next == 1:
                    for i in range(len(verify_III)-1):
                        if (custom_time_entry.get().find(verify_III[i]) != -1) or (bday_date_entry.get().find(verify_III[i]) != -1):
                            verify = 0
                            next = 0
                    Loading_label.configure(fg=letter_color, text = "Status: Loading (50%)")
                    print("Verify Status: 50%")
                if next == 1:
                    for i in range(len(verify_IV)-1):
                        if (custom_time_entry.get().find(verify_IV[i]) != -1) or (bday_date_entry.get().find(verify_IV[i]) != -1):
                            verify = 0
                            next = 0
                    Loading_label.configure(fg=letter_color, text = "Status: Loading (70%)")
                    print("Verify Status: 70%")
                if next == 1:
                    for i in range(len(verify_V)-1):
                        if (custom_time_entry.get().find(verify_V[i]) != -1) or (bday_date_entry.get().find(verify_V[i]) != -1):
                            verify = 0
                            next = 0
                    Loading_label.configure(fg=letter_color, text = "Status: Loading (90%)")
                    print("Verify Status: 90%")
                if next == 1:
                    for i in range(len(verify_VI)-1):
                        if (custom_time_entry.get().find(verify_VI[i]) != -1) or (bday_date_entry.get().find(verify_VI[i]) != -1):
                            verify = 0
                            next = 0
                    Loading_label.configure(fg=letter_color, text = "Status: Loading (99%)")
                    print("Verify Status: 99%")
                
                return verify

            #If the user wants to use a custom date
            if custom_date_info == 1:
                verification = verify_date()
                if verification == 1:
                    if (custom_time_entry.get().count("-") == 2 or custom_time_entry.get().count("_") == 2 or custom_time_entry.get().count(".") == 2 or custom_time_entry.get().count(",") == 2 or custom_time_entry.get().count(";") == 2 or custom_time_entry.get().count("/") == 2) and (bday_date_entry.get().count("-") == 2 or bday_date_entry.get().count("_") == 2 or bday_date_entry.get().count(".") == 2 or bday_date_entry.get().count(",") == 2 or bday_date_entry.get().count(";") == 2 or bday_date_entry.get().count("/") == 2):
                        Loading_label.configure(text="Status: Complete")
                        print("Verify Status: COMPLETE (100%)")

                        custom_date_value = custom_time_entry.get()
                        birth_date_value = bday_date_entry.get()

                        #caracter used by the user to separate the values (- _ . , ; /)
                        if custom_date_value.count("-") == 2:
                            split_value = "-"
                        elif custom_date_value.count("_") == 2:
                            split_value = "_"
                        elif custom_date_value.count(".") == 2:
                            split_value = "."
                        elif custom_date_value.count(",") == 2:
                            split_value = ","
                        elif custom_date_value.count(";") == 2:
                            split_value = ";"
                        elif custom_date_value.count("/") == 2:
                            split_value = "/"

                        if birth_date_value.count("-") == 2:
                            split_value_I = "-"
                        elif birth_date_value.count("_") == 2:
                            split_value_I = "_"
                        elif birth_date_value.count(".") == 2:
                            split_value_I = "."
                        elif birth_date_value.count(",") == 2:
                            split_value_I = ","
                        elif birth_date_value.count(";") == 2:
                            split_value_I = ";"
                        elif birth_date_value.count("/") == 2:
                            split_value_I = "/"

                        #make an array for custom date and another array for birthday date
                        custom_date_array = custom_date_value.split(split_value)
                        birth_date_array = birth_date_value.split(split_value_I)

                        #calculate age
                        result = int(custom_date_array[2]) - int(birth_date_array[2])
                        if int(birth_date_array[1]) > int(custom_date_array[1]):
                            result = result - 1
                        elif int(birth_date_array[1]) == int(custom_date_array[1]):
                            if int(birth_date_array[0]) > int(custom_date_array[0]):
                                result = result - 1

                        result_entry.configure(state=NORMAL)
                        result_entry.delete(0, END)
                        result_entry.insert('0', result)
                        result_entry.configure(state=DISABLED)

                        if save_log == "yes":
                            with open("log.txt", "r", encoding="UTF-8") as f:
                                cont_line=f.readlines()
                            #ID, Nome, Email, Senha, Tipo de user, Data de registo
                            save = '\n\n' + str(datetime.today().strftime('%d-%m-%Y')) + " at " + str(strftime("%H:%M:%S")) + "\nCustom Date: " + str(custom_date_value) + "\nDay of Birth: " + str(birth_date_value) + "\nAge: " + str(result)
                            with open("log.txt", "a", encoding="UTF-8") as f: 
                                f.write(save)  

                    else:
                        messagebox.showerror(title="Warning", message="Invalid Date value!\nPlease insert a valid date.")
                        Loading_label.configure(text = 'Status: Error')
                        print("Verify Status: Error")
                elif verification == 0:
                    messagebox.showerror(title="Warning", message="Invalid Date value!\nPlease insert a valid date.")
                    Loading_label.configure(text = 'Status: Error')
                    print("Verify Status: Error")
                
            
            #If the user wants to use the current date
            elif custom_date_info == 0:
                if bday_date_entry.get().count("-") == 2 or bday_date_entry.get().count("_") == 2 or bday_date_entry.get().count(".") == 2 or bday_date_entry.get().count(",") == 2 or bday_date_entry.get().count(";") == 2 or bday_date_entry.get().count("/") == 2:
                    Loading_label.configure(text = 'Status: Complete')
                    print("Verify Status: COMPLETE (100%)")

                    current_time_value = current_time_entry.get()
                    birth_date_value = bday_date_entry.get()

                    #caracter used by the user to separate the values (- _ . , ; /)
                    if birth_date_value.count("-") == 2:
                        split_value = "-"
                    elif birth_date_value.count("_") == 2:
                        split_value = "_"
                    elif birth_date_value.count(".") == 2:
                        split_value = "."
                    elif birth_date_value.count(",") == 2:
                        split_value = ","
                    elif birth_date_value.count(";") == 2:
                        split_value = ";"
                    elif birth_date_value.count("/") == 2:
                        split_value = "/"
                    #make an array for custom date and another array for birthday date
                    current_time_array = current_time_value.split("-")
                    birth_date_array = birth_date_value.split(split_value)

                    #calculate age
                    result = int(current_time_array[2]) - int(birth_date_array[2])
                    if int(birth_date_array[1]) > int(current_time_array[1]):
                        result = result - 1
                    elif int(birth_date_array[1]) == int(current_time_array[1]):
                        if int(birth_date_array[0]) > int(current_time_array[0]):
                            result = result - 1
                    
                    result_entry.configure(state=NORMAL)
                    result_entry.delete(0, END)
                    result_entry.insert('0', result)
                    result_entry.configure(state=DISABLED)

                    if save_log == "yes":
                        with open("log.txt", "r", encoding="UTF-8") as f:
                            cont_line=f.readlines()
                        #ID, Nome, Email, Senha, Tipo de user, Data de registo
                        save = '\n\n' + str(datetime.today().strftime('%d-%m-%Y')) + " at " + str(strftime("%H:%M:%S")) + "\nCustom Date: " + "\nDay of Birth: " + str(birth_date_value) + "\nAge: " + str(result)
                        with open("log.txt", "a", encoding="UTF-8") as f: 
                            f.write(save)  


                else:
                    messagebox.showerror(title="Warning", message="Invalid Date value!\nPlease insert a valid date.")
                    Loading_label.configure(text = 'Status: Error')
                    print("Verify Status: Error")



        calc_age = Button(main_painel, text = 'Calculate Age', font = ('Arial', 15), fg = letter_color_box, relief='raised', background = box_color, command=calc_age_function)
        calc_age.place(x = 115, y = 340)

        Loading_label = Label(main_painel, text = 'Status: Waiting', fg=letter_color, font = ('Arial', 15), background=background_color)
        Loading_label.place(x = 10, y = 420)

        result_label = Label(main_painel, text = 'Calculated Age', fg=letter_color, font = ('Arial', 15), background=background_color)
        result_label.place(x = 115, y = 465)
        result_entry = Entry(main_painel, width = 19, fg='white', font = ('Arial', 15),background="grey", state=DISABLED)
        result_entry.place(x = 80, y = 505)

        footer_label = Label(main_painel, text = 'App in development (Beta)                                  Open Source', fg=letter_color, font = ('Arial', 10), background=background_color)
        footer_label.place(x = 5, y = 555)


    #top buttons
    btn_main = Button(top_painel, text = 'H', font = ('Arial', 10), fg = letter_color_box, relief='flat', background = box_color, width=2, height=1, command=calc)
    btn_links = Button(top_painel, text = 'Web links', font = ('Arial', 10), fg = letter_color_box, relief='flat', background = box_color, width=8, height=1)
    btn_settings = Button(top_painel, text = 'Settings', font = ('Arial', 10), fg = letter_color_box, relief='flat', background = box_color, width=8, height=1, command=settings)
    btn_info = Button(top_painel, text = 'Information', font = ('Arial', 10), fg = letter_color_box, relief='flat', background = box_color, width=8, height=1, command=info)

    btn_main.place(x = 0, y = 0)
    btn_links.place(x = 20,y = 0)
    btn_settings.place(x = 110, y = 0)
    btn_info.place(x = 200, y = 0)

    #main painel
    def create_main_painel():
        global main_painel
        main_painel = PanedWindow(window, width = 380, height= 580, background=background_color)
        main_painel.place(x = 10, y = 60)

    create_main_painel()
    settings()
    calc()

main_calc()
window.mainloop()