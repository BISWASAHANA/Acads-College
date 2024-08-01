class Palindrome{
	public static void main(String args[]){
		String s=args[0];
		int l=0;
		int h=s.length() - 1;
		while (l<=h){
			if(s.charAt(l)!=s.charAt(h)){
				System.out.println("It is not Palindrome");
				return;
			}
			l++;
			h--;
		}
		System.out.println("It is a Palindrome");
	}
}