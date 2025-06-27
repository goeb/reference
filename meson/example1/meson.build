project('example1-project', 'c',
        version : '0.1',
        default_options : ['warning_level=3'])

conf_data = configuration_data()
conf_data.set('CONF_PATH', get_option('CONF_PATH'))
configure_file(input : 'src/config.h.in',
               output : 'config.h',
               configuration : conf_data)

openssldep = dependency('openssl')
exe = executable('example1',
                 'src/example1.c',
                 dependencies: openssldep,
                 install : true)

test('basic', exe)
test('basic error', exe, args: ['-x'], should_fail: true)

