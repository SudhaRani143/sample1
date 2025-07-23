public class strong{

    // Function to calculate factorial of a number
    public static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            int fact = 1;
            for (int i = 2; i <= n; i++) {
                fact *= i;
            }
            return fact;
        }
    }

    // Function to check if a number is strong
    public static boolean isStrongNumber(int num) {
        int originalNum = num;
        int sumOfFactorials = 0;
        int tempNum = num;

        while (tempNum > 0) {
            int digit = tempNum % 10;
            sumOfFactorials += factorial(digit);
            tempNum /= 10;
        }

        return sumOfFactorials == originalNum;
    }

    public static void main(String[] args) {
        System.out.println("Strong numbers from 1 to 5000 are:");
        for (int i = 1; i <= 5000; i++) {
            if (isStrongNumber(i)) {
                System.out.println(i);
            }
        }
    }
}