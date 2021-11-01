package com.cs311_2021;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Stack;

public class Move {

    String move; //String move
    Move confess, silent;

    public Move(String decision) {
        move = decision;
        confess = silent = null;
    }


    int years = 0;
    int i = 0;

    Stack<String> historyA = new Stack<>();
    Stack<String> historyB = new Stack<>();
    /*LinkedList<String> historyA = new LinkedList<>();
    LinkedList<String> historyB = new LinkedList<>();*/




    public Move() {
    }

    public void clear() {
        for (Stack<String> prevMoves : Arrays.asList(historyA, historyB)) {
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

    //TODO: Sorting
    public String toString() {
        return move;
    }

}
