
/* Compile with:
 * -------------
 * gcc test_check.c /usr/lib/i386-linux-gnu/libcheck.a -lm -lrt -pthread -lsubunit
 *
 *
 * Example output:
 * ---------------
 * Running suite(s): my_suite
 * 66%: Checks: 3, Failures: 1, Errors: 0
 * test_check.c:13:F:TC1:test_name_1:0: Assertion '1 == 0' failed: 1 == 1, 0 == 0
 * test_check.c:23:P:TC2:test_name_2:0: Passed
 * test_check.c:31:P:TC3:test_name_3:0: Passed
 *
 */
#include <stdlib.h>
#include <stdint.h>
#include <check.h>

START_TEST (test_name_1)
{
	  ck_assert_int_eq(1, 1);
	  ck_assert_int_eq(1, 1);
	  ck_assert_int_eq(1, 0);
	  ck_assert_int_eq(1, 1);
}
END_TEST


START_TEST (test_name_2)
{
	  ck_assert_int_eq(1, 1);
	  ck_assert_int_eq(1, 1);
	  ck_assert_int_eq(1, 1);
}
END_TEST

START_TEST (test_name_3)
{
	  ck_assert_int_eq(1, 1);
	  ck_assert_int_eq(1, 1);
	  ck_assert_int_eq(1, 1);
}
END_TEST

int main()
{
	Suite *s;
	SRunner *sr;
	TCase *tc_1, *tc_2, *tc_3;
	s = suite_create("my_suite");

	tc_1 = tcase_create("TC1");
	tcase_add_test(tc_1, test_name_1);
	suite_add_tcase(s, tc_1);

	tc_2 = tcase_create("TC2");
	tcase_add_test(tc_2, test_name_2);
	suite_add_tcase(s, tc_2);

	tc_3 = tcase_create("TC3");
	tcase_add_test(tc_3, test_name_3);
	suite_add_tcase(s, tc_3);

	sr = srunner_create(s);
	srunner_run_all(sr, CK_VERBOSE);
	int number_failed = srunner_ntests_failed(sr);
	srunner_free(sr);
	return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;

}

