import re
import os


if __name__ == "__main__":
    if os.path.exists('django-edited.log'):
        os.remove('django-edited.log')
    log = open('django_success.log', 'r')
    log_text = log.read()
    log.close()
    first_text = re.sub(
        r'[A-Za-z0-9_\/\-]*\/admin\/[A-Za-z0-9_\/\-\.]*',
        r'asdasf/asdas/asdas',
        log_text
    )
    second_text = re.sub(
        r'\[\d{2}\/[A-Z][a-z]{2}\/\d{4}\s(\d{2}:?){3}\]',
        r'[XX/XXX/XXXX XX:XX:XX]',
        first_text
    )

    with open('django-edited.log', 'a') as write_file:
        write_file.write(second_text)
