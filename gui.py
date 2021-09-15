import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import liveGui
from database import Database


def schedule_match_screen():
    global root1
    global numEntryMat
    global team1EntryMat
    global team2EntryMat
    global venueEntryMat
    global dateEntryMat
    global delnumEntryMat

    root1 = tkinter.Tk()
    root1.geometry('1450x800')
    root1.title('CMMS')

    scheduleLbl = Label(root1, text="Schedule", font=('Times New Roman', 30))
    scheduleLbl.place(relx=0.2, rely=0.1)

    numlbl = Label(root1, text="Match No : ", font=('Times New Roman', 15))
    numlbl.place(relx=0.1, rely=0.3)

    numEntryMat = Entry(root1, width=10, font=('Times New Roman', 15), state='readonly')
    numEntryMat.place(relx=0.25, rely=0.3)

    team1Lbl = Label(root1, text="Home Team : ", font=('Times New Roman', 15))
    team1Lbl.place(relx=0.1, rely=0.4)

    team1EntryMat = Entry(root1, width=25, font=('Times New Roman', 15))
    team1EntryMat.place(relx=0.25, rely=0.4)

    team2Lbl = Label(root1, text="Away Team : ", font=('Times New Roman', 15))
    team2Lbl.place(relx=0.1, rely=0.5)

    team2EntryMat = Entry(root1, width=25, font=('Times New Roman', 15))
    team2EntryMat.place(relx=0.25, rely=0.5)

    venueLbl = Label(root1, text="Venue : ", font=('Times New Roman', 15))
    venueLbl.place(relx=0.1, rely=0.6)

    venueEntryMat = Entry(root1, width=25, font=('Times New Roman', 15))
    venueEntryMat.place(relx=0.25, rely=0.6)

    dateLbl = Label(root1, text="Date : ", font=('Times New Roman', 15))
    dateLbl.place(relx=0.1, rely=0.7)

    dateEntryMat = Entry(root1, width=25, font=('Times New Roman', 15))
    dateEntryMat.place(relx=0.25, rely=0.7)

    Button(root1, text="Submit", command=schedule_match, font=('Times New Roman', 15)).place(relx=0.2, rely=0.8)
    Button(root1, text="Cancel", command=root1.destroy, font=('Times New Roman', 15)).place(relx=0.3, rely=0.8)

    numEntryMat.configure(state='normal')
    numEntryMat.delete(0, tkinter.END)
    id = list(dbc.getLastInsertedId())
    num = id[0][0]
    if num == None:
        numEntryMat.insert(0, '1')

    else:
        num += 1
        numEntryMat.insert(0, str(num))

    numEntryMat.configure(state='readonly')

    deleteLbl = Label(root1, text="Delete", font=('Times New Roman', 30))
    deleteLbl.place(relx=0.7, rely=0.1)

    delnumlbl = Label(root1, text="Match No : ", font=('Times New Roman', 15))
    delnumlbl.place(relx=0.6, rely=0.35)

    delnumEntryMat = Entry(root1, width=10, font=('Times New Roman', 15))
    delnumEntryMat.place(relx=0.75, rely=0.35)

    Button(root1, text='Show', font=('Times New Roman', 10), command=del_match_message_box).place(relx=0.85, rely=0.35)
    Button(root1, text= 'Delete', font=('Times New Roman', 15), command=delete_match).place(relx=0.65, rely=0.5)
    Button(root1, text='Cancel', font=('Times New Roman', 15), command=root1.destroy).place(relx=0.75, rely=0.5)


    root1.mainloop()


def delete_match():
    if delnumEntryMat.get() != '':
        id = int(delnumEntryMat.get())
        row = list(dbc.getMatch((id,)))
        if row:
            dbc.deleteMatch((id,))
            mb.showinfo('Done!', "Match "+str(id)+" deleted successfully", parent=root1)

        else:
            mb.showerror("Error!", "Match has't been scheduled yet", parent=root1)

    else:
        mb.showerror("Warning", "Please Enter Match Number", parent=root1)


