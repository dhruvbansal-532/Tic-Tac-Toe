import tkinter as tk

root = tk.Tk() 
root.title('Tic Tac Toe')
root.geometry('525x680')
root.configure(bg="#191970")

title_label = tk.Label(root, text='Tic Tac Toe', font=('Segoe UI', 22, 'bold'), bg='#191970', fg='#FFFFFF')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

status_label = tk.Label(root, text='Current turn: X', font=('Segoe UI', 13, 'bold'), bg='#191970', fg='#FFFFFF')
status_label.grid(row=4, column=0, columnspan=3, pady=8)

buttons = []
current_player='X'
game_over = False
def button_clicked(button_text):
    global current_player
    if game_over == False:
        if button_text.cget('text')=='':
            button_text.config(text=current_player)
            check_winner()
            if game_over==False:
                check_draw()
                if not game_over:
                    if current_player=='X':
                        current_player='O'
                        status_label.config(text='Current turn: O')
                    else:
                        current_player='X'
                        status_label.config(text='Current turn: X')

def declare_winner(player, winning_cells):
    global game_over
    status_label.configure(text=f'Player {player} won!')

    for index in winning_cells:
        buttons[index].configure(bg='#8BE9A8')
    game_over=True

def check_draw():
    global game_over
    for elt in buttons:
        if elt.cget('text') == '':
            return
    status_label.configure(text="It's a draw!")
    game_over =True

def check_winner():
    
    if buttons[0].cget('text')==buttons[1].cget('text')==buttons[2].cget('text') and buttons[0].cget('text')!='':
        declare_winner(buttons[0].cget('text'), [0,1,2])

    elif buttons[3].cget('text')==buttons[4].cget('text')==buttons[5].cget('text') and buttons[3].cget('text')!='':
        declare_winner(buttons[3].cget('text'), [3,4,5])

    elif buttons[6].cget('text')==buttons[7].cget('text')==buttons[8].cget('text') and buttons[6].cget('text')!='':
        declare_winner(buttons[6].cget('text'), [6,7,8])

    elif buttons[0].cget('text')==buttons[3].cget('text')==buttons[6].cget('text') and buttons[0].cget('text')!='':
        declare_winner(buttons[0].cget('text'), [0,3,6])

    elif buttons[1].cget('text')==buttons[4].cget('text')==buttons[7].cget('text') and buttons[1].cget('text')!='':
        declare_winner(buttons[1].cget('text'), [1,4,7])

    elif buttons[2].cget('text')==buttons[5].cget('text')==buttons[8].cget('text') and buttons[2].cget('text')!='':
        declare_winner(buttons[2].cget('text'), [2,5,8])

    elif buttons[0].cget('text')==buttons[4].cget('text')==buttons[8].cget('text') and buttons[0].cget('text')!='':
        declare_winner(buttons[0].cget('text'), [0,4,8])

    elif buttons[2].cget('text')==buttons[4].cget('text')==buttons[6].cget('text') and buttons[2].cget('text')!='':
        declare_winner(buttons[2].cget('text'), [2,4,6])

def restart_game():
    global game_over, current_player
    game_over=False
    current_player='X'

    for elt in buttons:
        elt.configure(text='', bg='#E6F1FF')
    status_label.configure(text='Current turn: X')

restart_button = tk.Button(root, text='Restart Game', command=restart_game, bg='#8BE9A8', fg='#191970', font=('Segoe UI', 12, 'bold'), padx=12, pady=6, activebackground='#6FD995', activeforeground='#191970')
restart_button.grid(row=5, column=0, columnspan=3)

for row in range(3):
    for column in range(3):
        button = tk.Button(root, text="", font=('Segoe UI', 32, 'bold'), bg='#E6F1FF', fg='#191970', width=6, height=2)
        button.configure(command=lambda b=button: button_clicked(b))
        buttons.append(button)
        button.grid(row=row+1, column=column, padx=4, pady=4)


root.mainloop()

