public class FindTheOddOccouringNum {
    public static void main(String[] args) {
        int arr[] = { 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6 };

        int oddoccouring = 0;
        for (int i = 0; i < arr.length; i++) {
            oddoccouring = oddoccouring ^ arr[i];
        }

        System.out.println(oddoccouring);
    }
}

// Theory
// n ^ n = 0
// 0 xor n = n     | n != 0
// a^(b^c) = (a^b)^c
// therefore all duplicate numbers cancel out each others and the only one number without any pair is left