def del_match_message_box():
    if delnumEntryMat.get() != '':
        id = int(delnumEntryMat.get())
        row = list(dbc.getMatch((id,)))
        if row:
            no, home, away, venue, date, res = row[0]
            mb.showinfo("Match", 'Match ' + str(id) + '  ' + home + ' Vs ' + away, parent=root1)

        else:
            mb.showerror("Error", "Match has't been scheduled yet!", parent=root1)

    else:
        mb.showerror("Warning", "Please Enter Match Number", parent=root1)


def schedule_match():
    home = team1EntryMat.get()
    away = team2EntryMat.get()
    venue = venueEntryMat.get()
    date = dateEntryMat.get()

    if home != '' and away != '' and venue != '' and date != '':
        dbc.insertMatch((home.upper(), away.upper(), venue.upper(), date))
        mb.showinfo('Done!', "Match " + home + " Vs " + away + " is scheduled", parent=root1)
        root1.destroy()

    else:
        mb.showerror('Warning', "All Fields are necessary", parent=root1)


def add_result_screen():
    global window
    window = Tk()
    window.geometry('1450x800')
    window.title('CMMS')

    global numEntryRes
    global score1EntryRes
    global score2EntryRes
    global momEntryRes
    global winEntryRes

    titlelbl = Label(window, text="Add Result", font=('Times New Roman', 40))
    titlelbl.place(x=600, y=50)

    numlbl = Label(window, text="Match No : ", font=('Times New Roman', 15))
    numlbl.place(x=400, y=150)

    numEntryRes = Entry(window, width=5, font=('Times New Roman', 15))
    numEntryRes.place(x=500, y=155)

    showbtn = Button(window, text="Show", font=('Times New Roman', 10), command=show_match_message_box)
    showbtn.place(x=600, y=153)

    score1lbl = Label(window, text="Home Team Score : ", font=('Times New Roman', 15))
    score1lbl.place(x=450, y=250)

    score1EntryRes = Entry(window, width=30, font=('Times New Roman', 15))
    score1EntryRes.place(x=650, y=250)

    score2lbl = Label(window, text="Away Team  Score : ", font=('Times New Roman', 15))
    score2lbl.place(x=450, y=300)

    score2EntryRes = Entry(window, width=30, font=('Times New Roman', 15))
    score2EntryRes.place(x=650, y=300)

    momlbl = Label(window, text="Man of the Match : ", font=('Times New Roman', 15))
    momlbl.place(x=450, y=350)

    momEntryRes = Entry(window, width=40, font=('Times New Roman', 15))
    momEntryRes.place(x=650, y=350)

    Button(window, text="Compute Winner", font=('Times New Roman', 15), command=compute_winner).place(x=600, y=390)

    winlbl = Label(window, text="Winning Team : ", font=('Times New Roman', 15))
    winlbl.place(x=450, y=450)

    winEntryRes = Entry(window, width=35, state='readonly', font=('Times New Roman', 15))
    winEntryRes.place(x=650, y=450)

    Button(window, text="Submit", font=('Times New Roman', 15), command=add_result).place(x=550, y=550)
    Button(window, text="Cancel", font=('Times New Roman', 15), command=window.destroy).place(x=700, y=550)

    window.mainloop()


def show_match_message_box():
    if numEntryRes.get() != '':
        id = int(numEntryRes.get())
        row = list(dbc.getMatch((id,)))
        if row:
            no, home, away, venue, date, res = row[0]
            mb.showinfo("Match", 'Match ' + str(id) + '  ' + home + ' Vs ' + away, parent=window)

        else:
            mb.showerror("Error" ,"Match has't been scheduled yet!", parent=window)

    else:
        mb.showerror("Warning", "Please Enter Match Number", parent=window)


def compute_winner():
    try:
        id = int(numEntryRes.get())
        score1 = int(score1EntryRes.get())
        score2 = int(score2EntryRes.get())

        row = list(dbc.getMatch((id,)))
        no, team1, team2, venue, date, res = row[0]

        winEntryRes.configure(state='normal')
        winEntryRes.delete(0, tkinter.END)
        if score1 > score2:
            result = team1

        elif score2 > score1:
            result = team2

        else:
            result = "Match Drawn"

        winEntryRes.insert(0, result)
        winEntryRes.configure(state='readonly')

    except:
        mb.showerror("Error!", "Something went wrong! Try again or Check scheduled matches...", parent=window)


