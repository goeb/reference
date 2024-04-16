
AC_INIT(demo_autotools, 1.0)

AM_INIT_AUTOMAKE

AC_PROG_LIBTOOL

AC_ARG_WITH([curl],
  [AS_HELP_STRING([--with-curl], [With curl])],
  [AC_MSG_NOTICE([>>>>>>>>>>> Using --with-curl=$with_curl])],
  [AC_MSG_NOTICE([>>>>>>>>>>> Not using --with/out-curl])],
)
AM_CONDITIONAL([WITH_CURL],[test x$with_curl = xyes])

if test x$with_curl = xyes; then
    PKG_CHECK_MODULES(CURL, libcurl)
fi

AC_OUTPUT(Makefile x/Makefile y/Makefile libzz/Makefile)
