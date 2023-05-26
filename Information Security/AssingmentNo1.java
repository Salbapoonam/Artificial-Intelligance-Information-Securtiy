public class AssingmentNo1 {
    public static void main(String[] args) {
        String str = "Hello World9";
        char[] chars = str.toCharArray();

        System.out.println("Original string: " + str);

        // Perform XOR with 127
        for (int i = 0; i < chars.length; i++) {
            chars[i] = (char) (chars[i] ^ 127);
        }

        String xorResult = new String(chars);
        System.out.println("XOR with 127: " + xorResult);

        // Perform AND with 127
        for (int i = 0; i < chars.length; i++) {
            chars[i] = (char) (chars[i] & 127);
        }

        String andResult = new String(chars);
        System.out.println("AND with 127: " + andResult);
    }
}
