is_non_negative_num = lambda s: True if s.replace('.', "", 1)[0] != "-" and s.upper() == s.lower() and s.replace(".", "", 2) == s.replace(".", "", 1) else False