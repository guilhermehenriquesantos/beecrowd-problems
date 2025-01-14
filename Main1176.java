import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main1176 {

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        Integer sequencia = 0;

        Integer quantidade_casos = sc.nextInt();

        for (int i = 0; i < quantidade_casos; i++) {
            sequencia = sc.nextInt();

            System.out.println("Fib(" + sequencia + ") = " + calculaFibonacci(sequencia));
        }

    }

    public static Long calculaFibonacci(Integer sequencia) {
        ArrayList<Long> sequencia_fibonacci = new ArrayList<Long>();
        Long anterior = 0L;
        Long atual = 0L;

        if (sequencia == 0) {
            return atual;
        } else {
            for (long i = 0; i <= sequencia; i++) {
                if (i <= 1) {
                    sequencia_fibonacci.add(i);
                } else {
                    anterior = sequencia_fibonacci.get(1);
                    atual = sequencia_fibonacci.get(0) + sequencia_fibonacci.get(1);

                    sequencia_fibonacci.set(0, anterior);
                    sequencia_fibonacci.set(1, atual);
                }
            }

            return sequencia_fibonacci.get(1);
        }

    }

}
