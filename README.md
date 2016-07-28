## VK music utils

Console utils for work with VK music API

### VK music searcher
Interactive console application for search music in VK.
 
* Install the required modules:
```bash
$ pip install pyshorteners
$ pip intall vk
```

* Generate Vk and Google api token:
[Create an App Vk](https://new.vk.com/editapp?act=create)
[Create an App Google - urlshortener](https://console.developers.google.com/apis/api/urlshortener/)

* Set VK_TOKEN, GOOGLE_TOKEN vars in config.py

* Example of the usage:

```bash
$ ./vk_searcher.py

Input audio name: linkin park
1) Eminem &amp; Linkin Park	: Violent Rhythm
2) Linkin Park	: Powerless
3) Linkin Park	: New Devide
4) Linkin Park	: My December
5) Eminem &amp; Linkin Park	: Dead Space
6) linkin park	: numb (432 hz)

Menu:
-> Next page - [n]
-> Get info about audio - [1-6]
-> Exit menu - [q]

Input option: 4
----> Linkin Park : My December | http://goo.gl/txWrfS

```

### VK music searcher
Noninteractive console application for download music in VK.

* Set VK_TOKEN var in config.py

* Uage:

```bash
$ ./vk_downloader.py --help
usage: vk_downloader.py [-h] -i ID -o OUT [-j JOB]

Script for download audio from vk.com

optional arguments:
  -h, --help         show this help message and exit
  -i ID, --id ID     User id
  -o OUT, --out OUT  Output folder with audio files
  -j JOB, --job JOB  Setting maximum of threads
```

* Example of the usage:

```bash
$ ./vk_downloader.py -i 27537400 -o out -j 10
Count audio : 394
Please, wait...

[+] : Wolves At The Gate - Slaves - Download successful
[+] : Enter Shikari - Torn Apart - Download successful
[+] : Motionless In White - Death March - Download successful
...
```