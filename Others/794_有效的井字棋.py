# 给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。
#
# 井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。
#
# 以下是井字游戏的规则：
#
# 1. 玩家轮流将字符放入空位（' '）中。
# 2. 玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。
# 3. 'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。
# 4. 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
# 5. 当所有位置非空时，也算为游戏结束。
# 6. 如果游戏结束，玩家不允许再放置字符。
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-tic-tac-toe-state
from typing import List


def is_winner(board: List[str], player: str) -> bool:
    for row in board:
        if all(char == player for char in row):
            return True
    for i in range(3):
        if all(row[i] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


class Solution:
    # 解题思路：
    # 只要棋盘上没有输赢 X的数量比O的数量多1 棋盘未满就返回TRUE
    # 否则返回 FALSE
    # 因此遍历棋盘判断输赢即可

    def validTicTacToe(self, board: List[str]) -> bool:
        counter = {
            'X': 0,
            'O': 0,
            ' ': 0
        }
        for row in board:
            for char in row:
                counter[char] += 1
        if counter[' '] == 0:
            if counter['X'] != counter['O'] + 1:
                return False
            elif is_winner(board, 'O'):
                return False
        else:
            if counter['X'] == counter['O']:
                if is_winner(board, 'X'):
                    return False
            elif counter['X'] == counter['O'] + 1:
                if is_winner(board, 'O'):
                    return False
            else:
                return False
        return True
