void _init()
{
    if (__gmon_start__ != 0)
        __gmon_start__();
}

int64_t sub_1020()
{
    int64_t var_8 = 0;
    /* jump -> nullptr */
}

int64_t sub_1030()
{
    int64_t var_8 = 0;
    /* tailcall */
    return sub_1020();
}

int64_t sub_1040()
{
    int64_t var_8 = 1;
    /* tailcall */
    return sub_1020();
}

int64_t sub_1050()
{
    int64_t var_8 = 2;
    /* tailcall */
    return sub_1020();
}

int64_t sub_1060()
{
    int64_t var_8 = 3;
    /* tailcall */
    return sub_1020();
}

int64_t sub_1070()
{
    int64_t var_8 = 4;
    /* tailcall */
    return sub_1020();
}

void __cxa_finalize(void* d)
{
    /* tailcall */
    return __cxa_finalize(d);
}

int32_t puts(char const* str)
{
    /* tailcall */
    return puts(str);
}

uint64_t strlen(char const* arg1)
{
    /* tailcall */
    return strlen(arg1);
}

void __stack_chk_fail() __noreturn
{
    /* tailcall */
    return __stack_chk_fail();
}

int32_t printf(char const* format, ...)
{
    /* tailcall */
    return printf();
}

int32_t __isoc99_scanf(char const* format, ...)
{
    /* tailcall */
    return __isoc99_scanf();
}

void _start(int64_t arg1, int64_t arg2, void (* arg3)()) __noreturn
{
    int64_t stack_end_1;
    int64_t stack_end = stack_end_1;
    __libc_start_main(main, __return_addr, &ubp_av, nullptr, nullptr, arg3, &stack_end);
    /* no return */
}

void deregister_tm_clones()
{
    return;
}

void register_tm_clones()
{
    return;
}

void __do_global_dtors_aux()
{
    if (__TMC_END__ != 0)
        return;

    if (__cxa_finalize != 0)
        __cxa_finalize(__dso_handle);

    deregister_tm_clones();
    __TMC_END__ = 1;
}

void frame_dummy()
{
    /* tailcall */
    return register_tm_clones();
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    int64_t var_68;
    __builtin_strcpy(&var_68, "ineedscissors61");
    puts("So? What's the password?");
    void var_58;
    __isoc99_scanf(&data_2021, &var_58);
    int32_t var_74 = 0;

    while (true)
    {
        if (var_74 >= strlen(&var_58))
        {
            puts("Your password is correct!");
            void* const var_70_1 = "https://youtu.be/68mbFvenlaQ?si=…";
            break;
        }

        if (*(&var_58 + var_74) != *(&var_68 + var_74))
        {
            printf("Wrong password! Exiting..");
            break;
        }

        var_74 += 1;
    }

    *(fsbase + 0x28);

    if (rax == *(fsbase + 0x28))
        return 0;

    __stack_chk_fail();
    /* no return */
}

int64_t _fini() __pure
{
    return;
}

