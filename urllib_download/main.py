from urllib.request import urlretrieve
from os import getcwd


#download image
url='http://www.umitkoc.com/images/5884c156-4bbb-43be-b968-6f0a852932c7.jpg'
name='/profil.png'
path=getcwd()+'/urllib_download'
path+=name
urlretrieve(url,path)
