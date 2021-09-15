# triple-triad-deck-solver
Fairly naive attempt at a deck solver for Triple Triad decks from Final Fantasy XIV. **Note, this does not work well for practical purposes!**

## Tool Summary
This tool is a python program that attempts to determines the winning percentage of one specific Triple Triad deck against another specific deck.

Currently, this percentage is calculated by simulating all possible games between the 2 given decks and dividing matches won by one deck by total matches.

(matches one by deck 1) \* (total number of matches)

### Current Supported Rules
* Standard

## Time Complexity Analysis
Triple Triad in FF14 has a suprisingly large problem space for essentially being tic-tac-toe. For example the number of matches between 2 specific decks breaks down as follows:
* <sub>5</sub>P<sub>5</sub> for the possible play permutations of the first deck (all 5 cards will be played) = 5!.
* <sub>5</sub>P<sub>4</sub> for the possible play permutations of the second deck (4 of the 5 cards will be played) = 5!/(5!-4!) = 5!.
* Number of possible game outcomes between 2 fixes play permutations from above: 9!
* So the total number of possible games is: 5! \* 5! \* 9! = 5225472000 \~ **5.2 billion possible games for 2 specific decks**.

Why this long-winded math explanation? 5.2 billion can be aruged to be large enough N for time-complexity to be an issue, and it is, in my opinion, this project's biggest issue currently.

Currently it takes ~17 seconds to simulate a single match for a single play permutation. This fact is a problem because 17 seconds\*5.2 billion ~24.6 million hours which is just a slightly infeasible compute time. To achieve a compute time in the hours or minutes range, the program would need to reduce single match compute by something like 8-9 orders of magnitude. Some of the reduction could be achieved by utilizing an extensive number of parallel threads, but more work needs to be done on single match compute time.

**TLDR: Time complexity bad.**
