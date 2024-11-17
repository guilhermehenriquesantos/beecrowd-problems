import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;

public class Main1164 {

    public static void main(String[] args) throws IOException {

        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> casosTeste = new ArrayList<>();
        int N = scanner.nextInt();

        if (verificarEntrada(N)) {
            for (int i = 0; i < N; i++) {
                int X = scanner.nextInt();
                casosTeste.add(X);
            }

            ehPerfeito(casosTeste);
        }

    }

    public static boolean verificarEntrada(int N) {
        if (N >= 1 && N <= 20) {
            return true;
        } else {
            return false;
        }
    }

    public static void ehPerfeito(ArrayList<Integer> casosTeste) {
        ArrayList<String> resultados = new ArrayList<>();

        for (int i = 0; i < casosTeste.size(); i++) {
            int contador = 1;
            int soma = 0;
            ArrayList<Integer> divisores = new ArrayList<>();

            while (contador < casosTeste.get(i)) {
                if (casosTeste.get(i) % contador == 0) {
                    divisores.add(contador);
                }
                contador++;
            }

            for (int divisor : divisores) {
                soma += divisor;
            }

            if (soma == casosTeste.get(i)){
                resultados.add(casosTeste.get(i) + " eh perfeito");
            }else{
                resultados.add(casosTeste.get(i) + " nao eh perfeito");
            }
        }

        for (String resultado : resultados) {
            System.out.println(resultado);
        }
    }

}