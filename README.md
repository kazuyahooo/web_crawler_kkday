# web_crawler_kkday
This is my first assignment in Web Intelligence and Message Understanding.
## Ajax Crawler
- KKday website is based on Ajax tech, the most of the contents in the html are unicode data. For this reason, we need to find the data in the following steps:
    - Press F12 and click on the Network page
    - Select Fetch/XHR only and review the key point requests
    - Check the response which has the web contents we want
    - Use the link in the header as the request url

- Final step: know that the parameters represent the meaning, you can find everything you want on KKday!
## Problems

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
