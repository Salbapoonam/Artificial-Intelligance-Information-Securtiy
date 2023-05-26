import java.math.BigInteger;
import java.security.SecureRandom;

public class DiffieHellman {

    private static BigInteger generateKey(BigInteger p, BigInteger g, BigInteger private_key) {
        return g.modPow(private_key, p);
    }

    public static void main(String[] args) {
        // Shared prime number and primitive root modulo
        BigInteger p = new BigInteger("23");
        BigInteger g = new BigInteger("5");

        // Private keys for both parties
        SecureRandom random = new SecureRandom();
        BigInteger private_key_A = new BigInteger(20, random);
        BigInteger private_key_B = new BigInteger(20, random);

        // Generate public keys
        BigInteger public_key_A = generateKey(p, g, private_key_A);
        BigInteger public_key_B = generateKey(p, g, private_key_B);

        // Compute shared secret keys
        BigInteger shared_secret_key_A = generateKey(p, public_key_B, private_key_A);
        BigInteger shared_secret_key_B = generateKey(p, public_key_A, private_key_B);

        // Both parties should have the same shared secret key
        System.out.println("Shared secret key for party A: " + shared_secret_key_A);
        System.out.println("Shared secret key for party B: " + shared_secret_key_B);
    }
}
