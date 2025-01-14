import java.util.ArrayList;
import java.util.Scanner;

public class Main1175 {
    public static void main(String[] args) {
        ArrayList<Integer> N = new ArrayList<Integer>();
        ArrayList<Integer> resultado = new ArrayList<Integer>();
        Scanner s = new Scanner(System.in);

        do {
            N.add(s.nextInt());
        } while (N.size() < 20);

        for (int i = N.size() - 1; i >= 0; i--) {
            resultado.add(N.get(i));
        }

        for (int j = 0; j < resultado.size(); j++) {
            System.out.println("N[" + j + "] = " + resultado.get(j));
        }
    }
}