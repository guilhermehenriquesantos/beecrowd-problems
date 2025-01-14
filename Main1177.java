import java.util.Scanner;

public class Main1177 {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        Integer T;
        Integer N[] = new Integer[1000];
        int i;

        T = sc.nextInt();
        i = 0;

        for (int j = 0; j < 1000; j++){
            if (i < T) {
                N[j] = i;
                System.out.println(String.format("N[%d] = %d", j, N[j]));
                i++;
            } else {
                i = 0;
                N[j] = i;
                System.out.println(String.format("N[%d] = %d", j, N[j]));
                i++;
            }
        }
    }
}