Why not?
--------

Writeup:
View the source code and we can get this code:
```javascript
			// Look's like weak JavaScript auth script :)
			$(".c_submit").click(function(event) {
				event.preventDefault();
				var k = new Array(176,214,205,246,264,255,227,237,242,244,265,270,283);
				var u = $("#cuser").val();
				var p = $("#cpass").val();
				var t = true;

				if(u == "administrator") {
					for(i = 0; i < u.length; i++) {
						if((u.charCodeAt(i) + p.charCodeAt(i) + i * 10) != k[i]) {
							$("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
							t = false;
							break;
						}
					}
				} else {
					$("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
					t = false;
				}
				if(t) {
					if(document.location.href.indexOf("?p=") == -1) {
						document.location = document.location.href + "?p=" + p;
               			}
				}
			});
```

There have a cuser named "administrator".We just need to kown the password.
After understood the code,I wrote the python code:
```python
list1 = [176,214,205,246,264,255,227,237,242,244,265,270,283]
cuser = map(ord, "administrator")
cpass = ""
for i in range(0,len(list1)):
    num = list1[i]-i*10-cuser[i]
    cpass = cpass+(chr(num))
print cpass
```
Run with the code,finally I got the password:OhLord4309111
Submit the username and the password and we can see flag.
