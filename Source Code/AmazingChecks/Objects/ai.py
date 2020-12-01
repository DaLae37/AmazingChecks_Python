import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Objects.king import King
from Objects.queen import Queen
from Objects.rook import Rook
from Objects.bishop import Bishop
from Objects.knight import Knight
from Objects.pawn import Pawn

class AI() :
    def __init__(self, isWhite) :
        self.isWhite = isWhite
        self.isGameOver = False
        self.pieces = list()

    def makePieces(self) :
        piecesLane = 0
        if self.isWhite :
            piecesLane = 7
            
        self.pieces.append(King(self.isWhite))
        self.pieces.append(Queen(self.isWhite))
        self.pieces.append(Rook(self.isWhite, 0, piecesLane))
        self.pieces.append(Rook(self.isWhite, 7, piecesLane))
        self.pieces.append(Bishop(self.isWhite, 1, piecesLane))
        self.pieces.append(Bishop(self.isWhite, 6, piecesLane))
        self.pieces.append(Knight(self.isWhite, 2, piecesLane))
        self.pieces.append(Knight(self.isWhite, 5, piecesLane))

        if self.isWhite :
            piecesLane = 6
        else :
            piecesLane = 1

        for i in range(8) :
            self.pieces.append(Pawn(self.isWhite, i, piecesLane))

    def copyPieces(self, pieces) :
        pi = list()
        for pc in pieces :
            if isinstance(pc, King) :
                pi.append(King(pc.getIsWhite()))
            elif isinstance(pc, Queen) :
                pi.append(Queen(pc.getIsWhite()))
            elif isinstance(pc, Rook) :
                pi.append(Rook(pc.getIsWhite(), 0, 0))
            elif isinstance(pc, Bishop) :
                pi.append(Bishop(pc.getIsWhite(), 0, 0))
            elif isinstance(pc, Bishop) :
                pi.append(Knight(pc.getIsWhite(), 0, 0))
            elif isinstance(pc, Pawn) :
                pi.append(Pawn(pc.getIsWhite(), 0, 0))
            pi[len(pi)-1].setBoardPos(pc.getBoardPos()[0], pc.getBoardPos()[1])
            pi[len(pi)-1].setIsDead(pc.getIsDead())
        return pi

    def copyChessBoard(self, chessBoard) :
        cb = list()
        for r in chessBoard :
            tmpList = list()
            for l in r :
                tmpList.append(l)
            cb.append(tmpList)

        return cb
    
    def getPieces(self) :
        return self.pieces

    def minimaxRoot(self, depth, chessBoard, pieces, isMax) :
        possibleMoves = list()
        for pc in pieces :
            if not pc.getIsDead() and pc.getIsWhite() != isMax :
                possibleMoves.append((pc, pc.canMove(chessBoard)))

        bestMove = -9999
        bestMoveFinal = [possibleMoves[0][0],possibleMoves[0][1]]
        
        for pms in possibleMoves :
            for pm in pms[1] :
                pi = self.copyPieces(pieces)
                cb = self.copyChessBoard(chessBoard)
                cb[pms[0].getBoardPos()[0]][pms[0].getBoardPos()[1]] = 0
                if cb[pm[0]][pm[1]] != 0 :
                    for pc in pi :
                        if pc.getBoardPos() == (pm[0], pm[1]) :
                            pc.setIsDead(True)
                cb[pm[0]][pm[1]] = 1 if pms[0].getIsWhite() else 2
                value = max(bestMove, self.minimax(depth -1, cb, pi, -10000, 10000, not isMax))

                if value > bestMove :
                    bestMove = value
                    bestMoveFinal = [pms[0],pm]

        return bestMoveFinal
    
    def minimax(self, depth, chessBoard, pieces, alpha, beta, isMax) :
        if depth <= 0 :
            return self.evaluation(pieces)
        
        possibleMoves = list()
        for pc in pieces :
            if not pc.getIsDead() and pc.getIsWhite() != isMax :
                possibleMoves.append((pc, pc.canMove(chessBoard)))
        if isMax :
            bestMove = -9999
            for pms in possibleMoves :
                for pm in pms[1] :
                    pi = self.copyPieces(pieces)
                    cb = self.copyChessBoard(chessBoard)
                    cb[pms[0].getBoardPos()[0]][pms[0].getBoardPos()[1]] = 0
                    if cb[pm[0]][pm[1]] != 0 :
                        for pc in pi :
                            if pc.getBoardPos() == (pm[0], pm[1]) :
                                pc.setIsDead(True)
                    cb[pm[0]][pm[1]] = 1 if pms[0].getIsWhite() else 2
                    bestMove = max(bestMove, self.minimax(depth -1, cb, pi, alpha, beta, not isMax))
                    alpha = max(alpha, bestMove)

                    if beta <= alpha :
                        return bestMove

            return bestMove

        else :
            bestMove = 9999
            for pms in possibleMoves :
                for pm in pms[1] : 
                    pi = self.copyPieces(pieces)
                    cb = self.copyChessBoard(chessBoard)
                    cb[pms[0].getBoardPos()[0]][pms[0].getBoardPos()[1]] = 0
                    if cb[pm[0]][pm[1]] != 0 :
                        for pc in pi :
                            if pc.getBoardPos() == (pm[0], pm[1]) :
                                pc.setIsDead(True)
                    cb[pm[0]][pm[1]] = 1 if pms[0].getIsWhite() else 2
                    bestMove = min(bestMove, self.minimax(depth -1, cb, pi, alpha, beta, not isMax))
                    beta = min(beta, bestMove)
                    
                    if beta <= alpha :
                        return bestMove

            return bestMove
    
    def evaluation(self, pieces) :
        val = 0

        for pc in pieces :
            if not pc.getIsDead() :
                val -= pc.getPieceValue()

        return val
