This is Pyside6 Project
To download YouTube videos, I uses the pytube library

To solve the pytube bug(When youtube download, raise RegexMatchError), I change cipher.py 30 line
var_regex = re.compile(r"^\w+\W") ->
var_regex = re.compile(r"^\$*\w+\W")