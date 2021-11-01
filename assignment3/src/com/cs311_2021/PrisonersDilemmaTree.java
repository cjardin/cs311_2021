package com.cs311_2021;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.stream.IntStream;
import java.util.stream.Stream;


public class PrisonersDilemmaTree {



    // Root of Binary Tree
    Move zero;

    // Constructors
    PrisonersDilemmaTree(String move) {
        zero = new Move(move);
    }

    PrisonersDilemmaTree() {
        zero = null;
    }




    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String opponentsMove = input.readLine();
        Move moveB = new Move(opponentsMove);
        Move moveA = new Move();
        String myMove = moveA.getMove();


        PrisonersDilemmaTree tree = new PrisonersDilemmaTree();
        // for history
        Stack<String> moveStackA = new Stack<>();
        Stack<String> moveStackB = new Stack<>();
        moveStackA.push(opponentsMove);
        moveStackB.push(myMove);
        System.out.print(myMove);

        //create root
        tree.zero = new Move("zero");
        //create nodes
        tree.zero.confess = new Move("confess");
        tree.zero.silent = new Move("silent");
        tree.zero.confess.confess = new Move("RR");
        tree.zero.confess.silent = new Move("ST");
        tree.zero.silent.confess = new Move("TS");
        tree.zero.silent.silent = new Move("PP");

        //tree traversal for score keeping & history
        /*public Stream<Move> traverseTree(moveA, moveB);
        Move traverse = tree.findNode(moveA, moveB);*/

        /*if (opponentsMove.compareTo(myMove) == 0) {
            moveStackA.push()
        }*/

        IntStream.rangeClosed(0, 100).mapToObj(j -> moveStackB.pop()).forEach(System.out::println);

        /*
        for (int i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }

         */

    }

   /* public Move findNode(Move moveA, Move moveB) {
         PrisonersDilemmaTree(moveA, moveB);
    }*/
}

