Then obfuscation is more secure?
-------

Writeup:
Like previous challenges,we should view the sourse code firstly.That would often help us.
This time the source code is also help me.Look this!
```
var _0xc360=["\x76\x61\x6C","\x23\x63\x70\x61\x73\x73","\x61\x6C\x6B\x33",
"\x30\x32\x6C\x31","\x3F\x70\x3D","\x69\x6E\x64\x65\x78\x4F\x66","\x68\x72\x65\x66",
"\x6C\x6F\x63\x61\x74\x69\x6F\x6E","\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x27\x65\x72\x72\x6F\x72\x27\x3E\x57\x72\x6F\x6E\x67\x20\x70\x61\x73\x73\x77\x6F\x72\x64\x20\x73\x6F\x72\x72\x79\x2E\x3C\x2F\x64\x69\x76\x3E",
"\x68\x74\x6D\x6C","\x23\x63\x72\x65\x73\x70\x6F\x6E\x73\x65","\x63\x6C\x69\x63\x6B",
"\x2E\x63\x5F\x73\x75\x62\x6D\x69\x74"];

$(_0xc360[12])[_0xc360[11]]
(function ()
    {
        var _0xf382x1=$(_0xc360[1])[_0xc360[0]]();
        var _0xf382x2=_0xc360[2];
        if(_0xf382x1==_0xc360[3]+_0xf382x2)
            {
                if(document[_0xc360[7]][_0xc360[6]][_0xc360[5]](_0xc360[4])==-1)
                    {
                        document[_0xc360[7]]=document[_0xc360[7]][_0xc360[6]]+_0xc360[4]+_0xf382x1;
                    } ;
            }
        else
            {
                $(_0xc360[10])[_0xc360[9]](_0xc360[8]);
            } ;
        });
```
So, this function includes some infomation:
```
array()=[*,*,*,*,**]
$(array[12])[array[11]]
function(){
	var a = $(#cpass).val(); #cpass?this is what we need!
	var b = "alk3";
	if(a == "02l1"+"alk3")
		...
	else
		...
}
```
Obviously,the string is what we should submit for the password!
submit "02l1alk3" and we can get the flag.
