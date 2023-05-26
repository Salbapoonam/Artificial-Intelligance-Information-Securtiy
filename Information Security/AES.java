import java.security.Key;
import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class AES {
    private static final String ALGORITHM = "AES";
    private static final String KEY = "mysecretkey12345";

    public static void main(String[] args) {
        String originalString = "Hello, world!";
        System.out.println("Original string: " + originalString);

        try {
            // Encrypt the string
            String encryptedString = encrypt(originalString, KEY);
            System.out.println("Encrypted string: " + encryptedString);

            // Decrypt the string
            String decryptedString = decrypt(encryptedString, KEY);
            System.out.println("Decrypted string: " + decryptedString);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    public static String encrypt(String value, String key) throws Exception {
        Key aesKey = new SecretKeySpec(key.getBytes(), ALGORITHM);
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, aesKey);
        byte[] encrypted = cipher.doFinal(value.getBytes());
        return Base64.getEncoder().encodeToString(encrypted);
    }

    public static String decrypt(String value, String key) throws Exception {
        Key aesKey = new SecretKeySpec(key.getBytes(), ALGORITHM);
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.DECRYPT_MODE, aesKey);
        byte[] decrypted = cipher.doFinal(Base64.getDecoder().decode(value));
        return new String(decrypted);
    }
}
