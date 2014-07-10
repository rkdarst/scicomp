int f(x) { y(x);  x+=1;  y(x); }  // f is fast, but calls y twice
int y(z) {                        // y is slow
  for ( ; z>=0 ; z-- ) {
    0;
} }

int main() {                      // main has a loop, calls f and y
  int i;
  for (i=0; i<10000; i++) {
    f(i);
    y(i);
} }
