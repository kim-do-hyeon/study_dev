import java.util.Scanner;
public class java_1002{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        int x1, y1, r1, x2, y2, r2;
        for(int i = 0; i < T; i++)
        {
            x1 = scanner.nextInt();
            y1 = scanner.nextInt();
            r1 = scanner.nextInt();
            x2 = scanner.nextInt();
            y2 = scanner.nextInt();
            r2 = scanner.nextInt();
            int distance = (int)Math.sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
            if (distance == 0 && r1 == r2)
            {
                System.out.print(-1);
            }
            else if(Math.abs(r1 - r2) == distance || r1 + r2 == distance)
            {
                System.out.print(1);
            }
            else if(Math.abs(r1 - r2) < distance && distance < (r1 + r2))
            {
                System.out.print(2);
            }
            else{
                System.out.print(0);
            }
        }
        scanner.close();
    }
}