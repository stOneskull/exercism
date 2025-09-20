def grep(pattern, flags, files):
    result = ''

    for file in files:
        with open(file, 'r') as text:
            pattern = pattern.lower() if '-i' in flags else pattern

            for linenum, line in enumerate(text.readlines()):
                _line = line.lower() if '-i' in flags else line
                
                if ('-v' in flags) ^ (
                    pattern in _line and '-x' not in flags
                        or pattern + '\n' == _line):
                    if '-l' in flags:
                        result += file + '\n'
                        break
                    if len(files) > 1:
                        result += file + ':'
                    if '-n' in flags:
                        result += f"{linenum+1}:"
                    result += line
                
    return result
