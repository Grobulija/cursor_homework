import re
import os

FILE = 'django_success.log'
EDITED_FILE = 'django_edited.log'


def file_read(file):
    log = open(file, 'r')
    log_text = log.read()
    log.close()
    return log_text


def file_write(file, text):
    with open(file, 'a') as write_file:
        write_file.write(text)



def hide_admin_path(text):
    return re.sub(
        r'[A-Za-z0-9_\/\-]*\/admin\/[A-Za-z0-9_\/\-\.]*',
        r'asdasf/asdas/asdas',
        text
    )


def hide_data_time(text):
    return re.sub(
        r'\[\d{2}\/[A-Z][a-z]{2}\/\d{4}\s(\d{2}:?){3}\]',
        r'[XX/XXX/XXXX XX:XX:XX]',
        text
    )


if __name__ == "__main__":
    if os.path.exists(EDITED_FILE):
        os.remove(EDITED_FILE)
    log_text = file_read(FILE)
    new_text = hide_admin_path(log_text)
    new_text = hide_data_time(new_text)
    print(new_text)
    file_write(EDITED_FILE, new_text)
