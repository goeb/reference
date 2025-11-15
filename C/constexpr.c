/*
 * This progam shows how const and constexpr differ in C23.
 * Tested with gcc version 13.3.0.
 *
 * 1. gcc constexpr.c
 *     warning: overflow in conversion from ‘long unsigned int’ to ‘int32_t’
 *     ./a.out
 *     bignum_const value: 0x0 (expected 0x100000000)
 *
 * 2. gcc constexpr.c -DUSE_CONSTEXPR
 *     error: unknown type name ‘constexpr’
 *
 * 3. gcc constexpr.c -DUSE_CONSTEXPR -std=c2x
 *     error: ‘constexpr’ initializer not representable in type of object
 */
#include <stdint.h>
#include <stdio.h>

// A value that is too large to fit into a 32-bit integer
#define LARGE_VALUE 0x100000000UL
// max that can fit: 0xFFFFFFFFUL

#if USE_CONSTEXPR
// In C23, a constant expression must be exactly representable in its type.
constexpr int32_t bignum_constexpr = LARGE_VALUE; 
#endif

// Compiles successfully (value will likely wrap/truncate)
const int32_t bignum_const = LARGE_VALUE; 

int main(void) {
    printf("bignum_const value: 0x%x (expected 0x%lx)\n", bignum_const, LARGE_VALUE);
    return 0;
}
