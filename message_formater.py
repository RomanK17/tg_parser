def format_message(items_list):
    splitted_messages : list = []
    res_message = ""
    for item in items_list:
        text = f"{item['name']}\nЦена: {item['price']}\n"

        if len(res_message) + len(text) > 4096:
            splitted_messages.append(res_message)
            res_message = text
        else:
            res_message += text

    if res_message:
        splitted_messages.append(res_message)
    return splitted_messages
    

