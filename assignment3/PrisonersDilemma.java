import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class PrisonersDilemma {

    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String opponentsMove = input.readLine();
        Move moveB = new Move(opponentsMove);

        PrisonersDilemmaTree tree = new PrisonersDilemmaTree();
        Stack<String> moveStackA = new Stack<>();
        Stack<String> moveStackB = new Stack<>();
        moveStackA.push(opponentsMove);

        /*create root*/
        tree.zero = new Move("zero");
        //create nodes
        tree.zero.confess = new Move("confess");
        tree.zero.silent = new Move("silent");
        tree.zero.confess.confess = new Move("RR");
        tree.zero.confess.silent = new Move("ST");
        tree.zero.silent.confess = new Move("TS");
        tree.zero.silent.silent = new Move("PP");
 IntStream.rangeClosed(0, 100).mapToObj(j -> moveStackB.pop()).forEach(System.out::println);

public class Move {

    String move; //String move
    Move confess, silent;

    public Move(String decision) {
        move = decision;
        confess = silent = null;
    }
LinkedList<String> historyA = new LinkedList<>();
    LinkedList<String> historyB = new LinkedList<>();
    public Move() {
    }

    public void clear() {
        for (LinkedList<String> prevMoves : Arrays.asList(historyA, historyB)) {
            prevMoves.clear();
        }
    }

    public String getMove() {
        return move;
    }

    public void setMove(String move) {
        this.move = move;
    }

    public int getI() {
        return i;
    }

    public void setI(int i) {
        this.i = i;
    }

    public void clearHistory() {
        historyA.clear();
        historyB.clear();
    }

    public void setPayoff(int totalScore) {
        years += totalScore;
    }

    public String move(int turn) {
        return "";
    }

    public void addToHistory(String moveA, String moveB) {
        historyA.add(i, moveA);
        historyB.add(i, moveB);
    }
}
public class Score {
    Payoff payoff = new Payoff();
    int scoreA = 0;
    int scoreB = 0;
    int pointsA, pointsB;


    public Score() {

    }
    public Score(int payoffA, int payoffB) {

        scoreA = payoffA;
        scoreB = payoffB;
    }


    public int getPointsA() {
        return pointsA = payoff.getPointsA();
    }

    public void setPointsA(int pointsA) {
        this.pointsA = pointsA;
    }

    public int getPointsB() {
        return pointsB = payoff.getPointsB();
    }

    public void setPointsB(int pointsB) {
        this.pointsB = pointsB;
    }

    public int getScoreA() {
        return scoreA;
    }

    public void setScoreA(int pointsA) {
        scoreA += pointsA;
    }

    public int getScoreB() {
        return scoreB;
    }

    public void setScoreB(int pointsB) {
        scoreB += pointsB;
    }


    @Override
    public String toString() {
        return scoreA + ", " + scoreB;
    }
}
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
