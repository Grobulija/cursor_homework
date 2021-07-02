import re

if __name__ == "main":
    log = open('django_success.log', 'r')
    log_text = log.read()
    log.close()
    print(log_text)
    new_text = re.sub(
        r'[A-Za-z0-9_\/\-]*\/admin\/[A-Za-z0-9_\/\-\.]*',
        r'asdasf\/asdas\/asdas',
        log_text
    )
    print(new_text)
