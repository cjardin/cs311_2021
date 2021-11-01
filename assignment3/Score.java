

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