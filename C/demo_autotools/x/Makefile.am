
bin_PROGRAMS = x
x_SOURCES = x.c
x_CPPFLAGS =
x_LDADD =

if WITH_CURL
x_SOURCES += x_curl.c
x_CPPFLAGS += @CURL_CFLAGS@ -DWITH_CURL
x_LDADD += @CURL_LIBS@
endif
