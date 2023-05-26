// Write a Java/C/C++/Python program to implement DES algorithm.
import java.util.Arrays;

public class DES {
    public static void main(String[] args) {
        // Input block of 64 bits
        byte[] inputBlock = {
            (byte)0x12, (byte)0x34, (byte)0x56, (byte)0x78,
            (byte)0x9a, (byte)0xbc, (byte)0xde, (byte)0xf0
        };

        // Initial permutation table
        int[] ipTable = {
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7
        };

        // Apply initial permutation to input block
        byte[] permutedBlock = new byte[8];
        for (int i = 0; i < ipTable.length; i++) {
            int bitPosition = 7 - i % 8;
            int bytePosition = i / 8;
            int inputBit = (inputBlock[ipTable[i] / 8] >> (7 - ipTable[i] % 8)) & 1;
            permutedBlock[bytePosition] |= inputBit << bitPosition;
        }

        System.out.println("Input block: " + Arrays.toString(inputBlock));
        System.out.println("Permuted block: " + Arrays.toString(permutedBlock));
    }
}

