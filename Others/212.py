from typing import *


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        def out(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return True
            return False
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        character_location = {}
        for i in range(m):
            for j in range(n):
                if board[i][j] not in character_location.keys():
                    character_location[board[i][j]] = [(i, j)]
                else:
                    character_location[board[i][j]].append((i, j))
        ans = []
        for word in words:
            if len(word) == 1 and word[0] in character_location.keys():
                ans.append(word)
                continue

            if word[0] not in character_location.keys():
                continue
            found = False
            for loc in character_location[word[0]]:
                if found:
                    break
                queue = [loc]
                location_queue = [1]
                used = [[loc]]
                while queue and not found:
                    cur_used = used.pop(0)
                    cx, cy = queue.pop(0)
                    nt = location_queue.pop(0)
                    for dx, dy in directions:
                        temp = cur_used[:]
                        nx, ny = cx + dx, cy + dy
                        if (nx, ny) in temp or out(nx, ny):
                            continue
                        if board[nx][ny] == word[nt]:
                            if nt >= len(word) - 1:
                                ans.append(word)
                                queue = []
                                found = True
                                break
                            queue.append((nx, ny))
                            location_queue.append(nt + 1)
                            temp.append((nx, ny))
                            used.append(temp)
        return ans


if __name__ == '__main__':
    solution = Solution()
    ans = solution.findWords(
        [["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]],
        ["aaaaaaaaaa"]
    )
    print(ans)
