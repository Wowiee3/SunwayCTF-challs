int __cdecl main(int _Argc,char **_Argv,char **_Env)

{
  byte bVar1;
  longlong lVar2;
  basic_ostream *pbVar3;
  byte *pbVar4;
  string input;
  int i;

  __main();
  std::__cxx11::basic_string<>::basic_string();
  std::operator<<((basic_ostream *)&_ZSt4cout,"Tell me the key: ");
  std::operator>>((basic_istream *)&_ZSt3cin,(basic_string *)&input);
  lVar2 = std::__cxx11::basic_string<>::length();
  if (lVar2 == 6) {
    pbVar3 = std::operator<<((basic_ostream *)&_ZSt4cout,"The flag probably is:");
    std::basic_ostream<>::operator<<((basic_ostream<> *)pbVar3,std::endl<>);
    for (i = 0; (uint)i < 0x20; i = i + 1) {
      bVar1 = flag[i];
      pbVar4 = (byte *)std::__cxx11::basic_string<>::operator[]((ulonglong)&input);
      std::operator<<((basic_ostream *)&_ZSt4cout,*pbVar4 ^ bVar1);
    }
  }
  else {
    pbVar3 = std::operator<<((basic_ostream *)&_ZSt4cout,"Wrong key.");
    std::basic_ostream<>::operator<<((basic_ostream<> *)pbVar3,std::endl<>);
  }
  std::__cxx11::basic_string<>::~basic_string((basic_string<> *)&input);
  return 0;
}
