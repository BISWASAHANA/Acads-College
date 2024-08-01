//program to print a star pattern in Java
class StarPattern {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        if (n < 1) {
            System.out.println("Invalid Input!");
            return;
        }
        printPattern(n);
    }

    public static void printPattern(int rows) {
        char[][] pattern = new char[rows][];
        
        for (int i = 0; i < rows; i++) {
            pattern[i] = new char[i + 1];
            for (int j = 0; j < pattern[i].length; j++) {
                pattern[i][j] = '*';
            }
        }
        
        for (char[] row : pattern) {
            for (char i : row) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }
}