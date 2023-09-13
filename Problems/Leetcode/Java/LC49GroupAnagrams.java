import java.util.*;

/**
 * S49GroupAnagrams
 */
public class LC49GroupAnagrams {

    public static String getFrequencyString(String str) {
        int[] freq = new int[26];

        for (char c : str.toCharArray()) {
            freq[c - 'a'] += 1;
        }

        StringBuilder fs = new StringBuilder("");

        char c = 'a';

        for (int i : freq) {
            fs.append(c);
            fs.append(i);
            c++;
        }

        return fs.toString();
    }

    public static List<List<String>> groupAnagrams(String[] strs) {
        // List<List<String>>;
        if (strs.length == 0) {
            return new ArrayList<>();
        }

        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            String freqStr = getFrequencyString(str);

            if (map.containsKey(freqStr)) {
                map.get(freqStr).add(str);
            } else {
                List<String> strList = new ArrayList<>();
                strList.add(str);
                map.put(freqStr, strList);
            }
        }

        return new ArrayList<>(map.values());
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        // String s = scan.nextLine();
        System.out.print("Enter number of strings: ");
        int n = scan.nextInt();
        String[] arr = new String[n];

        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextLine();
        }
        scan.close();
        System.out.println(arr);

        System.out.println("" + groupAnagrams(arr));
    }
}