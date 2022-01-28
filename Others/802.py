class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        end_node = []
        node_map = [[0 for _ in range(n)] for _ in range(n)]
        for index, edges in enumerate(graph):
            if len(edges) == 0:
                end_node.append(index)
            for node in edges:
                node_map[index][node] = 1
        print(node_map)
        ans = []
        for i in range(n):
            res = []
            self.dfs(node_map, i, [], end_node, res)
            print(res)
            if all(res):
                ans.append(i)
        return ans

    def dfs(self, node_map, current_node, temp, end_node, res):
        if current_node in temp:
            res.append(False)
            if temp:
                temp.pop()
            return
        if current_node in end_node:
            res.append(True)
            if temp:
                temp.pop()
            return
        temp.append(current_node)
        for i in range(len(node_map)):
            if node_map[current_node][i]:
                self.dfs(node_map, i, temp, end_node, res)


if __name__ == '__main__':
    test = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
    print(Solution().eventualSafeNodes(test))
