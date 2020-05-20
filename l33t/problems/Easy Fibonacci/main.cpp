#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int F[500006];
  F[0] = 0;
  F[1] = 1;
  for (int i = 2; i < 500006; i++) {
    F[i] = (F[i-1]+ F[i-2]) % 100000007;
  }
  int t;
  scanf("%d", &t);
  while (t--) {
    int n;
    scanf("%d", &n);
    printf("%d\n", F[n]);
  }

  return 0;
}
