#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


using namespace std;

int main() {
    int num_lines, original_width, new_width;
    cin >> num_lines >> original_width >> new_width;

    string input_string = "";
    for (int line_index = 0; line_index < num_lines; line_index++) {
        string line;
        cin >> line;

        if (line_index % 2 == 0) {
            input_string += line;
        } else {
            reverse(line.begin(), line.end());
            input_string += line;
        }
    }

    vector<string> words;
    string word = "";
    for (char c : input_string) {
        if (c == '.') {
            words.push_back(word);
            word = "";
        } else {
            word += c;
        }
    }
    words.push_back(word);

    int current_line_length = 0;
    int line_count = 1;
    for (int index = 0; index < words.size(); index++) {
        if (index + 1 == words.size()) {
            words[index].erase(remove_if(words[index].begin(), words[index].end(), ::isspace), words[index].end());
        }

        if (current_line_length == 0) {
            current_line_length += words[index].length();
        } else {
            if (current_line_length + words[index].length() + 1 > new_width) {
                line_count++;
                current_line_length = words[index].length();
            } else {
                current_line_length += (words[index].length() + 1);
            }
        }
    }

    cout << line_count << endl;
    return 0;
}

