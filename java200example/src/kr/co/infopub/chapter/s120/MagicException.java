package kr.co.infopub.chapter.s120;

public class MagicException extends Exception {

    public MagicException() {
        this("이런 마방진은 생성 불가능"); // MagicException(String message) 생성자 함수를 호출한다
    }

    public MagicException(String message, Throwable cause) {
        super(message, cause);
    }

    public MagicException(String message) {
        super(message + " 형태의 마방진 생성 불가능");
    }

    public MagicException(Throwable cause) {
        super(cause);
    }
}
