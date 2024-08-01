//Program to arrange a set of strings in alphabetical order
class SortStr{
	public static void main(String args[]){
		for(int i=0; i<args.length; i++){
			args[i]=args[i];
		}
		for (int i = 0; i < args.length - 1; i++) {
			for(int j=0; j< args.length - i - 1; j++){
				if(args[j].compareToIgnoreCase(args[j+1])>0){
					String temp = args[j];
					args[j] = args[j+1];
					args[j+1] = temp;
				}
			}
		}
		System.out.println("Cities in Sorted Order:");
		for (String i : args) {
			System.out.print(i + " ");
        	}
	}
}