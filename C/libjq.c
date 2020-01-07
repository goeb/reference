/* Experiment with libjq */

#include <stdio.h>
#include <string.h>
#include <jv.h>
#include <jq.h>

void test_dump()
{
	printf("test_dump\n");

	jv jnull = jv_null();
	jv_dump(jnull, 0);
	printf("\n");
}

void test_parse(const char *s)
{
	jv item;
	printf("-- test_parse: %s\n", s);
	jv_parser *parser = jv_parser_new(0);
	jv_parser_set_buf(parser, s, strlen(s), 1);

	printf("remaining=%d\n", jv_parser_remaining(parser));

	while (1) {
		item = jv_parser_next(parser);
		if (jv_is_valid(item)) {
			printf("jv_is_valid: item=");
			jv_dump(item, 0);
			printf("\n");
		} else if (jv_invalid_has_msg(jv_copy(item))) {
			printf("jv_invalid_has_msg\n");
			jv msg = jv_invalid_get_msg(item);
			jv_dump(msg, 0);
			printf("\n");
			printf("remaining=%d\n", jv_parser_remaining(parser));
			break;
		} else {
			printf("invalid\n");
			printf("remaining=%d\n", jv_parser_remaining(parser));
			break;
		}

		printf("remaining=%d\n", jv_parser_remaining(parser));
	}

}

int main()
{
	test_dump();
	test_parse("1234");
	test_parse("{\"a\":null");
	test_parse("{]ab");
	test_parse("{\"a\":null}");
	test_parse("[1, 2, 3]{\"a\":12345}");
}
