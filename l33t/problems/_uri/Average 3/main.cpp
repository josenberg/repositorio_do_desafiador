#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
  double n1, n2, n3, n4;
  cin >> n1 >> n2 >> n3 >> n4;
  double avg = ((n1 * 2.0) + (n2 * 3.0) + (n3 * 4.0) + n4)/10.0;
  printf("Media: %.1f\n", avg);

  if (avg >= 7.0) {
      printf("Aluno aprovado.\n");
  } else if (avg <= 4.9) {
      printf("Aluno reprovado.\n");
  } else {
      printf("Aluno em exame.\n");
      double exam, new_avg;
      cin >> exam;

      new_avg = (exam + avg)/2.0;
      if (new_avg >= 4.9) {
          printf("Aluno aprovado.");
          printf("Media final: %.1f\n", new_avg);
      } else {
          printf("Aluno reprovado.\n");
          printf("Media final: %.1f\n", new_avg);
      }
  }

  return 0;
}
