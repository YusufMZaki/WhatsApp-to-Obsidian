import re
import os
import shutil

def Folder_format(chat):
    if re.search(r"^([0-9]+\_?)+\s.+",chat): return True
    else: return False
    
def read_chat(date, folder):
    with open(f"{date} {folder}\Chat WhatsApp dengan {folder}.txt", "r", encoding="utf8") as file:
        lines = file.readlines()
        for line in lines:
            if re.search("(file terlampir)", line):
                strip = line.split(":", 1)[1]
                document = strip[2:].split(" (file terlampir)")
                yield line.split(":", 1)[0] + ": " + f"![[{document[0]}]]" + "\n"
            elif re.search("<Media tidak disertakan>", line):
                strip = line.split(":", 1)[1]
                document = strip[1:-1]
                yield line.split(":", 1)[0] + ": " + f"![[{document}]]" + "\n"
            else:
                yield line

def move_file():
    for _ in os.listdir():
        if Folder_format(_):
            date, folder = _.split(" ", 1)
            try: os.makedirs(f"{_}/Files")
            except: pass
            for Files in os.listdir(_):
                if (Files != "Files") and (Files != f"Chat WhatsApp dengan {folder}.txt") and (not re.search(r"^[0-9]{1,2}\_.+\.md$", Files)):
                    source = f"{_}/{Files}"
                    destination = f"{_}/Files/{Files}"
                    shutil.move(source, destination)

def obsidian_delete():
    for _ in os.listdir():
        if Folder_format(_):
            group_chat = os.listdir(_)
            for md in group_chat:
                if re.search(r"^.+\.md$", md):
                    os.remove(f"{_}/{md}")

def Month_Header(file, month, current_month, chat):
    if month != current_month:
        month = current_month
        file.write(f"## {month}" + "\n")
    file.write(chat)
    return month