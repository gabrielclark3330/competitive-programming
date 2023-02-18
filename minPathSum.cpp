#include <iostream>
#include <queue>
#include "vector"
#include <map>

using namespace std;

class Solution {
public:
    int minPathSum(vector< vector<int> >& grid) {
        struct position {
            int row;
            int col;
            int sumToPoint;
            position(int row_, int col_, int sumToPoint_){
                row = row_;
                col = col_;
                sumToPoint = sumToPoint_;
            }
	    bool operator<(const position& pos) const
	    {
		return sumToPoint < pos.sumToPoint;
	    }
        };
        auto cmp = [](position left, position right) {
            return (left.sumToPoint) < (right.sumToPoint); };
	//priority_queue<position, vector<position>, decltype(cmp)> pq(cmp);
	priority_queue<position> pq;

        bool reached_end = false;
        map<pair<int, int>, int> visited;
        for (int i=0; i<grid.size(); i++) {
            for (int j=0; j<grid[0].size(); j++) {
                visited[make_pair(i,j)] = 99999;
            }
        }

        position pos = position(0, 0, grid[0][0]);
        pq.push(pos);
        while(!pq.empty()) {
	    position top = pq.top();
	    pq.pop();
            visited[make_pair(top.row, top.col)] = top.sumToPoint;
	    /*
	    cout<<top.row;
	    cout<<",";
	    cout<<top.col;
	    cout<<",";
	    cout<<top.sumToPoint;
	    cout<<"\n";
	    */

            if (top.row+1 < grid.size()){
                if ((grid[top.row+1][top.col]+top.sumToPoint) < visited[make_pair(top.row+1,top.col)]) {
                    int weight = grid[top.row+1][top.col]+top.sumToPoint;
                    int row = top.row+1;
                    int col = top.col;
                    pq.push(position(row, col, weight));
                }
            }
            if (top.row-1 >= 0){
                if ((grid[top.row-1][top.col]+top.sumToPoint) < visited[make_pair(top.row-1,top.col)]) {
                    int weight = grid[top.row-1][top.col]+top.sumToPoint;
                    int row = top.row-1;
                    int col = top.col;
                    pq.push(position(row, col, weight));
                }
            }
            if (top.col+1 < grid[0].size()){
                if ((grid[top.row][top.col+1]+top.sumToPoint) < visited[make_pair(top.row,top.col+1)]) {
                    int weight = grid[top.row][top.col+1]+top.sumToPoint;
                    int row = top.row;
                    int col = top.col+1;
                    pq.push(position(row, col, weight));
                }
            }
            if (top.col-1 >= 0){
                if ((grid[top.row][top.col-1]+top.sumToPoint) < visited[make_pair(top.row,top.col-1)]) {
                    int weight = grid[top.row][top.col-1]+top.sumToPoint;
                    int row = top.row;
                    int col = top.col-1;
                    pq.push(position(row, col, weight));
                }
            }
        }

        return visited[make_pair(grid.size()-1, grid[0].size()-1)];
    }
};

int main() {
        vector< vector<int> > grid = { {1,3,1},{1,5,1},{4,2,1} };
	Solution s = Solution();
	cout << s.minPathSum(grid);
}
