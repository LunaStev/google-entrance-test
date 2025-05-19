bool isValid(char* s) {
    char st[100000];
    int top = -1;

    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];

        if (c == '(' || c == '[' || c == '{') {
            st[++top] = c;
        } else {
            if (top == -1) return false;
            char tc = st[top--];

            if((c == ')' && tc != '(') || (c == ']' && tc != '[') || (c == '}' && tc != '{')) {
                return false;
            }
        }
    }

    return top == -1;
}
