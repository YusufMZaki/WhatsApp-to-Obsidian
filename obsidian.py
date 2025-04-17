import re
import os
from folder_editor import move_file, Folder_format, read_chat, obsidian_delete, Month_Header
from chat_editor import Full_chat, chat_dates, Name_Highlight, Pesan_diedit

move_file() # move files on /File except whatsapp chat
obsidian_delete() # delete available notes
        
def write_chat(date, folder): # write on obsidian notes "yy_name.md"
    current_month, month, year = 0, 0, 0 # state the early date variable with 0
    for chat in read_chat(date, folder): # read whatsapp chat and return every line
        if Full_chat(chat): # condition chat contain "dates clock - name: messages"
            current_month, year = chat_dates(chat.split()) # identify current month and year
            chat = Name_Highlight(chat, "YMZ") # highlight name
            
        file = open(f"{date} {folder}\{year}_{folder}.md", "a", encoding="utf8") # folder location \ naming obsidian note .md
        month = Month_Header(file, month, current_month, f"{Pesan_diedit(chat)}") # write header by month and chat line (while edit message)
    
def main():
    for _ in os.listdir(): # find chat folder available
        if Folder_format(_): # folder format "yyyy_mm_dd name"
            write_chat(*_.split(" ",1)) # devide date and name

if __name__ == "__main__":
    main()