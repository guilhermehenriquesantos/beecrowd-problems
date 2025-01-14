import java.util.Scanner;

public class Main1172 {
    public static void main(String[] agrs) throws Exception{
        int[] X = new int[10];
        Scanner s = new Scanner(System.in);

        for (int i=0; i < X.length; i++) {
            X[i]= s.nextInt();
        }

        for (int i=0; i< X.length; i++) {
            if (X[i] <= 0) {
                X[i] = 1;
            }
            System.out.println("X[" +i+ "] = " + X[i]);
        }
    }
}
