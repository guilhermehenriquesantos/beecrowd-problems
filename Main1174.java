import java.io.IOException;
import java.util.Scanner;

public class Main1174 {

    public static void main(String[] args) throws IOException {

        Double A[] = new Double[100];
        Scanner s = new Scanner(System.in);

        for (int i = 0; i < 100; i++) {
            A[i] = s.nextDouble();
        }
        
        for (int i = 0; i < A.length; i++) {
            if (A[i]  <= 10) {
                System.out.println("A[" + i + "] = " + A[i]);
            }
        }

    }

}