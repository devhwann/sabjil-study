def solution(new_id):
    new_id = new_id.lower()

    for i in new_id:
        if not i.isalnum() and i not in "-_.":
            new_id = new_id.replace(i, "")

    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    new_id = new_id.strip(".")

    if new_id == "":
        new_id += "a"

    if len(new_id) > 15:
        new_id = new_id[:15].rstrip(".")

    new_id += new_id[-1] * (3 - len(new_id))

    return new_id
