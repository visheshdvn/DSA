package tmp;

import java.lang.reflect.Array;
import java.util.*;

public class Test {
    public static void main(String[] args) {
        List<List<Integer>> l = new ArrayList<>();

        List<Integer> abc = new ArrayList<>();

        abc.add(1);
        abc.add(2);
        abc.add(3);
        abc.add(4);
        abc.add(5);

        l.add(abc);

        System.out.print(l.get(0).get(0));

    }
}
