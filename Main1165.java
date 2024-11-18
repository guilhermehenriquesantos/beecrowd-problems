import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main1165 {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        ArrayList<Integer> numeros = new ArrayList<>();
        ArrayList<String> resultados = new ArrayList<>();
        int numero = 0;

        try {
            if (verificarEntrada(N)) {
                for (int i = 0; i < N; i++) {
                    numero = scanner.nextInt();
                    numeros.add(numero);
                }

                resultados = verificarPrimo(numeros);

                for (String resultado : resultados) {
                    System.out.println(resultado);
                }
            }
        } catch (Exception e) {
            System.exit(0);
        }

    }

    public static boolean verificarEntrada(int N) {
        return (1 <= N && N <= 100) ? true : false;
    }

    public static ArrayList<String> verificarPrimo(ArrayList<Integer> numeros) {
        ArrayList<String> resultado = new ArrayList<>();
        int contador = 0;

        for (int numero : numeros) {
            for (int i = 1; i <= numero; i++) {
                if (numero % i == 0) {
                    contador++;
                }
            }

            resultado.add((contador == 2) ? numero + " eh primo" : numero + " nao eh primo");
            contador = 0;
        }

        return resultado;
    }
}