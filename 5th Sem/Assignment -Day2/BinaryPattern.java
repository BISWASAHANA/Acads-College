//Program to print pattern of 0's and 1's in java
class BinaryPattern {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        if (n < 1) {
            System.out.println("Invalid Input");
            return;
        }
        printPattern(n);
    }

    public static void printPattern(int rows) {
        int[][] pattern = new int[rows][];
        
        for (int i = 0; i < rows; i++) {
            pattern[i] = new int[i + 1];
            for (int j = 0; j < pattern[i].length; j++) {
                pattern[i][j] = j % 2;
            }
        }
        
        for (int[] row : pattern) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
