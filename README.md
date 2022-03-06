# web_crawler_kkday
This is my first task in Web Intelligence and Message Understanding.

## Problem

- fake_useragent module not connecting properly - IndexError: list index out of range
  - solution: modified fake_useragent.utils.py line99
  ```python
  html = html.split('<table class="w3-table-all notranslate">')[1] #origin
  html = html.split('<table class="ws-table-all notranslate">')[1] #change w3 to ws
  ```
