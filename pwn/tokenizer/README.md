```
nc 165.22.57.24 32000
```

## Pseudo code
```
std::string input_string;
std::string input_delimiter;

char* sub_401261() {
    char dest[1024];

    std::cout << "please input string";
    std::getline(std::cin, input_string);
    const char* v0 = input_string.c_str();
    strncpy(dest, v0, 1024);
    std::cout << "string after truncated: " << dest << "\n";
    std::getline(std::cin, input_delimiter);
    return split_string(dest);
}

char* split_string(char* str) {
    char* stringp;
    stringp = str;
    std::cout << "Tokens:\n";
    const char* delim = input_delimiter.c_str();
    result = strsep(&stringp, delim);
    char* i = result;
    while(i) {
        std::cout << i << '\n';
        const char* v4 = input_delimiter.c_str();
        result = strsep(&stringp, v4);
        i = result;
    };
}
```

## Run the payload
```
for i in {1..20} do; python exploit.py
```