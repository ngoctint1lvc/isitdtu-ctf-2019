## IDA decompiler
```c
void __fastcall main(__int64 a1, char **a2, char **a3)
{
  char choice[8]; // [rsp+30h] [rbp+0h]

  sub_4008B1();
  input_name();
  while ( 1 )
  {
    show_menu();
    read_integer();
    switch ( (unsigned int)choice )
    {
      case 1u:
        add();
        break;
      case 2u:
        edit();
        break;
      case 3u:
        delete();
        break;
      case 4u:
        show_name();
        break;
      case 5u:
        exit(0);
        return;
      default:
        continue;
    }
  }
}

void add()
{
  unsigned __int8 *str; // ST08_8
  __int64 i; // [rsp+0h] [rbp-10h]
  int ia; // [rsp+0h] [rbp-10h]
  signed int size; // [rsp+4h] [rbp-Ch]

  LODWORD(i) = 0;
  while ( (signed int)i <= 20 )
  {
    if ( !pointer_list[(signed int)i] )
    {
      printf("Enter size: ", i);
      size = read_integer();
      if ( size <= 0 && size > 127 )
      {
        puts("Invalid size!");
        exit(0);
      }
      str = (unsigned __int8 *)malloc(size);
      printf("Enter data: ");
      read_input(str, size);
      pointer_list[ia] = str;
      puts("Success!");
      return;
    }
    LODWORD(i) = i + 1;
  }
}

int edit()
{
  unsigned __int8 *v0; // ST08_8
  __int64 v2; // [rsp+0h] [rbp-10h]
  int v3; // [rsp+0h] [rbp-10h]
  signed int v4; // [rsp+4h] [rbp-Ch]

  printf("Enter index: ");
  LODWORD(v2) = read_integer();
  if ( (signed int)v2 < 0 && (signed int)v2 > 20 )
  {
    puts("Invalid index!");
    exit(0);
  }
  if ( pointer_list[(signed int)v2] )
    free((void *)pointer_list[(signed int)v2]);
  printf("Enter size: ", v2);
  v4 = read_integer();
  if ( v4 <= 0 && v4 > 127 )
  {
    puts("Invalid size!");
    exit(0);
  }
  v0 = (unsigned __int8 *)malloc(v4);
  printf("Enter data: ");
  read_input(v0, v4);
  pointer_list[v3] = v0;
  return puts("Success!");
}

_QWORD *delete()
{
  _QWORD *result; // rax
  int v1; // [rsp+Ch] [rbp-4h]

  printf("Enter index: ");
  v1 = read_integer();
  if ( v1 < 0 && v1 > 20 )
  {
    puts("Invalid index!");
    exit(0);
  }
  if ( !pointer_list[v1] )
  {
    puts("Not found!");
    exit(0);
  }
  free((void *)pointer_list[v1]);
  result = pointer_list;
  pointer_list[v1] = 0LL;
  return result;
}

unsigned __int64 show_name()
{
  char buf[24]; // [rsp+0h] [rbp-20h]
  unsigned __int64 v2; // [rsp+18h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  printf("DO you want to edit: (Y/N)");
  read(0, buf, 8uLL);
  if ( buf[0] == 'Y' )
  {
    printf("Input name: ", buf);
    read_input((unsigned __int8 *)name, 256);
    printf("Name: %s\n", name);
  }
  if ( buf[0] == 'N' )
    printf("Name: %s\n", name);
  return __readfsqword(0x28u) ^ v2;
}
```