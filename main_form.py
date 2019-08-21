try:
    import tkinter as tk
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.ttk as ttk

import database as db
import scoreboard as sb
# import database as db

class MainWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button1 = tk.Button(self, text="Add Competitor", width=40, command=self.add_competitor)           
        self.button1.place(x=20,y=20)

        self.button2 = tk.Button(self, text="Modify Competitor", width=40, command=self.mod_competitor)                      
        self.button2.place(x=20,y=50)

        self.button3 = tk.Button(self, text="Event Management", width=40, command=self.event_management)
        self.button3.place(x=20,y=80)

        self.button4 = tk.Button(self, text="Scoreboard", width=40, command=self.show_scoreboard)
        self.button4.place(x=20,y=110) 

        self.button5 = tk.Button(self, text="Competitor Attendance Check", width=40, command=self.mark_attendance)
        self.button5.place(x=20,y=140)

    def add_competitor(self):
        print("===> Creating New Competitor")
        t1 = tk.Toplevel(self)
        t1.wm_title("Registration Form")
        t1.geometry('1040x700')
        base = 80

        def on_submit():
            # competitor information
            fn = first_name_entry.get()
            ln = last_name_entry.get()
            club = club_name_entry.get()
            dob = dob_entry.get()               # place check when possible
            age = age_entry.get()               # place check when possible
            weight = weight_entry.get()         # place check when possible
            gen = gen_var.get()

            # contact details
            add = address_entry.get()
            sub = suburb_entry.get()
            pc = post_code_entry.get()
            cn = contact_number_entry.get()
            em = email_entry.get()

            # martial arts level
            malvl = exp_sv.get()
            belt = belt_entry.get()

            # event selection
            ev_k = k_sv.get()
            ev_ds = ds_sv.get()
            ev_ps = ps_sv.get()
            ev_cs = cs_sv.get()
            ev_w = w_sv.get()
            ev_ksc = ksc_sv.get()
            ev_kf = kf_sv.get()
            ev_kb = kb_sv.get()
            ev_s = s_sv.get()
            ev_a = a_sv.get()
            ev_sd = sd_sv.get()
            ev_sf = sf_sv.get()

            # print(gen)
            db.add_competitor(fn, ln, club, dob, age, weight, gen, add, sub, pc, cn, em, malvl, belt,
                                ev_k, ev_ds, ev_ps, ev_cs, ev_w, ev_ksc, ev_kf, ev_kb, ev_s, ev_a, ev_sd, ev_sf)
            t1.destroy()

        def on_close():
            t1.destroy()  

        # Main title
        title1 = tk.Label(t1, text="Registration",font=("bold", 20), fg="blue")
        title1.place(x=20,y=base-70)

        # competitor information
        title1 = tk.Label(t1, text="Competitor Information",font=("bold", 15))
        title1.place(x=20,y=base-30)

        # competitor first name
        first_name_label = tk.Label(t1, text="First Name",font=("bold", 10))
        first_name_label.place(x=20,y=base+10)
        first_name_entry = tk.Entry(t1, width=35)
        first_name_entry.place(x=200,y=base+10)

        # competitor last name
        last_name_label = tk.Label(t1, text="Last Name",font=("bold", 10))
        last_name_label.place(x=20,y=base+40)
        last_name_entry = tk.Entry(t1, width=35)
        last_name_entry.place(x=200,y=base+40)

        # competitor club name
        club_name_label = tk.Label(t1, text="Club Name",font=("bold", 10))
        club_name_label.place(x=20,y=base+70)
        club_name_entry = tk.Entry(t1, width=35)
        club_name_entry.place(x=200,y=base+70)

        # competitor date of birth
        dob_label = tk.Label(t1, text="Date of Birth (dd/mm/yyyy)",font=("bold", 10))
        dob_label.place(x=20,y=base+100)
        dob_entry = tk.Entry(t1, width=35)
        dob_entry.place(x=200,y=base+100)

        # competitor age
        age_label = tk.Label(t1, text="Age",font=("bold", 10))
        age_label.place(x=20,y=base+130)
        age_entry = tk.Entry(t1, width=35)
        age_entry.place(x=200,y=base+130)

        # competitor weight
        weight_label = tk.Label(t1, text="Weight (kg)",font=("bold", 10))
        weight_label.place(x=20,y=base+160)
        weight_entry = tk.Entry(t1, width=35)
        weight_entry.place(x=200,y=base+160)

        # competitor gender
        gender_label = tk.Label(t1, text="Gender",font=("bold", 10))
        gender_label.place(x=20,y=base+190)
        gen_var = tk.IntVar()
        tk.Radiobutton(t1, text="Male",padx = 5, variable=gen_var, value=1).place(x=200,y=base+190)
        tk.Radiobutton(t1, text="Female",padx = 20, variable=gen_var, value=2).place(x=255,y=base+190)

        # ------------------------------------------------------------------------------------------------
        # contact details
        title2 = tk.Label(t1, text="Contact Details",font=("bold", 15))
        title2.place(x=20,y=base+230)

        # competitor address
        address_label = tk.Label(t1, text="Address",font=("bold", 10))
        address_label.place(x=20,y=base+270)
        address_entry = tk.Entry(t1, width=35)
        address_entry.place(x=200,y=base+270)

        # competitor suburb
        suburb_label = tk.Label(t1, text="Suburb",font=("bold", 10))
        suburb_label.place(x=20,y=base+300)
        suburb_entry = tk.Entry(t1, width=35)
        suburb_entry.place(x=200,y=base+300)

        # competitor post code
        post_code_label = tk.Label(t1, text="Post Code",font=("bold", 10))
        post_code_label.place(x=20,y=base+330)
        post_code_entry = tk.Entry(t1, width=35)
        post_code_entry.place(x=200,y=base+330)

        # competitor phone 
        contact_number_label = tk.Label(t1, text="Contact Number",font=("bold", 10))
        contact_number_label.place(x=20,y=base+360)
        contact_number_entry = tk.Entry(t1, width=35)
        contact_number_entry.place(x=200,y=base+360)

        # competitor email
        email_label = tk.Label(t1, text="Email",font=("bold", 10))
        email_label.place(x=20,y=base+390)
        email_entry = tk.Entry(t1, width=35)
        email_entry.place(x=200,y=base+390)

        # ------------------------------------------------------------------------------------------------
        # Level of martial arts experience
        title3 = tk.Label(t1, text="Level of Martial Arts Experience",font=("bold", 15))
        title3.place(x=20,y=base+430)

        exp_label = tk.Label(t1, text="Martial Arts experience",font=("bold", 10))
        exp_label.place(x=20,y=base+470)
        exp_sv = tk.StringVar()
        exp_droplist = tk.OptionMenu(t1, exp_sv, *db.exp_list)
        exp_droplist.config(width=30)
        exp_sv.set('Select level') 
        exp_droplist.place(x=200-5,y=base+470-5)

        # belt
        belt_label = tk.Label(t1, text="Belt",font=("bold", 10))
        belt_label.place(x=20,y=base+500)
        belt_entry = tk.Entry(t1, width=35)
        belt_entry.place(x=200,y=base+500)

        # ------------------------------------------------------------------------------------------------
        # Event Selection
        title4 = tk.Label(t1, text="Event Selection",font=("bold", 15))
        title4.place(x=500,y=base-30)

        # Kata, Forms, Patterns (K)
        k_label = tk.Label(t1, text="Kata, Forms, Patterns",font=("bold", 10))
        k_label.place(x=500,y=base+10)
        k_label = tk.Label(t1, text="K",font=("bold", 10))
        k_label.place(x=700,y=base+10)
        k_sv = tk.StringVar()
        k_droplist = tk.OptionMenu(t1, k_sv, *db.k_list)
        k_droplist.config(width=35)
        k_sv.set('Select Division') 
        k_droplist.place(x=760,y=base+10-5)

        # Demo/Showmanship (DS)
        ds_label = tk.Label(t1, text="Demo/Showmanship",font=("bold", 10))
        ds_label.place(x=500,y=base+40)
        ds_label = tk.Label(t1, text="DS",font=("bold", 10))
        ds_label.place(x=700,y=base+40)
        ds_sv = tk.StringVar()
        ds_droplist = tk.OptionMenu(t1, ds_sv, *db.ds_list)
        ds_droplist.config(width=35)
        ds_sv.set('Select Division') 
        ds_droplist.place(x=760,y=base+40-5)

        # Point Sparring (PS)
        ps_label = tk.Label(t1, text="Point Sparring",font=("bold", 10))
        ps_label.place(x=500,y=base+70)
        ps_label = tk.Label(t1, text="PS",font=("bold", 10))
        ps_label.place(x=700,y=base+70)
        ps_sv = tk.StringVar()
        ps_droplist = tk.OptionMenu(t1, ps_sv, *db.ps_list)
        ps_droplist.config(width=35)
        ps_sv.set('Select Division') 
        ps_droplist.place(x=760,y=base+70-5)

        # Continuous Sparring (CS)
        cs_label = tk.Label(t1, text="Continuous Sparring",font=("bold", 10))
        cs_label.place(x=500,y=base+100)
        cs_label = tk.Label(t1, text="CS",font=("bold", 10))
        cs_label.place(x=700,y=base+100)
        cs_sv = tk.StringVar()
        cs_droplist = tk.OptionMenu(t1, cs_sv, *db.cs_list)
        cs_droplist.config(width=35)
        cs_sv.set('Select Division') 
        cs_droplist.place(x=760,y=base+100-5)

        # Traditional Weapons (W)
        w_label = tk.Label(t1, text="Traditional Weapons",font=("bold", 10))
        w_label.place(x=500,y=base+130)
        w_label = tk.Label(t1, text="W",font=("bold", 10))
        w_label.place(x=700,y=base+130)
        w_sv = tk.StringVar()
        w_droplist = tk.OptionMenu(t1, w_sv, *db.w_list)
        w_droplist.config(width=35)
        w_sv.set('Select Division') 
        w_droplist.place(x=760,y=base+130-5)

        # Kyokushin Sparring Contact (KSC)
        ksc_label = tk.Label(t1, text="Kyokushin Sparring Contact",font=("bold", 10))
        ksc_label.place(x=500,y=base+160)
        ksc_label = tk.Label(t1, text="KSC",font=("bold", 10))
        ksc_label.place(x=700,y=base+160)
        ksc_sv = tk.StringVar()
        ksc_droplist = tk.OptionMenu(t1, ksc_sv, *db.ksc_list)
        ksc_droplist.config(width=35)
        ksc_sv.set('Select Division') 
        ksc_droplist.place(x=760,y=base+160-5)

        # Kyokushin Kata/Forms (KF)
        kf_label = tk.Label(t1, text="Kyokushin Kata/Forms",font=("bold", 10))
        kf_label.place(x=500,y=base+190)
        kf_label = tk.Label(t1, text="KF",font=("bold", 10))
        kf_label.place(x=700,y=base+190)
        kf_sv = tk.StringVar()
        kf_droplist = tk.OptionMenu(t1, kf_sv, *db.kf_list)
        kf_droplist.config(width=35)
        kf_sv.set('Select Division') 
        kf_droplist.place(x=760,y=base+190-5)

        # ------------------------------------------------------------------------------------------------
        # Kata - Beginners (KB)
        kb_label = tk.Label(t1, text="Kata - Beginners",font=("bold", 10))
        kb_label.place(x=500,y=base+250)
        kb_label = tk.Label(t1, text="KB",font=("bold", 10))
        kb_label.place(x=700,y=base+250)
        kb_sv = tk.StringVar()
        kb_droplist = tk.OptionMenu(t1, kb_sv, *db.kb_list)
        kb_droplist.config(width=35)
        kb_sv.set('Select Division') 
        kb_droplist.place(x=760,y=base+250-5)

        # Sumo (S)
        s_label = tk.Label(t1, text="Sumo",font=("bold", 10))
        s_label.place(x=500,y=base+280)
        s_label = tk.Label(t1, text="S",font=("bold", 10))
        s_label.place(x=700,y=base+280)
        s_sv = tk.StringVar()
        s_droplist = tk.OptionMenu(t1, s_sv, *db.s_list)
        s_droplist.config(width=35)
        s_sv.set('Select Division') 
        s_droplist.place(x=760,y=base+280-5)

        # Fastest Kick (A)
        a_label = tk.Label(t1, text="Fastest Kick",font=("bold", 10))
        a_label.place(x=500,y=base+310)
        a_label = tk.Label(t1, text="A",font=("bold", 10))
        a_label.place(x=700,y=base+310)
        a_sv = tk.StringVar()
        a_droplist = tk.OptionMenu(t1, a_sv, *db.a_list)
        a_droplist.config(width=35)
        a_sv.set('Select Division') 
        a_droplist.place(x=760,y=base+310-5)

        # Self Defence (SD)
        sd_label = tk.Label(t1, text="Self Defence",font=("bold", 10))
        sd_label.place(x=500,y=base+340)
        sd_label = tk.Label(t1, text="SD",font=("bold", 10))
        sd_label.place(x=700,y=base+340)
        sd_sv = tk.StringVar()
        sd_droplist = tk.OptionMenu(t1, sd_sv, *db.sd_list)
        sd_droplist.config(width=35)
        sd_sv.set('Select Division') 
        sd_droplist.place(x=760,y=base+340-5)

        # Sword Fighting (SF)
        sf_label = tk.Label(t1, text="Sword Fighting",font=("bold", 10))
        sf_label.place(x=500,y=base+370)
        sf_label = tk.Label(t1, text="SF",font=("bold", 10))
        sf_label.place(x=700,y=base+370)
        sf_sv = tk.StringVar()
        sf_droplist = tk.OptionMenu(t1, sf_sv, *db.sf_list)
        sf_droplist.config(width=35)
        sf_sv.set('Select Division') 
        sf_droplist.place(x=760,y=base+370-5)

        # Submit and Close buttons
        tk.Button(t1, text='Submit',width=20,bg='brown',fg='white', command=on_submit).place(x=860,y=660)
        tk.Button(t1, text='Close',width=20,bg='brown',fg='white', command=on_close).place(x=700,y=660)

    def mod_competitor(self):
        t2 = tk.Toplevel(self)
        t2.wm_title("Modify Competitor")
        t2.geometry('1040x800')
        base = 130 

        def null_fix(input):
            if (type(input) == int) == False: return None
            else: return input

        def on_submit():
            # competitor information
            lup_name = lookup_sv.get()
            fn = first_name_entry.get()
            ln = last_name_entry.get()
            club = club_name_entry.get()
            dob = dob_entry.get()               # place check when possible
            age = age_entry.get()               # place check when possible
            weight = weight_entry.get()         # place check when possible
            gen = null_fix(gen_var.get())

            # contact details
            add = address_entry.get()
            sub = suburb_entry.get()
            pc = post_code_entry.get()
            cn = contact_number_entry.get()
            em = email_entry.get()

            # martial arts level
            malvl = exp_sv.get()
            belt = belt_entry.get()

            # event selection
            ev_k = k_sv.get()
            ev_ds = ds_sv.get()
            ev_ps = ps_sv.get()
            ev_cs = cs_sv.get()
            ev_w = w_sv.get()
            ev_ksc = ksc_sv.get()
            ev_kf = kf_sv.get()
            ev_kb = kb_sv.get()
            ev_s = s_sv.get()
            ev_a = a_sv.get()
            ev_sd = sd_sv.get()
            ev_sf = sf_sv.get()

            if lookup_sv.get() != "Select Competitor":
                db.mod_competitor(lup_name, fn, ln, club, dob, age, weight, gen, add, sub, pc, cn, em, malvl, belt,
                                ev_k, ev_ds, ev_ps, ev_cs, ev_w, ev_ksc, ev_kf, ev_kb, ev_s, ev_a, ev_sd, ev_sf)
                t2.destroy()
            else:
                print("===> Submission Rejected, Please Select Competitor")
        
        def on_close():
            t2.destroy()

        def null_check(input):
            if input == None: return ""
            else: return input

        def gender_check(input):
            if input == 'male': return 1
            elif input == 'female': return 2
            else: return None 

        def event_check(input):
            if input == None: return "Select Division"
            else: return input 

        def clear_form():
            first_name_entry.delete(0, 'end')
            last_name_entry.delete(0, 'end')
            club_name_entry.delete(0, 'end')
            dob_entry.delete(0, 'end')
            age_entry.delete(0, 'end')
            weight_entry.delete(0, 'end')
            gen_var.set(None)

            address_entry.delete(0, 'end')
            suburb_entry.delete(0, 'end')
            post_code_entry.delete(0, 'end')
            contact_number_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
        
            exp_sv.set('Select level') 
            belt_entry.delete(0, 'end')

            k_sv.set('Select Division')
            ds_sv.set('Select Division')
            ps_sv.set('Select Division')
            cs_sv.set('Select Division')
            w_sv.set('Select Division')
            ksc_sv.set('Select Division')
            kf_sv.set('Select Division')

            kb_sv.set('Select Division')
            s_sv.set('Select Division')
            a_sv.set('Select Division')
            sd_sv.set('Select Division')
            sf_sv.set('Select Division')

        def show_details(value):
            selected_name = lookup_sv.get()
            print(f"===> Retreiving details for {selected_name}")
            selected_list = db.get_selected_details(selected_name)
            clear_form()

            first_name_entry.insert(0, null_check(selected_list[0]))
            last_name_entry.insert(0, null_check(selected_list[1]))
            club_name_entry.insert(0, null_check(selected_list[3]))
            dob_entry.insert(0, null_check(selected_list[4]))
            age_entry.insert(0, null_check(selected_list[5]))
            weight_entry.insert(0, null_check(selected_list[6]))
            gen_var.set(gender_check(selected_list[7]))       

            address_entry.insert(0, null_check(selected_list[8]))
            suburb_entry.insert(0, null_check(selected_list[9]))
            post_code_entry.insert(0, null_check(selected_list[10]))
            contact_number_entry.insert(0, null_check(selected_list[12]))
            email_entry.insert(0, null_check(selected_list[13]))

            exp_sv.set(selected_list[16]) 
            belt_entry.insert(0, null_check(selected_list[14]))

            ev_list = []
            ev_list.append(selected_list[17])

            k_sv.set(event_check(ev_list[0][0]))
            ds_sv.set(event_check(ev_list[0][1]))
            ps_sv.set(event_check(ev_list[0][2]))
            cs_sv.set(event_check(ev_list[0][3]))
            w_sv.set(event_check(ev_list[0][4]))
            ksc_sv.set(event_check(ev_list[0][5]))
            kf_sv.set(event_check(ev_list[0][6]))

            kb_sv.set(event_check(ev_list[0][7]))
            s_sv.set(event_check(ev_list[0][8]))
            a_sv.set(event_check(ev_list[0][9]))
            sd_sv.set(event_check(ev_list[0][10]))
            sf_sv.set(event_check(ev_list[0][11]))

        # Main title
        title_mod = tk.Label(t2, text="Modification",font=("bold", 20), fg="blue")
        title_mod.place(x=20,y=base-120)
        
        # look up
        look_up_label = tk.Label(t2, text="Please select competitor before proceeding: ",font=("bold", 12))
        look_up_label.place(x=20,y=base-70)

        lookup_list = db.get_list_of_competitors()
        lookup_sv = tk.StringVar()
        lookup_droplist = tk.OptionMenu(t2, lookup_sv, *lookup_list, command=show_details)
        lookup_droplist.config(width=50)
        lookup_sv.set('Select Competitor') 
        lookup_droplist.place(x=350,y=base-75)

        # competitor information
        title1 = tk.Label(t2, text="Competitor Information",font=("bold", 15))
        title1.place(x=20,y=base-30)

        # competitor first name
        first_name_label = tk.Label(t2, text="First Name",font=("bold", 10))
        first_name_label.place(x=20,y=base+20)
        first_name_entry = tk.Entry(t2, width=35)
        first_name_entry.place(x=200,y=base+20)

        # competitor last name
        last_name_label = tk.Label(t2, text="Last Name",font=("bold", 10))
        last_name_label.place(x=20,y=base+50)
        last_name_entry = tk.Entry(t2, width=35)
        last_name_entry.place(x=200,y=base+50)

        # competitor club name
        club_name_label = tk.Label(t2, text="Club Name",font=("bold", 10))
        club_name_label.place(x=20,y=base+80)
        club_name_entry = tk.Entry(t2, width=35)
        club_name_entry.place(x=200,y=base+80)

        # competitor date of birth
        dob_label = tk.Label(t2, text="Date of Birth (dd/mm/yyyy)",font=("bold", 10))
        dob_label.place(x=20,y=base+110)
        dob_entry = tk.Entry(t2, width=35)
        dob_entry.place(x=200,y=base+110)

        # competitor age
        age_label = tk.Label(t2, text="Age",font=("bold", 10))
        age_label.place(x=20,y=base+140)
        age_entry = tk.Entry(t2, width=35)
        age_entry.place(x=200,y=base+140)

        # competitor weight
        weight_label = tk.Label(t2, text="Weight (kg)",font=("bold", 10))
        weight_label.place(x=20,y=base+170)
        weight_entry = tk.Entry(t2, width=35)
        weight_entry.place(x=200,y=base+170)

        # competitor gender
        gender_label = tk.Label(t2, text="Gender",font=("bold", 10))
        gender_label.place(x=20,y=base+200)
        gen_var = tk.IntVar()
        tk.Radiobutton(t2, text="Male",padx = 5, variable=gen_var, value=1).place(x=200,y=base+200)
        tk.Radiobutton(t2, text="Female",padx = 20, variable=gen_var, value=2).place(x=255,y=base+200)

        # ------------------------------------------------------------------------------------------------
        # contact details
        title2 = tk.Label(t2, text="Contact Details",font=("bold", 15))
        title2.place(x=20,y=base+260)

        # competitor address
        address_label = tk.Label(t2, text="Address",font=("bold", 10))
        address_label.place(x=20,y=base+310)
        address_entry = tk.Entry(t2, width=35)
        address_entry.place(x=200,y=base+310)

        # competitor suburb
        suburb_label = tk.Label(t2, text="Suburb",font=("bold", 10))
        suburb_label.place(x=20,y=base+340)
        suburb_entry = tk.Entry(t2, width=35)
        suburb_entry.place(x=200,y=base+340)

        # competitor post code
        post_code_label = tk.Label(t2, text="Post Code",font=("bold", 10))
        post_code_label.place(x=20,y=base+370)
        post_code_entry = tk.Entry(t2, width=35)
        post_code_entry.place(x=200,y=base+370)

        # competitor phone 
        contact_number_label = tk.Label(t2, text="Contact Number",font=("bold", 10))
        contact_number_label.place(x=20,y=base+400)
        contact_number_entry = tk.Entry(t2, width=35)
        contact_number_entry.place(x=200,y=base+400)

        # competitor email
        email_label = tk.Label(t2, text="Email",font=("bold", 10))
        email_label.place(x=20,y=base+430)
        email_entry = tk.Entry(t2, width=35)
        email_entry.place(x=200,y=base+430)

        # ------------------------------------------------------------------------------------------------
        # Level of martial arts experience
        title3 = tk.Label(t2, text="Level of Martial Arts Experience",font=("bold", 15))
        title3.place(x=20,y=base+490)

        exp_label = tk.Label(t2, text="Martial Arts experience",font=("bold", 10))
        exp_label.place(x=20,y=base+530)
        exp_sv = tk.StringVar()
        exp_droplist = tk.OptionMenu(t2, exp_sv, *db.exp_list)
        exp_droplist.config(width=30)
        exp_sv.set('Select level') 
        exp_droplist.place(x=200-5,y=base+530-5)

        # belt
        belt_label = tk.Label(t2, text="Belt",font=("bold", 10))
        belt_label.place(x=20,y=base+575)
        belt_entry = tk.Entry(t2, width=35)
        belt_entry.place(x=200,y=base+575)

        # ------------------------------------------------------------------------------------------------
        # Event Selection
        title4 = tk.Label(t2, text="Event Selection",font=("bold", 15))
        title4.place(x=500,y=base-30)

        # Kata, Forms, Patterns (K)
        k_label = tk.Label(t2, text="Kata, Forms, Patterns",font=("bold", 10))
        k_label.place(x=500,y=base+20)
        k_label = tk.Label(t2, text="K",font=("bold", 10))
        k_label.place(x=700,y=base+20)
        k_sv = tk.StringVar()
        k_droplist = tk.OptionMenu(t2, k_sv, *db.k_list)
        k_droplist.config(width=35)
        k_sv.set('Select Division') 
        k_droplist.place(x=760,y=base+20-5)

        # Demo/Showmanship (DS)
        ds_label = tk.Label(t2, text="Demo/Showmanship",font=("bold", 10))
        ds_label.place(x=500,y=base+50)
        ds_label = tk.Label(t2, text="DS",font=("bold", 10))
        ds_label.place(x=700,y=base+50)
        ds_sv = tk.StringVar()
        ds_droplist = tk.OptionMenu(t2, ds_sv, *db.ds_list)
        ds_droplist.config(width=35)
        ds_sv.set('Select Division') 
        ds_droplist.place(x=760,y=base+50-5)

        # Point Sparring (PS)
        ps_label = tk.Label(t2, text="Point Sparring",font=("bold", 10))
        ps_label.place(x=500,y=base+80)
        ps_label = tk.Label(t2, text="PS",font=("bold", 10))
        ps_label.place(x=700,y=base+80)
        ps_sv = tk.StringVar()
        ps_droplist = tk.OptionMenu(t2, ps_sv, *db.ps_list)
        ps_droplist.config(width=35)
        ps_sv.set('Select Division') 
        ps_droplist.place(x=760,y=base+75)

        # Continuous Sparring (CS)
        cs_label = tk.Label(t2, text="Continuous Sparring",font=("bold", 10))
        cs_label.place(x=500,y=base+110)
        cs_label = tk.Label(t2, text="CS",font=("bold", 10))
        cs_label.place(x=700,y=base+110)
        cs_sv = tk.StringVar()
        cs_droplist = tk.OptionMenu(t2, cs_sv, *db.cs_list)
        cs_droplist.config(width=35)
        cs_sv.set('Select Division') 
        cs_droplist.place(x=760,y=base+110-5)

        # Traditional Weapons (W)
        w_label = tk.Label(t2, text="Traditional Weapons",font=("bold", 10))
        w_label.place(x=500,y=base+140)
        w_label = tk.Label(t2, text="W",font=("bold", 10))
        w_label.place(x=700,y=base+140)
        w_sv = tk.StringVar()
        w_droplist = tk.OptionMenu(t2, w_sv, *db.w_list)
        w_droplist.config(width=35)
        w_sv.set('Select Division') 
        w_droplist.place(x=760,y=base+140-5)

        # Kyokushin Sparring Contact (KSC)
        ksc_label = tk.Label(t2, text="Kyokushin Sparring Contact",font=("bold", 10))
        ksc_label.place(x=500,y=base+170)
        ksc_label = tk.Label(t2, text="KSC",font=("bold", 10))
        ksc_label.place(x=700,y=base+170)
        ksc_sv = tk.StringVar()
        ksc_droplist = tk.OptionMenu(t2, ksc_sv, *db.ksc_list)
        ksc_droplist.config(width=35)
        ksc_sv.set('Select Division') 
        ksc_droplist.place(x=760,y=base+170-5)

        # Kyokushin Kata/Forms (KF)
        kf_label = tk.Label(t2, text="Kyokushin Kata/Forms",font=("bold", 10))
        kf_label.place(x=500,y=base+200)
        kf_label = tk.Label(t2, text="KF",font=("bold", 10))
        kf_label.place(x=700,y=base+200)
        kf_sv = tk.StringVar()
        kf_droplist = tk.OptionMenu(t2, kf_sv, *db.kf_list)
        kf_droplist.config(width=35)
        kf_sv.set('Select Division') 
        kf_droplist.place(x=760,y=base+200-5)

        # ------------------------------------------------------------------------------------------------
        # Kata - Beginners (KB)
        kb_label = tk.Label(t2, text="Kata - Beginners",font=("bold", 10))
        kb_label.place(x=500,y=base+250)
        kb_label = tk.Label(t2, text="KB",font=("bold", 10))
        kb_label.place(x=700,y=base+250)
        kb_sv = tk.StringVar()
        kb_droplist = tk.OptionMenu(t2, kb_sv, *db.kb_list)
        kb_droplist.config(width=35)
        kb_sv.set('Select Division') 
        kb_droplist.place(x=760,y=base+250-5)

        # Sumo (S)
        s_label = tk.Label(t2, text="Sumo",font=("bold", 10))
        s_label.place(x=500,y=base+280)
        s_label = tk.Label(t2, text="S",font=("bold", 10))
        s_label.place(x=700,y=base+280)
        s_sv = tk.StringVar()
        s_droplist = tk.OptionMenu(t2, s_sv, *db.s_list)
        s_droplist.config(width=35)
        s_sv.set('Select Division') 
        s_droplist.place(x=760,y=base+280-5)

        # Fastest Kick (A)
        a_label = tk.Label(t2, text="Fastest Kick",font=("bold", 10))
        a_label.place(x=500,y=base+310)
        a_label = tk.Label(t2, text="A",font=("bold", 10))
        a_label.place(x=700,y=base+310)
        a_sv = tk.StringVar()
        a_droplist = tk.OptionMenu(t2, a_sv, *db.a_list)
        a_droplist.config(width=35)
        a_sv.set('Select Division') 
        a_droplist.place(x=760,y=base+310-5)

        # Self Defence (SD)
        sd_label = tk.Label(t2, text="Self Defence",font=("bold", 10))
        sd_label.place(x=500,y=base+340)
        sd_label = tk.Label(t2, text="SD",font=("bold", 10))
        sd_label.place(x=700,y=base+340)
        sd_sv = tk.StringVar()
        sd_droplist = tk.OptionMenu(t2, sd_sv, *db.sd_list)
        sd_droplist.config(width=35)
        sd_sv.set('Select Division') 
        sd_droplist.place(x=760,y=base+340-5)

        # Sword Fighting (SF)
        sf_label = tk.Label(t2, text="Sword Fighting",font=("bold", 10))
        sf_label.place(x=500,y=base+370)
        sf_label = tk.Label(t2, text="SF",font=("bold", 10))
        sf_label.place(x=700,y=base+370)
        sf_sv = tk.StringVar()
        sf_droplist = tk.OptionMenu(t2, sf_sv, *db.sf_list)
        sf_droplist.config(width=35)
        sf_sv.set('Select Division') 
        sf_droplist.place(x=760,y=base+370-5)

        # Submit and Close buttons
        tk.Button(t2, text='Submit',width=20,bg='brown',fg='white', command=on_submit).place(x=850,y=600)
        tk.Button(t2, text='Close',width=20,bg='brown',fg='white', command=on_close).place(x=690,y=600)

    def event_management(self):
        t3 = tk.Toplevel(self)
        t3.wm_title("Event Management")
        t3.geometry('950x675')

        title_mod = tk.Label(t3, text="Event Management",font=("bold", 20), fg="blue")
        title_mod.place(x=20,y=10)

        firstplace_label = tk.Label(t3, text="1st Place: ",font=("bold", 10))
        firstplace_label.place(x=610,y=210)
        secondplace_label = tk.Label(t3, text="2nd Place: ",font=("bold", 10))
        secondplace_label.place(x=610,y=240)
        thirdplace_label = tk.Label(t3, text="3rd Place: ",font=("bold", 10))
        thirdplace_label.place(x=610,y=270)

        def event_droplist(value):
            selection = eve_sv.get()
            selection_event = selection.split('(')[-1].split(')')[0]
            division_list = db.get_division(selection_event)

            div_sv.set('')
            div_droplist.children['menu'].delete(0, 'end')
            for option in division_list:
                div_droplist['menu'].add_command(label=option, command=lambda value=option: div_sv.set(value))

        div_list = ['Null']
        div_sv = tk.StringVar()
        div_droplist = tk.OptionMenu(t3, div_sv, *div_list)
        div_droplist.config(width=30)
        div_sv.set('Select Division') 
        div_droplist.place(x=280,y=60)
        
        eve_sv = tk.StringVar()
        eve_droplist = tk.OptionMenu(t3, eve_sv, *db.event_list, command=event_droplist)
        eve_droplist.config(width=30)
        eve_sv.set('Select Event') 
        eve_droplist.place(x=30,y=60)

        event_tree = ttk.Treeview(t3, columns=('one','two'), height=25)
        event_tree.heading('#0', text='Competitor')
        event_tree.heading('#1', text='Placement')
        event_tree.heading('#2', text='Score')
        event_tree.column('#0', width=350, stretch=False, minwidth=350)
        event_tree.column('#1', width=100, stretch=False, minwidth=100)
        event_tree.column('#2', width=100, stretch=False, minwidth=100)
        event_tree.place(x=30,y=110)

        def get_competitors():
            if eve_sv.get() and div_sv.get():
                event_tree.delete(*event_tree.get_children())
                curr_list = db.get_list_of_competitors_from_event_division(eve_sv.get(), div_sv.get())
                for comp in curr_list:
                    event_tree.insert('', 'end', text=comp[0], values = (comp[1], comp[-1]))

                first_place_sv.set('')
                first_place_droplist.children['menu'].delete(0, 'end')
                second_place_sv.set('')
                second_place_droplist.children['menu'].delete(0, 'end')
                third_place_sv.set('')
                third_place_droplist.children['menu'].delete(0, 'end')

                null_list = ['null', 'null', 'null']
                curr_list.append(null_list) 

                for comp in curr_list:
                    dude = comp[0]
                    first_place_droplist['menu'].add_command(label=dude, command=lambda value=dude: first_place_sv.set(value))
                    second_place_droplist['menu'].add_command(label=dude, command=lambda value=dude: second_place_sv.set(value))
                    third_place_droplist['menu'].add_command(label=dude, command=lambda value=dude: third_place_sv.set(value))

        tk.Button(t3, text='Get Competitors',width=20,bg='brown',fg='white', command=get_competitors).place(x=535,y=63)

        first_place_list = ['null']
        first_place_sv = tk.StringVar()
        first_place_droplist = tk.OptionMenu(t3, first_place_sv, *first_place_list)
        first_place_droplist.config(width=30)
        first_place_sv.set('Select Winner') 
        first_place_droplist.place(x=700,y=210-4)

        second_place_list = ['null']
        second_place_sv = tk.StringVar()
        second_place_droplist = tk.OptionMenu(t3, second_place_sv, *second_place_list)
        second_place_droplist.config(width=30)
        second_place_sv.set('Select Winner') 
        second_place_droplist.place(x=700,y=240-4)

        third_place_list = ['null']
        third_place_sv = tk.StringVar()
        third_place_droplist = tk.OptionMenu(t3, third_place_sv, *third_place_list)
        third_place_droplist.config(width=30)
        third_place_sv.set('Select Winner') 
        third_place_droplist.place(x=700,y=270-4)
        
        def final_check():
            # eve_sv.get() == "Select Event" or div_sv.get() == "Select Division"
            if eve_sv.get() == "Select Event":
                return False
            elif div_sv.get() == "Select Division":
                return False
            elif div_sv.get() == "Null":
                return False
            elif div_sv.get() == "":
                return False
            elif first_place_sv.get() == "Select Winner" or first_place_sv.get() == "":
                return False
            elif second_place_sv.get() == "Select Winner" or second_place_sv.get() == "":
                return False
            elif third_place_sv.get() == "Select Winner" or third_place_sv.get() == "":
                return False
            elif first_place_sv.get() == "null" and second_place_sv.get() == "null" and third_place_sv.get() == "null":
                return False
            else:
                return True
            
        def everyone_else_list(first, second, third):
            everyone_else = db.get_list_of_competitors_from_event_division(eve_sv.get(), div_sv.get())
            new_list = []
            for element in everyone_else:
                new_list.append(element[0])
        
            new_list.remove(first)
            new_list.remove(second)
            new_list.remove(third)
            return new_list

        def final_submit():
            print("Final Submit Clicked")
            if final_check():
                print("===> Submission Accepted")
                db.score_placement_entry(first_place_sv.get(), 1, eve_sv.get(), div_sv.get())
                db.score_placement_entry(second_place_sv.get(), 2, eve_sv.get(), div_sv.get())
                db.score_placement_entry(third_place_sv.get(), 3, eve_sv.get(), div_sv.get())

                # everyone else
                for other in everyone_else_list(first_place_sv.get(), second_place_sv.get(), third_place_sv.get()):
                    db.score_placement_entry(other, '>=4', eve_sv.get(), div_sv.get())

                print(f"===> Score Entry for {div_sv.get()} Complete")
            else:
                print("===> Submission Denied")

        tk.Button(t3, text='Submit',width=20,bg='brown',fg='white', command=final_submit).place(x=702,y=310)

    def show_scoreboard(self):
        sb.scoreboard_loop()

    def mark_attendance(self):
        t5 = tk.Toplevel(self)
        t5.wm_title("Competitor Attendance Check")
        t5.geometry('505x600')

        pres_comp_lb = tk.Listbox(t5, height = 30, width = 30)
        pres_comp_lb.place(x=300,y=60)
        pres_comp_list = db.get_list_of_present_competitors()
        for competitor in pres_comp_list:
            pres_comp_lb.insert('end', competitor)

        abs_comp_lb = tk.Listbox(t5, height = 30, width = 30)
        abs_comp_lb.place(x=20,y=60)
        abs_comp_list = db.get_list_of_absent_competitors()
        for competitor in abs_comp_list:
            abs_comp_lb.insert('end', competitor)

        def reset_abs_list():
            abs_comp_lb.delete(0, 'end')
            abs_comp_list = db.get_list_of_absent_competitors()
            for competitor in abs_comp_list:
                abs_comp_lb.insert('end', competitor)

        def reset_pres_list():
            pres_comp_lb.delete(0, 'end')
            pres_comp_list = db.get_list_of_present_competitors()
            for competitor in pres_comp_list:
                pres_comp_lb.insert('end', competitor)

        def on_submit():
            curr_selection = abs_comp_lb.get(abs_comp_lb.curselection())
            if curr_selection != "":
                db.set_attendance_val(curr_selection, True)      
                reset_abs_list()
                reset_pres_list()
 
        def on_remove():
            curr_selection = pres_comp_lb.get(pres_comp_lb.curselection())
            if curr_selection != "":
                db.set_attendance_val(curr_selection, False)
                reset_abs_list()
                reset_pres_list()

        tk.Button(t5, text='Submit',width=20,bg='brown',fg='white', command=on_submit).place(x=35,y=560)
        tk.Button(t5, text='Remove',width=20,bg='brown',fg='white', command=on_remove).place(x=317,y=560)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('330x190')
    root.title("Main Menu")
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()