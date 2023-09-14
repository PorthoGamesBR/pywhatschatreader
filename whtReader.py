"""
Reads and process messages from a whatsapp downloaded chat file (Link to get the file: https://faq.whatsapp.com/1180414079177245/?cms_platform=android)
Lê e processa mensagens de um arquivo baixado de uma conversa do whatsapp (Link para baixar o arquivo: https://faq.whatsapp.com/1180414079177245/?cms_platform=android)

Contains functions to transform a chat message file from whatsapp into usable data for python apps (As dict)
Contém funções para transformar um arquivo de mensagens do whatsapp em dados utilizáveis em aplicações python (Em forma de dict)

Functions:

    open_conversa(str) -> TextIOWrapper
    is_new_message(str) -> bool
    read_all_messages(TextIoWrapper) -> list[str]
    format_message(str,str,str,str) -> dict[str,dict[str,str] | str]
    separate_data(str) -> list[str]
    list_of_messages(list[str]) -> list[dict[str,str]]
    
"""
import re
from io import TextIOWrapper
    
def open_conversa(filepath:str) -> TextIOWrapper:
    """Opens a whatsapp downloaded chat text file

    Args:
        filepath (str): Path of the file

    Returns:
        conversa/chat (TextIOWrapper): Buffer interface for text, just like open()
    """
    return open(filepath, encoding="utf-8")

def is_new_message(line:str) -> bool:
    """Check if a line of text contains the elements of the start of a message (date,hour and contact name) and returns true if so

    Args:
        line (str): Line of text

    Returns:
        bool: True if is the start of a message, false if is not
    """
    regx = r"^(([0-9]{2}/){2}[0-9]{4} [0-9]{2}:[0-9]{2} - )"
    match = re.search(regx,line)
    return not(match == None)

def read_all_messages(conversa:TextIOWrapper) -> list[str]:
    """Reads from a conversa/chat text file and converts it into a list of strings. Beware if file is too big

    Args:
        conversa (TextIOWrapper): Can be generated with open_conversa()

    Returns:
        list[str]: List with all messages from this conversa/chat
    """
    toReturn = []
    msg_body = ""
    for l in conversa:
        # Check if is the start of a message
        if is_new_message(l):
            # if it is, add the last message to toReturn (unless msg_body is empty)
            if len(msg_body) > 0:
                toReturn.append(msg_body)
                msg_body = ""
        msg_body += l
        
    return toReturn

def format_message(date:str, hour:str, name:str, text:str) -> dict[str,dict[str,str] | str]:
    """Formats a list with data from a message into a dict

    Args:
        date (str): date that the message was sent
        hour (str): hour that the message was sent
        name (str): username that sent the message
        text (str): content of the message

    Returns:
        dict[str,dict[str,str] | str]: dict with date-hour{d,h}, username and text
    """
    return {"date-hour":{
                "d":date,
                "h":hour,
            },
            "username":name,
            "text":text}

def separate_data(msg: str) -> list[str]:
    """
    Parses the msg string into a list
    Every text message on whatsapp follows this pattern:
    DD/MM/YYYY hh:mm -Username/Cellphone Number: Message

    Args:
        msg (str): String with the whole message

    Returns:
        list[str]: list containing date,hour,username,message in this order
    """
    # This separates the date and hour from the rest of the string while creating the list to return
    data = [msg[:10],msg[11:16],"",""]
    # Separates the username and message from the rest
    nick_and_text = msg[19:]
    # Regex to separate the message from the username (I dont think usernames can have : on them)
    regx = f': '
    match = re.split(regx,nick_and_text,1)
    # This will work if is a message and not an alert. If it is an alert (No username), match will be None
    if match and len(match) > 1:
        data[2] = match[0]
        data[3] = match[1]
    else:
        data[3] = match[0]
    return data


def list_of_messages(ls: list[str]) -> list[dict[str,str]]:
    """Turns a list of messages into a list of dicts with data of the messages

    Args:
        ls (list[str]): List of messages. Can be loaded with read_all_messages()

    Returns:
        list[dict[str,str]]: List of dicts with the data parsed from the messages
    """
    toReturn = []
    for d in ls:
        date,hour,name,text = separate_data(d)
        toReturn.append(format_message(date,hour,name,text))
    return toReturn