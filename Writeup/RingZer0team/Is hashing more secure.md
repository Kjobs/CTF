Is hashing more secure?
-------

writeup:
View the source code and there are some important infomation in somewhere!
Got it!
```javascript
			// Look's like weak JavaScript auth script :)
			$(".c_submit").click(function(event) {
				event.preventDefault();
				var p = $("#cpass").val();
				if(Sha1.hash(p) == "b89356ff6151527e89c4f3e3d30c8e6586c63962") {
				    if(document.location.href.indexOf("?p=") == -1) {   
				        document.location = document.location.href + "?p=" + p;
				    }
				} else {
				    $("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
				}
			});
```
So,the question is going to challenge us with the decryption of SHA1.

We can use tools to finish it with this ciphertext "b89356ff6151527e89c4f3e3d30c8e6586c63962".

Finally we can get the password "adminz".Back to the challenge page and submit with the password,then get the flag.
