# web_crawler_kkday
This is my first task in Web Intelligence and Message Understanding.

## Problem

- fake_useragent module not connecting properly - IndexError: list index out of range
  - solution: modified fake_useragent.utils.py line99
  - https://github.com/hellysmile/fake-useragent/pull/110
  ```python
  html = html.split('<table class="w3-table-all notranslate">')[1] #origin
  html = html.split('<table class="ws-table-all notranslate">')[1] #change w3 to ws
  ```
- Syntax Error: Non-UTF-8 code starting with '\xe9' in file
  - solution: add this line in the code
  ```python
  # -*- coding: utf-8 -*-
  ```
