import time
import os

#commentadded
def intro():
    intro = [
        "    Booting Stellar Interface ⏳",
        "",
        "    [ OK ] Initializing star matrix...",
        "",
        "              *                 *           ",
        "            *   *             *   *         ",
        "           *  *  *           *  *  *        ",
        "         *    *    *       *    *    *      ",
        "            *   *             *   *         ",
        "              *                 *           ",
        "",
        "    [ OK ] Parsing cosmic signatures...",
        "",
        "        _        _        _        ",
        "       /\\ \\     /\\ \\     /\\ \\     ",
        "      /  \\ \\   /  \\ \\   /  \\ \\    ",
        "     / /\\ \\ \\ / /\\ \\ \\ / /\\ \\ \\   ",
        "    / / /\\ \\_\\ / /\\ \\_\\ / /\\ \\_\\ ",
        "   / / /_/ / // / /_/ / // / /_/  ",
        "  / / /__\\/ // / /__\\/ // / /__\\  ",
        "  \\ \\ \\__/ / \\ \\ \\__/ / \\ \\ \\__/  ",
        "   \\ \\___/   \\ \\___/   \\ \\___/    ",
        "    \\/__/     \\/__/     \\/__/     ",
        "",
        "🪐  Welcome to Jubin’s Star Cluster 🪐",
        "",
        "🚀  Preparing for launch sequence...",
        "",
        "✨  May the force be with you. ✨",
        ""
    ]

    for line in intro:
        print(line)
        time.sleep(0.4)

if __name__ == "__main__":
    intro()
