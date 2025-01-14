import java.util.Scanner;

public class Main1173 {
    public static void main (String[] agrs) {
        Scanner scanner = new Scanner(System.in);
        int[] N = new int[10];
        int numero;

        numero = scanner.nextInt();
        scanner.close();

        if (numero <= 50) {
            N[0] = numero;
            for (int i=1; i < 10; i++) {
                N[i] = N[i-1]*2;
            }

            for (int i=0; i < 10; i++) {
                System.out.println("N["+ i +"] = " + N[i]);
            }
        }

    }
}