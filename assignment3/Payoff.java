

public class Payoff {
    int R = 5;
    int S = 0;
    int T = 20;
    int P = 1;
    char payoffA, payoffB;
    int pointsA, pointsB;
    String pA, pB, payoff;

    public Payoff() {

    }
    public Payoff(String points) {
        payoff = points;
    }

    public int getPointsA() {
        return pointsA;
    }

    public void setPointsA(String payoff) {
        payoffA = payoff.charAt(0);
        switch (payoffA) {
            case 'R' -> pointsA = R;
            case 'S' -> pointsA = S;
            case 'T' -> pointsA = T;
            case 'P' -> pointsA = P;
        }
    }

    public int getPointsB() {
        return pointsB;
    }

    public void setPointsB(String payoff) {
        payoffB = payoff.charAt(1);
        switch (payoffB) {
            case 'R' -> pointsB = R;
            case 'S' -> pointsB = S;
            case 'T' -> pointsB = T;
            case 'P' -> pointsB = P;
        }
    }
}
