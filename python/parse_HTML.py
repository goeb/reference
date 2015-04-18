import sys

# simple parsing for HTML files
html = file(sys.argv[1]).read()

in_tag = False
skip_blank = True
select = None

for c in html:
	if skip_blank and c in ' \t': continue
	if c == '<':
		skip_blank = True
		select = 'TAG'
		tag_name = ''
		continue

	elif select == 'TAG':
		skip_blank = False
		if c == '>':
			select = None
			print 'tag:', tag_name
		elif c in ' \t':
			# end of the tag
			print 'tag:', tag_name
			select = 'ATTRIBUTE'
			attribute_name = ''
			skip_blank = True
		else:
			tag_name = tag_name + c

	elif select == 'ATTRIBUTE':
		skip_blank = False
		if c in ' \t=':
			print 'attribute_name=', attribute_name
			attribute_value = ''
			separators = ''
			skip_blank = True

			if c == '=': select = 'VALUE'
			else: select = 'EQUAL'
		elif c == '>':
			if attribute_name != '':
				print 'attribute_name=', attribute_name
			select = None
		else:
			attribute_name = attribute_name + c

	elif select == 'EQUAL':
		if c == '=':
			select = 'VALUE'
		elif c == '>':
			print 'attribute_name=', attribute_name
			select = None
		else:
			select = 'ATTRIBUTE'
			attribute_name = c

	elif select == 'VALUE':
		# reading the value
		skip_blank = False
		if separators == '':
			if c in '\'"':
				separators = c
				continue
			else: separators = ' \t'

		if c == '>':
			print 'attribute_value=', attribute_value
			select = None
		elif c in separators:
			# end
			print 'attribute_value=', attribute_value
			select = 'ATTRIBUTE'
			skip_blank = True
			attribute_name = ''
		else:
			attribute_value = attribute_value + c

