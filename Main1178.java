import java.io.IOException;
import java.util.Scanner;

public class Main1178 {
    public static void main (String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        Double X = sc.nextDouble();
        Double N[] = new Double[100];
        int contador = 0;

        N[0] = X;

        for (int i = 1; i < 100; i++){
            N[i] = N[i - 1]/2;
        }

        for (Double j : N) {
            System.out.printf("N["+contador+"] = %.4f\n", (j));
            contador++;
        }

    }
}
