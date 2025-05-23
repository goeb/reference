AC_INIT([example-1], [1.0], [fhoerni@free.fr])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AC_PROG_CC
AC_CONFIG_HEADERS([src/config.h])
AC_CONFIG_FILES([Makefile src/Makefile])

AC_ARG_WITH([var-a],
			[AS_HELP_STRING([--with-var-a=VAR_A], [use this value for VAR_A])],
			AC_DEFINE_UNQUOTED([VAR_A], ["$withval"], [Define VAR_A]),
			AC_DEFINE([VAR_A], ["default value of var-a"], [Define VAR_A])
			)

AC_OUTPUT
