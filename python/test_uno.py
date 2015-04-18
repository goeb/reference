
"""
This script connects to a soffice server and
create an ODT document.

The soffice server must be started by the command:
    soffice -accept="socket,host=localhost,port=8100;urp;StarOffice.ServerManager" -headless
"""

import uno
localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)
ctx = resolver.resolve("uno:socket,host=localhost,port=8100;urp;StarOffice.ComponentContext")
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
doc=desktop.loadComponentFromURL("private:factory/swriter", "_blank", 0, ())
text = doc.Text
cursor=text.createTextCursor()
text.insertString(cursor, "Hello World", 0)
doc.storeAsURL(uno.systemPathToFileUrl("/tmp/toto.odt"), ())
doc.dispose()
