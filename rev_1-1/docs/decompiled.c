undefined8 main(void)

{
  size_t sVar1;
  long in_FS_OFFSET;
  int local_90;
  int local_8c;
  char local_88 [104];
  long local_20;

  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  puts("You\'ll need a valid key to get this flag.");
  puts("What\'s your key?");
  fflush(stdout);
  __isoc99_scanf(&DAT_00102043,local_88);
  local_90 = 0;
  local_8c = 0;
  while( true ) {
    sVar1 = strlen(local_88);
    if (sVar1 <= (ulong)(long)local_8c) break;
    local_90 = local_90 + local_88[local_8c];
    local_8c = local_8c + 1;
  }
  if (local_90 == 0x197) {
    puts("Valid key!");
    puts("Flag: <SEND TO SERVER TO GET THE FLAG.>");
  }
  else {
    puts("Wrong key. Exiting...");
  }
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}