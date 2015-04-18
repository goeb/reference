

import gettext
gettext.bindtextdomain('roundup', '.')
gettext.textdomain('roundup')
_ = gettext.lgettext
#gettext.bind_textdomain_codeset('roundup', 'utf-8')
# ...

print _('no such item "%(designator)s"') % { 'designator' : 'xxx' }

print "gettext.bind_textdomain_codeset=", gettext.bind_textdomain_codeset('roundup')

print "gettext.GNUTranslations=", gettext.GNUTranslations