def add_result():
    try:
        id = int(numEntryRes.get())
        match = dbc.getResults((id,))

        flag = False

        for row in match:
            if row[0] == id:
                flag = True

        if flag:
            mb.showerror('Error', 'Result for this match has already been added!', parent=window)

        elif numEntryRes.get() != '' and score1EntryRes.get() != '' and score2EntryRes.get() != '' and momEntryRes.get() != '':
            id = int(numEntryRes.get())
            score1 = int(score1EntryRes.get())
            score2 = int(score2EntryRes.get())
            mom = momEntryRes.get()

            row = list(dbc.getMatch((id,)))
            no, home, away, venue, date, res = row[0]

            if score1 > score2:
                result = home

            elif score2 > score1:
                result = away

            else:
                result = "Match Drawn"

            dbc.insertResult((id, score1, score2, mom.upper(), result.upper()))
            mb.showinfo('Done!', "Result of Match " + str(no) + " is recorded", parent=window)
            window.destroy()

        else:
            mb.showerror('Warning', "All Fields are necessary", parent=window)

    except:
        mb.showerror("Error!", "Something went wrong! Try again or Check scheduled matches...", parent= window)


def show_results_screen():
    global show_res_window
    show_res_window = Tk()
    show_res_window.geometry('1450x800')
    show_res_window.title('CMMS')

    global numEntry
    global team1entry
    global team2entry
    global venueentry
    global dateentry
    global score1entry
    global score2entry
    global momentry
    global winentry



    titlelbl = Label(show_res_window, text="Results", font=('Times New Roman', 40))
    titlelbl.place(x=600, y=50)

    numlbl = Label(show_res_window, text="Match No : ", font=('Times New Roman', 15))
    numlbl.place(x=400, y=150)

    numEntry = Entry(show_res_window, width=5, font=('Times New Roman', 15))
    numEntry.place(x=500, y=155)

    showbtn = Button(show_res_window, text="Show", font=('Times New Roman', 10), command=show_results)
    showbtn.place(x=600, y=153)

    team1lbl = Label(show_res_window, text="Home Team\t: ", font=('Times New Roman', 15))
    team1lbl.place(x=450, y=250)

    team1entry = Entry(show_res_window, font=('Times New Roman', 15), state='readonly', width=25)
    team1entry.place(x=700, y=250)

    team2lbl = Label(show_res_window, text="Away Team\t: ", font=('Times New Roman', 15))
    team2lbl.place(x=450, y=300)

    team2entry = Entry(show_res_window, font=('Times New Roman', 15), state='readonly', width=25)
    team2entry.place(x=700, y=300)

    venuelbl = Label(show_res_window, text="Venue\t\t: ", font=('Times New Roman', 15))
    venuelbl.place(x=450, y=350)

    venueentry = Entry(show_res_window, font=('Times New Roman', 15), state='readonly', width=25)
    venueentry.place(x=700, y=350)

    datelbl = Label(show_res_window, text="Date\t\t: ", font=('Times New Roman', 15))
    datelbl.place(x=450, y=400)

    dateentry = Entry(show_res_window, font=('Times New Roman', 15), state='readonly', width=25)
    dateentry.place(x=700, y=400)

    score1lbl = Label(show_res_window, text="Home Team Score\t: ", font=('Times New Roman', 15))
    score1lbl.place(x=450, y=450)

    score1entry = Entry(show_res_window, font=('Times New Roman', 15), state='readonly', width=25)
    score1entry.place(x=700, y=450)

    score2lbl = Label(show_res_window, text="Away Team Score\t: ", font=('Times New Roman', 15))
    score2lbl.place(x=450, y=500)

    score2entry = Entry(show_res_window, font=('Times New Roman', 15), state='readonly', width=25)
    score2entry.place(x=700, y=500)

    momlbl = Label(show_res_window, text="Player of the Match : ", font=('Times New Roman', 15))
    momlbl.place(x=450, y=550)

    momentry = Entry(show_res_window, font=('Times New Roman', 15), state='readonly', width=25)
    momentry.place(x=700, y=550)

    winlbl = Label(show_res_window, text="Winning Team\t: ", font=('Times New Roman', 15))
    winlbl.place(x=450, y=600)

    winentry = Entry(show_res_window, font=('Times New Roman', 15), state='readonly', width=25)
    winentry.place(x=700, y=600)

    show_res_window.mainloop()


