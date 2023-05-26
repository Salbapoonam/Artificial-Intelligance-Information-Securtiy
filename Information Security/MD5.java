import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5 {
    public static void main(String[] args) {
        String text = "example text";
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(text.getBytes());

            StringBuffer hexString = new StringBuffer();
            for (int i = 0; i < messageDigest.length; i++) {
                String hex = Integer.toHexString(0xff & messageDigest[i]);
                if(hex.length() == 1) hexString.append('0');
                hexString.append(hex);
            }
            System.out.println("Message Digest: " + hexString.toString());
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }
}
