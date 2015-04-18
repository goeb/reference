
import xml.dom.minidom

dom1 = xml.dom.minidom.parse('t.xml')

x = dom1.getElementsByTagName('document')[0]
y = x.getElementsByTagName('a')[0]
a = y.childNodes[0]
s=a.data


