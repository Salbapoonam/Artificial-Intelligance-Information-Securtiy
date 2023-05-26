
// Write a Java/C/C++/Python program to perform encryption and
//  decryption using the method of the method of Transposition technique.


public class AssingmentNo2 {
    
    // Encryption function
    public static String encrypt(String plaintext, int key) {
        String ciphertext = "";
        char[][] transpositionGrid = new char[key][plaintext.length()/key+1];
        int index = 0;
        
        // Fill the transposition grid column by column
        for(int j = 0; j < transpositionGrid[0].length; j++) {
            for(int i = 0; i < key && index < plaintext.length(); i++) {
                transpositionGrid[i][j] = plaintext.charAt(index++);
            }
        }
        
        // Read the ciphertext row by row
        for(int i = 0; i < key; i++) {
            for(int j = 0; j < transpositionGrid[0].length; j++) {
                if(transpositionGrid[i][j] != '\u0000') {
                    ciphertext += transpositionGrid[i][j];
                }
            }
        }
        return ciphertext;
    }
    
    // Decryption function
    public static String decrypt(String ciphertext, int key) {
        String plaintext = "";
        char[][] transpositionGrid = new char[key][ciphertext.length()/key+1];
        int index = 0;
        
        // Fill the transposition grid row by row
        for(int i = 0; i < key; i++) {
            for(int j = 0; j < transpositionGrid[0].length && index < ciphertext.length(); j++) {
                transpositionGrid[i][j] = ciphertext.charAt(index++);
            }
        }
        
        // Read the plaintext column by column
        for(int j = 0; j < transpositionGrid[0].length; j++) {
            for(int i = 0; i < key; i++) {
                if(transpositionGrid[i][j] != '\u0000') {
                    plaintext += transpositionGrid[i][j];
                }
            }
        }
        return plaintext;
    }
    
    // Main function to test the program
    public static void main(String[] args) {
        String plaintext = "Hello World";
        int key = 4;
        
        System.out.println("Plaintext: " + plaintext);
        
        // Encrypt the plaintext
        String ciphertext = encrypt(plaintext, key);
        System.out.println("Ciphertext: " + ciphertext);
        
        // Decrypt the ciphertext
        String decryptedText = decrypt(ciphertext, key);
        System.out.println("Decrypted text: " + decryptedText);
    }
}
