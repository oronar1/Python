import re

#define parse_date below
def parse_date(data):
    date_regex=re.compile(r'^(\d{2}|\d{1})[,/.](\d{2})[,/.](\d{4})$')
               #re.compile(r'^(\d{2}|\d{1})(,|/|.)(\d{2})(,|/|.)(\d{4})$')
    matches=date_regex.search(data)
    if matches:
        return {'d':matches.group(1),
                'm':matches.group(2),
                'y':matches.group(3)
        }
    return None
