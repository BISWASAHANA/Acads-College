//Program to arrange a set of integer in ascending order where input will be taken through command line
class SortInt{
	public static void main(String args[]){
		if (args.length==0){
			System.out.println("Invalid input");
			return;
		}
		int[] numbers = new int[args.length];
            	for (int i = 0; i < args.length; i++) {
                	numbers[i] = Integer.parseInt(args[i]);
            	}

            	// Implementing bubble sort to sort the array in ascending order
            	for (int i = 0; i < numbers.length - 1; i++) {
                	for (int j = 0; j < numbers.length - i - 1; j++) {
                    		if (numbers[j] > numbers[j + 1]) {
                        	int temp = numbers[j];
                        	numbers[j] = numbers[j + 1];
                        	numbers[j + 1] = temp;
                    		}
                	}
            	}
		
            	System.out.print("Sorted numbers in ascending order: ");
            	for (int number : numbers) {
                	System.out.print(number + " ");
            	}
            }
}
       