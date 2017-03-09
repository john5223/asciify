ASCIIFY
=======

Image to ascii art API.

Assumes your python version is version 3.
Otherwise replace "python" with "python3" below.



Run API in debug mode
======================

Run api in python debug mode without installing use


	python -m asciify


OR


	python -m asciify.api




Install
========

To install application:


	pip3 install -r requirements.txt

	python setup.py install
	


Run API
========


To run the api:


	python asciify




Run tests
===========

To run tests either use tox:


	tox


or use pytest directly


	pytest test -s





Use cURL for sending images
============================



	curl -F file=@tests/images/earth.png 127.0.0.1:8000/art


Ascii art is returned in json format by default.


To return ascii art as text format use query parameter "format=text".
You can also specify scale, factor and/or max_height as query parameters


Examples:



	curl -F file=@tests/images/earth.png "127.0.0.1:8000/art?format=text&max_height=20&factor=2.5"


@@@@@@@@@@@@@.       i@@@@@@@@@@@@@
@@@@@@@@@                i@@@@@@@@@
@@@@@@s                    .&@@@@@@
@@@@@                  ..   .i@@@@@
@@@@.                 ..    .,,@@@@
@@@,                .       ..;;&@@
@@:..              ..,,.    ...,r@@
@s,,..            ..,,..   ...,,iG@
@::,,... ...     ..,,,    ...,,,ri@
@:::,,.............,,   ....,,,:;r@
@;:::,,,........,,,:  .....,,,:::;@
@;;:::,,,..::,,....,.....,,,:::::2@
@@::::::,,,,.;;;;;..i,:,,,,:::::,@@
@@i::;::::,,,,,,,:i,,rrrrr;::;:,@@@
@@@;,::;:::::::,,,,,irrssssrri.s@@@
@@@@@.,::;;::::::::;issssssi:.@@@@@
@@@@@&,.,,:::::;;;;:;:;i;:. sB&&@@@
@@@&&9#SG  ..,,,,,,,,,. . HGS#9&&@@
@@@@&&B9SGHM,         :hMHGS#9&&@@@
@@@@@@@&&&&BB999#####99BB&&&&@@@@@@



	curl -F file=@tests/images/earth.png "127.0.0.1:8000/art?format=text&max_height=50"


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@i52AAA5i@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@sXr,...       .......i33@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@3rr,...          ..........,,,,;33@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@Hri,....            ...........,,::,,:;s3&@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@3ii,,...             ...........,,,,::,,,:;iii39@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@5r;,,,,.               ..........,,,,;,,,::::;irrihM@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@2ii,:,,,..               .........,,:;;;i;,::::::;isssh3@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@Ai;,,.,,,..                ....,,:..:;;iiiiiii:::::;;isssXhM@@@@@@@@@@@@@@
@@@@@@@@@@@@Gsi:,,,........              ..,,:::::;;iiirrrrrrr::ii;;;risXA3&@@@@@@@@@@@@
@@@@@@@@@@@2ri::,,,...,,...         ... ..,,::::;;;iiirrrrssss;;sX;;irXXXAA3H@@@@@@@@@@@
@@@@@@@@@@Ari;::,,,,:,,...        .......,,:::::,,,,:irssssssi;;ii;iiirAXAA235@@@@@@@@@@
@@@@@@@@@Asi;;:::,:::,,....        .....,,,,:;;;;;;:,,:rssXXXi;;;;;iiiirXsA22A5@@@@@@@@@
@@@@@@@@AXri;;;::,,,,..,.....    ....,,,,,:,:;;;iiirir::rXXXXX;;;;iiiirrrrrX22A3@@@@@@@@
@@@@@@@2Xsrii;;:::,,,...,............,,,,:::;;;,irrrri::::isXs;;;iiiiirrrrss552h3@@@@@@@
@@@@@@2AXsrrii;;:::,,,...,,,.......,,,,,:::;:i:,iiisr;i:::;;;;;;iiiiirrrrsssX555hh@@@@@@
@@@@@22AXssrrii;;:::,,,,,,,,,,,,,,,,,,,:::,...,,rrssrsXss;;;;;;iiiiirrrrssssXX533hh@@@@@
@@@@M22AXssrriii;;;:::,,,::::::,,,,,:::::;:,::,,;sssXXXXAAAi;;iiiiirrrrrssssXXX23hh#@@@@
@@@@222AXXssrriii;;;:::::;i;;;:::::::::;;;;iiii;rssXXXXAAA22siiiiirrrrrssssXXXX233h3@@@@
@@@H222AAXXssrrriii;;;:::;iiii;;;;;;;;;;;iiirrrsrsXXXXAAAXsAXiiiirrrrrssssXXXXAA53hh9@@@
@@@222AAAAXXsssrriii;;;;;rrrriiiiii;;;;iiiirrrsssXXXXAAAs;;iiiiirrrrrssssXXXXAAA5hhhM@@@
@@@2222AAAAXXsssrrriii;;rrrrrrrriiiiiiiiiirsiissXXXXAAAXiiiiiiirrrrrssssXXXXAAAA3hhh3@@@
@@@22222AAAAXXXsssrrriiissrrrrrrrrrriiiiirrrsrXrXXAAAA2riiiiiirrrrrssssXXXXAAAAA5hhhh@@@
@@H52222AAAAAXXXXsssrrrrsssrrrrrrrrrrrrrrrrsrXXXXXAAA2siiiiirrrrrsssssXXXXXAAAA22hhhh9@@
@@M522222AAAAAXXXXssssrrAssssrrrrrrrrrrrrrssssXXAAAAAiiiiirrrrrrsssssXXXXAAAAA2223hhh9@@
@@M5522222AAAAXXXXXssssss2ssssssrrrrrrrsssssXXXAAAA2siiirrrrrrrsssssXXXXXAAAA22225hhh9@@
@@H55222222AAAAAXXXXXsssssXssssssssssssssXXXXAAA222XrrrrrrrrrsssssXXXXXXAAAA2222253hh9@@
@@@555222222AAAAAXXXXXssssAXXXssssssXXXXXXXAAAA22XrrrrrrrrrssssssXXXXXAAAAA2222222555@@@
@@@5555222222AAAAAAXXXXXsssAAAXXXXXXXXA52552XXX52ArrrrrrsssssssXXXXXXAAAAA22222222222@@@
@@@555552222222AAAAAXXXXXXss2AX2AAAAAAAsrrrrrrrX5ArrrssssssssXXXXXXAAAAA222222222222h@@@
@@@G255552222222AAAAAAXXXXXXXXsX222222Assssssss555AA5XssssXXXXXXXAAAAAA2222222252222@@@@
@@@@22255552222222AAAAAAXXXXXXXX2522225XsX225ssXXA533Ahhhh32XXXAAAAAA222222255522223@@@@
@@@@G222555522222222AAAAAAAXXXXXXA53555555555XsssXX2AXXAAXAAAAAAAAA22222222555222AA@@@@@
@@@@@22222555522222222AAAAAAAAXXXXXXX25533335555XXXXXXXXXAAAAAAAA22222222555522AAAM@@@@@
@@@@@@2A2225555222222222AAAAAAAAAAXXXXXXXAA23h33AXXXX5hhhhhhhhhh52535222555522AAAM@@@@@@
@@@@@@@AA2225555552222222222AAAAAAAAAAAAAAAAA2hh33333hhhhhhhhhhhhhhhh53553332AAX2@@@@@@@
@@@@@@@@AAA222555555222222222222AAAAAAAAAAAAAAA255533hhhhhhhhhMMMhhhhhhhhhh32XXA@@@@@@@@
@@@@@@@@@XAAA22255555552222222222222222AAAAAAAAA2223hhhhhhMMMMMMMMMMhhhhh35AXsA@@@@@@@@@
@@@@@@@@@@AXAAA2225555555552222222222222222222222233hhhhMMMMMMMMMMMMMhh352Xssh@@@@@@@@@@
@@@@@@@@@@@hsXXAA22225555555555222222222222222222333hhMMMMMMMMMMMMMhh3522Xsr@@@@@@@@@@@@
@@@@@@@@@@@@@ssXXAA2222255555555555555552222222553553hMMMMMMMMMMMMh352AAsrX@@@@@@@@@@@@@
@@@@@@@@@@@@@@3rssXXAA22222255555555555555555555555h5533hhMMMMhh352AXXsrr&&&&&@@@@@@@@@@
@@@@@@@@@@@&&&&&GrrssXXAAA22222225555555555555555555h22255333552AXXXrirH&&&&&&&&@@@@@@@@
@@@@@@@@@&&&&&&&&BSrrrssXXAAAA22222222222222222222222222AAAAXXsrisrirBBBBB&&&&&&&@@@@@@@
@@@@@@@@@&&&&&&BBBBB9sirrrsssXXXAAAAAAA22222222AAAAAAA2XssrrrirsriA9999BBBBB&&&&&&@@@@@@
@@@@@@@@&&&&&&&BBBBB999SriiirrrrssssXXXXXXXXXXXXXXsssArriiirriis##99999BBBBB&&&&&&&@@@@@
@@@@@@@@@&&&&&&&BBBBB9999##3iiiiiiirrrrrrrrrrrrrrrisii;isiir5####99999BBBBB&&&&&&&@@@@@@
@@@@@@@@@@@&&&&&&&&BBBBB99999###SAr;;;;;;;;;;;;;;;iiiX3SS#####99999BBBBB&&&&&&&&@@@@@@@@
@@@@@@@@@@@@@&&&&&&&&&&&BBBBB999999######SSSSSSSSS######999999BBBBB&&&&&&&&&&&@@@@@@@@@@
@@@@@@@@@@@@@@@@&@&&&&&&&&&&&&&&&BBBBBBBBBBBBBBBBBBBBBBBBB&&&&&&&&&&&&&&&@&@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@

