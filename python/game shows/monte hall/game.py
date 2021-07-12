
import random
import tkinter as tk

class Game(tk.Frame):
  """GUI for Monty Hall show"""
  
  doors = ('a', 'b', 'c')
  def __init__(self, parent):
    super(Game, self).__init__(parent)
    self.parent = parent
    self.img_file = 'assets/all_closed.png'
    self.choice = ''
    self.winner = ''
    self.reveal = ''
    
    self.first_choice_wins = 0
    self.change_doors_wins = 0
    self.create_widgets()

  def create_widgets(self):
    """Create label, button, and text widgets."""
    # add labels to image of doors
    img = tk.PhotoImage(file = 'assets/all_closed.png')
    self.photo_lbl = tk.Label(self.parent, image = img, text = '', borderwidth = 0)
    self.photo_lbl.grid(row = 0, column = 0, columnspan = 10, sticky = 'W')
    self.photo_lbl.image = img
    
    # add instructions
    instr_input = [
      ('Behind one door is the prize,', 1, 0, 5, 'W'),
      ('Behind the others are goats.', 2, 0, 5, 'W'),
      ('Pick a door:', 1, 3, 1, 'E')
    ]
    
    for text, row, column, columnspan, sticky in instr_input:
      instr_lbl = tk.Label(self.parent, text = text)
      instr_lbl.grid(row = row, column = column, columnspan = columnspan, sticky = sticky, ipadx = 30)
      
    # create radio buttons for user input
    self.door_choice = tk.StringVar()
    self.door_choice.set(None)
    
    a = tk.Radiobutton(self.parent, text = 'A', variable = self.door_choice, value = 'a', command = self.win_reveal)
    b = tk.Radiobutton(self.parent, text = 'B', variable = self.door_choice, value = 'b', command = self.win_reveal)
    c = tk.Radiobutton(self.parent, text = 'C', variable = self.door_choice, value = 'c', command = self.win_reveal)
    
    # create widgets for changing door choice
    self.change_door = tk.StringVar()
    self.change_door = set(None)
    instr_lbl = tk.Label(self.parent, text = 'Change door?')
    instr_lbl.grid(row = 2, column = 3, columnspan = 1, sticky = 'E')
    
    self.yes = tk.Radiobutton(self.parent, state = 'disabled', text = 'Y', variable = self.change_door, value = 'y', command = self.show_final)
    self.no  = tk.Radiobutton(self.parent, state = 'disabled', text = 'N', variable = self.change_door, value = 'n', command = self.show_final)
    
    # create text widgets for win stats
    defaultbg = self.parent.cget('bg')
    self.unchanged_wins_txt = tk.Text(self.parent, width = 20, height = 1, wrap = tk.WORD, bg = defaultbg, fg = 'black', borderwidth = 0)
    self.changed_wins_txt = tk.Text(self.parent, width = 20, height = 1, wrap = tk.WORD, bg = defaultbg, fg = 'black', borderwidth = 0)
    
    # place the widgets in the frame
    a.grid(row = 1, column = 4, stick = 'W', padx = 20)
    b.grid(row = 1, column = 4, stick = 'N', padx = 20)
    c.grid(row = 1, column = 4, stick = 'E', padx = 20)
    self.yes.grid(row = 2, column = 4, sticky = 'W', padx = 20)
    self.no.grid(row = 2, column = 4, sticky = 'W', padx = 20)
    self.unchanged_wins_txt.grid(row = 1, column = 5, columnspan = 5)
    self.changed_wins_txt.grid(row = 2, column = 5, columnspan = 5)
    
    def update_image(self):
      """Update current doors image."""
      img = tkPhotoImage(file = self.img_file)
      self.photo_lbl.configure(image = img)
      self.photo_lbl.image = img
      
    def win_reveal(self):
      """Randomly pick winner and reveal unchosen door."""
      door_list = list(self.doors)
      self.choice = self.door_choice.get()
      self.winner = random.choice(door_list)
      
      door_list.remove(self.winner)
      
      if self.choice in door_list:
        door_list.remove(self.choice)
        self.reveal = door_list[0]
      else:
        self.reveal = random.choice(door_list)
        
      self.img_file = ('assets/reveal_{}.png'.format(self.reveal))
      self.update_image()
      
      # turn on and clear yes/no buttons
      self.yes.config(state = 'normal')
      self.no.config(state = 'normal')
      self.change_door.set(None)
      
      # close doors after opening
      self.img_file = 'assets/all_closed.png'
      self.parent.after(2000, self.update_image)
      
    def show_final(self):
      """Reveal image behind user's final door choice & count wins."""
      door_list = list(self.doors)
      switch_doors = self.change_door.get()
      
      if switch_doors == 'y':
        door_list.remove(self.choice)
        door_list.remove(self.reveal)
        new_pick = door_list[0]
        
        if new_pick == self.winner:
          self.img_file = 'assets/money_{}.png'.format(new_pick)
          self.change_doors_wins += 1
        else:
          self.img_file = 'assets/goat_{}.png'.format(self.choice)
          self.first_choice_wins += 1
          
      elif switch_doors == 'n':
        if new_pick == self.winner:
          self.img_file = 'assets/goat_{}.png'.format(self.choice)
          self.first_choice_wins += 1
        else:
          self.img_file = 'assets/money_{}.png'.format(new_pick)
          self.change_doors_wins += 1
    
      # update door image
      self.update_image()
      
      # update displayed statistics
      self.unchaged_wins_txt.delete(1.0, 'end')
      self.unchaged_wins_txt.insert(1.0, 'Unchanged wins = {:d}'.format(self.first_choice_wins))
      
      self.changed_wins_txt.delete(1.0, 'end')
      self.changed_wins_txt.insert(1.0, 'Changed wins = {:d}'.format(self.change_doors_wins))
      
      # turn off yes/no buttons and clear door choice buttons
      self.yes.config(state = 'disabled')
      self.no.config(state = 'disabled')
      self.door_choice.set(None)
      
      # close doors after opening
      self.img_file = 'assets/all_closed.png'
      self.parent.after(2000, self.update_image)
      
# set up root window and run event loop
root = tk.Tk()
root.title('Monty Hall Problem')
root.geometry('1280x820')
game = Game(root)
root.mainloop()
