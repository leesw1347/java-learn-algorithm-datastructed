package kr.co.infopub.chapter.s046;

public class BioRandom {
    public static void main(String[] args) {
        int start = 1;
        int range = 10;
        int a = 0, b = 0, c = 0;

        while (true) {
            a = (int) (range * Math.random() + start);
            b = (int) (range * Math.random() + start);
            c = (int) (range * Math.random() + start);

            if (a != b && b != c && c != a) {
                break;
            }
        }
        System.out.printf("%d\t%d\t%d\n", a, b, c);
    }
}