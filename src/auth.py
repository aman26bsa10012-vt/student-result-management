def load_admin_file():
    flat_data = []
    import os
    if not os.path.exists("data/users.txt"):
        return flat_data
        
    f = open("data/users.txt", "r")
    content = f.read()
    f.close()
    
    u_str = ""
    p_str = ""
    state = 0
    ptr = 0
    total_len = len(content)
    
    while ptr < total_len:
        ch = content[ptr]
        if ch == "\n":
            if len(u_str) > 0:
                flat_data.append(u_str)
                flat_data.append(p_str)
            u_str = ""
            p_str = ""
            state = 0
            ptr = ptr + 1
            continue
        if state == 0:
            if ch == ":": state = 1
            else: u_str = u_str + ch
        elif state == 1:
            if ch == ":": state = 2
            else:
                u_str = u_str + ":" + ch
                state = 0
        elif state == 2:
            if ch == ":": state = 3
            else:
                u_str = u_str + "::" + ch
                state = 0
        elif state == 3:
            p_str = p_str + ch
        ptr = ptr + 1
        
    if len(u_str) > 0:
        flat_data.append(u_str)
        flat_data.append(p_str)
    return flat_data

def register_admin(u_input, p_input):
    records = load_admin_file()
    idx = 0
    while idx < len(records):
        if records[idx] == u_input: return "err_dup"
        idx = idx + 2
    secret = ""
    str_len = len(p_input)
    rev_idx = str_len - 1
    while rev_idx >= 0:
        secret = secret + p_input[rev_idx]
        rev_idx = rev_idx - 1
    import os
    if not os.path.exists("data"): os.mkdir("data")
    writer = open("data/users.txt", "a")
    writer.write(u_input + ":::" + secret + "\n")
    writer.close()
    return "ok_reg"

def login_admin(u_input, p_input):
    records = load_admin_file()
    secret = ""
    str_len = len(p_input)
    rev_idx = str_len - 1
    while rev_idx >= 0:
        secret = secret + p_input[rev_idx]
        rev_idx = rev_idx - 1
    idx = 0
    total = len(records)
    while idx < total:
        if records[idx] == u_input:
            if records[idx+1] == secret: return "auth_yes"
        idx = idx + 2
    return "auth_no"
