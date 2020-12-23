
def to_str(l):
    return ''.join(l)


def lz77_encode(text):
    final_code = ''
    sb_len = 10
    lab_len = 6
    search_buffer = []
    look_ahead_buffer = [text[i] for i in range(lab_len)]
    i = lab_len
    while len(look_ahead_buffer) > 1:
        offset = 0
        match_len = 0
        char = look_ahead_buffer[0]

        if char not in search_buffer:
            search_buffer.insert(0, char)
            if len(search_buffer) > sb_len:
                search_buffer.pop()
            look_ahead_buffer.pop(0)

        else:
            match_len = 1
            offset = search_buffer.index(char)
            substring = char
            j = 1
            if j < len(look_ahead_buffer):
                substring += look_ahead_buffer[j]

            position = to_str(reversed(search_buffer)).find(substring)

            while position != -1:
                j += 1
                offset = len(search_buffer) - position - 1
                match_len += 1
                if j < len(look_ahead_buffer):
                    substring += look_ahead_buffer[j]
                else:
                    break

                position = to_str(reversed(search_buffer)).find(substring)
                new_substring = ''
                if offset + 1 - len(substring) < 0:
                    new_substring += substring[offset+1:]
                    new_position = to_str(look_ahead_buffer).find(new_substring)
                    while new_position != -1:
                        j += 1
                        match_len += 1

                        if j < len(look_ahead_buffer):
                            new_substring += look_ahead_buffer[j]
                        else:
                            break
                        new_position = to_str(look_ahead_buffer)

                    substring = substring[:-1] + new_substring[:-1]
                    j -= 1
                    match_len -= 1

            if j < len(look_ahead_buffer):
                char = look_ahead_buffer[j]
            else:
                char = 'none'

            for k in range(len(substring)):
                search_buffer.insert(0, substring[k])
            while len(search_buffer) > sb_len:
                search_buffer.pop()
            for k in range(len(substring)):
                if len(look_ahead_buffer) > 0:
                    look_ahead_buffer.pop(0)
        while i < (len(text)) and len(look_ahead_buffer) < lab_len:
            look_ahead_buffer.append(text[i])
            i += 1

        code = '{}{}{}'.format(offset, match_len, char)
        final_code += code

    return final_code


def lz77_decode(code):
    text = []

    for j in range(len(code)):
        if (j + 1) % 3 == 0:
            offset = int(code[j-2])
            match_len = int(code[j-1])
            letter = code[j]

            if offset == 0 and match_len == 0:
                text.append(letter)
                continue
            else:
                j = 0
                substring = ''
                while match_len > 0:
                    if len(text) - offset + j - 1 < len(text):
                        substring += text[len(text) - offset + j - 1]
                    else:
                        j = j % 3
                        substring += text[len(text) - offset + j - 1]
                    j += 1
                    match_len -= 1
                for char in substring + letter:
                    text.append(char)

    return to_str(text)


def main():
    code = lz77_encode('cabracadabrarrarrad')
    print(code)
    text = lz77_decode(code)
    print(text)

main()