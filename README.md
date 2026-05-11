#  CODE GUESSING GAME

## Decrease & Conquer Strategy Based Puzzle Game

---

##  Table of Contents
1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Algorithm Strategy](#algorithm-strategy)
4. [Features](#features)
5. [Installation & Setup](#installation--setup)
6. [How to Play](#how-to-play)
7. [Game Rules](#game-rules)
8. [Technical Details](#technical-details)
9. [Complexity Analysis](#complexity-analysis)
10. [File Structure](#file-structure)
11. [Screenshots](#screenshots)
12. [Troubleshooting](#troubleshooting)
13. [Future Enhancements](#future-enhancements)
14. [Credits](#credits)

---

## Project Overview

The **Code Guessing Game** is an interactive GUI-based puzzle game where the player must identify a hidden binary code by asking strategic questions. The game implements the **Decrease-and-Conquer algorithm** to solve the puzzle in at most `n` questions (where `n` is the code length).

This project was developed as Assignment #4 for the **Design and Analysis of Algorithms** course at Bahria University Islamabad Campus.

---

##  Problem Statement

Your friend thinks of an **n-bit string** (sequence of 0's and 1's, e.g., "01011" for n=5). Your goal is to identify the code by asking questions. Each question provides an n-bit string, and your friend tells you how many bits match the corresponding bits in the code.

**Example:**
- Hidden Code: `01011`
- Your Guess: `11001`
- Response: `3` (matches at positions 1, 3, 4)

**Objective:** Design an efficient algorithm that identifies the code in at most **n questions**.

---

##  Algorithm Strategy

### Decrease-and-Conquer Approach

1. **First Query (Free Hint):** Query all zeros (`000...0`) to determine how many zeros are in the correct positions.
2. **Bit-by-Bit Deduction:** Flip one bit at a time and observe the change in matches:
   - If matches **increase** → flipped bit is `1`
   - If matches **decrease** → flipped bit is `0`
3. **Last Bit Determination:** Use the total zero count from the first query to determine the last bit.

### Why This Works

| Step | Action | Information Gained |
|------|--------|-------------------|
| 1 | Query `000...0` | Number of zeros in correct positions |
| 2 | Flip bit i to 1 | Whether bit i should be 0 or 1 |
| 3 | Repeat for all bits | Complete code reconstructed |

**Time Complexity:** Θ(n) - Linear time!  
**Space Complexity:** Θ(n)

---

##  Features

### Core Features
- ✅ **Random Code Length** (3-8 bits) - Friend chooses randomly
- ✅ **Free Hint System** - First guess of all zeros doesn't count as attempt
- ✅ **Real-time Statistics** - Matching bits, attempts counter, timer
- ✅ **Attempt Limit** - Maximum n attempts (excluding free hint)
- ✅ **Visual Feedback** - Cartoon faces (happy, sad, win)
- ✅ **Restart Functionality** - New random code and length

### UI/UX Features
- 🎨 **Gradient Backgrounds** - Smooth color transitions
- ✨ **Particle Animation** - Floating particles in header
- 🔘 **Glowing Buttons** - Hover effects and neon borders
- 📊 **Animated Stat Boxes** - Real-time score updates
- 🖱️ **Scrollable Interface** - Supports all screen sizes
- 🔊 **Sound Effects** - Win sound on victory

##  Game Rules

| Rule | Description |
|------|-------------|
| **Code Length** | Random between 3-8 bits (friend's choice) |
| **First Guess** | Must be all zeros (**FREE hint**) |
| **Valid Input** | Only `0`s and `1`s, exact length `n` |
| **Attempt Limit** | `n` attempts (free hint **NOT** counted) |
| **Win Condition** | Guess entire code correctly |
| **Loss Condition** | `n` wrong guesses |


##  Example Gameplay (n=5)

| Guess | Input | Matches | Attempts | Strategy |
|-------|-------|---------|----------|----------|
| 1 (Free) | `00000` | 2 | 0 | Free hint |
| 2 | `10000` | 3 | 1 | Bit 0 = 1 (matches increased) |
| 3 | `11000` | 2 | 2 | Bit 1 = 0 (matches decreased) |
| 4 | `10100` | 3 | 3 | Bit 2 = 1 |
| 5 | `10110` | 5 | 4 | **WIN!** |

---

##Credits

| Role | Name |
|------|------|
| **Student** | Maryam Khan |
| **Enrollment** | 01-134242-064 |
| **Program** | BS-CS (5th Semester) |
| **Course** | Design and Analysis of Algorithm |
| **Instructor** | Mam Saima Jawad |
| **University** | Bahria University Islamabad Campus |
| **Assignment** | #4 - Project Part II |
| **Submission Date** | May 11, 2026 |


##Conclusion

The **Code Guessing Game** successfully demonstrates the **Decrease-and-Conquer** algorithm in action. With **Θ(n) time complexity**, it solves the puzzle exponentially faster than brute force (Θ(2ⁿ)). The interactive GUI makes the algorithm accessible and engaging for players while maintaining educational value.