def show_results():
    try:
        id = int(numEntry.get())

        match = list(dbc.getMatch((id,)))
        no, home, away, venue, date, res = match[0]

        result = list(dbc.getResults((id,)))
        matno, score1, score2, mom, win = result[0]

        team1entry.configure(state='normal')
        team1entry.delete(0, tkinter.END)
        team1entry.insert(0, home)
        team1entry.configure(state='readonly')

        team2entry.configure(state='normal')
        team2entry.delete(0, tkinter.END)
        team2entry.insert(0, away)
        team2entry.configure(state='readonly')

        venueentry.configure(state='normal')
        venueentry.delete(0, tkinter.END)
        venueentry.insert(0, venue)
        venueentry.configure(state='readonly')

        dateentry.configure(state='normal')
        dateentry.delete(0, tkinter.END)
        dateentry.insert(0, date)
        dateentry.configure(state='readonly')

        score1entry.configure(state='normal')
        score1entry.delete(0, tkinter.END)
        score1entry.insert(0, score1)
        score1entry.configure(state='readonly')

        score2entry.configure(state='normal')
        score2entry.delete(0, tkinter.END)
        score2entry.insert(0, score2)
        score2entry.configure(state='readonly')

        momentry.configure(state='normal')
        momentry.delete(0, tkinter.END)
        momentry.insert(0, mom)
        momentry.configure(state='readonly')

        winentry.configure(state='normal')
        winentry.delete(0, tkinter.END)
        winentry.insert(0, win)
        winentry.configure(state='readonly')

    except:
        mb.showerror("Error!", "Something went wrong! Try again or Check scheduled matches...", parent= show_res_window)


def show_matches_screen():
    window = Tk()
    window.geometry('1450x800')
    window.title('CMMS')

    titlelbl = Label(window, text="Scheduled Matches", font=('Times New Roman', 40))
    titlelbl.place(x=500, y=50)

    tree = ttk.Treeview(window, selectmode='browse', height= 20)
    tree.place(x=70, y=200)

    scroll = ttk.Scrollbar(window, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='x')

    tree.configure(xscrollcommand=scroll.set)

    tree["columns"] = ("1", "2", "3", "4", "5", "6")

    tree['show'] = "headings"

    tree.column("1", width=200, anchor="c")
    tree.column("2", width=200, anchor="c")
    tree.column("3", width=200, anchor="c")
    tree.column("4", width=200, anchor="c")
    tree.column("5", width=200, anchor="c")
    tree.column("6", width=200, anchor="c")

    tree.heading("1", text="Match No")
    tree.heading("2", text="Home Team")
    tree.heading("3", text="Away Team")
    tree.heading("4", text="Venue")
    tree.heading("5", text="Date")
    tree.heading("6", text="Result Status")

    matches = list(dbc.getMatches())
    for mat in matches:
        tree.insert('', 'end', values=mat)

    window.mainloop()


root = tkinter.Tk()
root.geometry('1450x800')
root.title('CMMS')

dbc = Database()
dbc.createTable()

image_file = PhotoImage(file="homepage.png")
lbl = Label(root, image=image_file).place(relx=0, rely=0)

Label(lbl, text="Manage The Matches", bg='blue', font=('Times New Roman', 50)).place(relx=0.3, rely=0.1)

Button(lbl, text="Display Matches", font=('Times New Roman', 20), command=show_matches_screen).place(relx=0.1, rely=0.5)

Button(lbl, text="Schedule/Delete Match", font=('Times New Roman', 20), command=schedule_match_screen).place(relx=0.3,
                                                                                                      rely=0.5)

Button(lbl, text="Add Result", font=('Times New Roman', 20), command=add_result_screen).place(relx=0.55, rely=0.5)

Button(lbl, text="Show Match Results", font=('Times New Roman', 20), command=show_results_screen).place(relx=0.7,
                                                                                                        rely=0.5)

Button(lbl, text="Live Match", font=('Times New Roman', 20), command=liveGui.live_match_screen).place(relx=0.45,
                                                                                                        rely=0.65)

root.mainloop()
