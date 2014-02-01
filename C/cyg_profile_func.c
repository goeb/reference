


void __cyg_profile_func_enter (void *this_fn,
                                         void *call_site)
{
    printf("Entering function %x (call_site=%x)\n", this_fn, call_site);
}
void __cyg_profile_func_exit  (void *this_fn,
                                         void *call_site)
{
    printf("Exiting function %x (call_site=%x)\n", this_fn, call_site);
}

