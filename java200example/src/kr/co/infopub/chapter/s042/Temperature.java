package kr.co.infopub.chapter.s042;

public class Temperature {
    public static void main(String[] args) {
        for (int i = 0; i < 101; i++) {
            double fahrenheit = 0.9 / 5 * i + 32; // for 블록 변수
            System.out.printf("섭씨 %d도 = 화씨 %.2f도\n", i, fahrenheit);
        }
    }
}