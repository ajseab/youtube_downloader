CHECK requirements.txt

MUST change 'DOWNLOAD_PATH' to the path you want the file downloaded to

ERROR: 
    In case of RegexMatchError replace: 
      'cypher.py' line 30: var_regex = re.compile(r"^\w+\W")
            with         : var_regex = re.compile(r"^\$*\w+\W")