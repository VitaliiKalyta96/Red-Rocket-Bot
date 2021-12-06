def convert_list(list):
    json_list = []
    for el in list:
        json_list.append(el.serialize)
    return json_list