package kr.co.infopub.chapter.s035;

// 삼항(?:) 연산자
public class EvenOddTriCondition {
    public static void main(String[] args) {
        int temp = 99;
        // temp % 2 == 1 은 홀수를 의미한다
        // temp % 2 == 0 은 짝수를 의미한다
        temp = (temp % 2 == 1) ? temp * 3 + 1 : temp / 2;
        System.out.printf("계산 후 = %d\n", temp);
    }
}