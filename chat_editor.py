import re

def Full_chat(chat):
    if re.search(r"^([0-9]+\/?)+\s([0-9]+\.?)+\s\-\s.+\:\s.+$", chat): return True
    else: return False
    
def chat_dates(chat):
    chat2date = chat[0].split("/")
    return [chat2date[1], chat2date[2]]

def Name_Highlight(chat, name):
    if re.search(name, chat.split(":", 1)[0]):
        chat = chat.replace(name, f"=={name}==")
    return chat
    
def Link_Detection(chat):
    link_find = re.findall(r"\s(https://\S+|www\.\S+)", chat)
    link_start = re.findall(r"^(https://\S+|www\.\S+)", chat)
    chat = re.sub(r"(\s#|^#)"," ",chat)
    if link_find or link_start:
        for _ in link_find + link_start:
            link_split = re.sub(r"(https://)?(www\.)?","",_)
            link_slash = link_split.split("/")[0].replace(".","")
            if (re.search("youtu", link_slash)) and (not re.search(r"(shorts|playlist|channel)", chat)):
                chat = chat.replace(_, f"#{link_slash} ![]({_})")
            else:
                chat = chat.replace(_, f"#{link_slash} {_}")
    return chat

def Pesan_diedit(chat):
    chat = Link_Detection(chat)
    if re.search("<Pesan ini diedit>", chat): 
        chat = chat.replace("<Pesan ini diedit>", "")
    return chat