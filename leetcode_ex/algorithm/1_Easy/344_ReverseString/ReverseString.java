

public class ReverseString {
	public static void reverseString(char[] str) {
		for (int i = 0; i < str.length/2; i++) {
			char temp = str[i];
			str[i] = str[str.length-1-i];
			str[str.length-1-i] = temp;
		}
	}

	public static void main(String [] args) {
		String str = "hello";
		char[] input = str.toCharArray();

		System.out.println(input);
		reverseString(input);
		System.out.println(input);
	}
}
