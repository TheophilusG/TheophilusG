#!/usr/bin/env python3
"""
Daily README update script for dynamic profile README.
Updates daily quote and dev mood based on day of year.
"""

import re
from datetime import datetime

# Pool of developer-themed quotes (30+ unique quotes)
QUOTES = [
    "The only way to do great work is to love what you do. — Steve Jobs",
    "First, solve the problem. Then, write the code. — John Johnson",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. — Martin Fowler",
    "The most dangerous phrase in the language is, 'It's always been done this way.' — Grace Hopper",
    "Code is read much more often than it is written. — Guido van Rossum",
    "The best performance improvement is the transition from nonworking to working. — John Ousterhout",
    "Simplicity is prerequisite for reliability. — Edsger W. Dijkstra",
    "Premature optimization is the root of all evil. — Donald Knuth",
    "Talk is cheap. Show me the code. — Linus Torvalds",
    "Debugging: Removing the needles from the haystack. — Dev Proverb",
    "It's not a bug, it's a feature. — Classic Developer Excuse",
    "Don't go wrong in the details. — Japanese Proverb",
    "There's no place like 127.0.0.1 — Dev Quote",
    "One man's crappy software is another man's full-time job. — Jessica Gaston",
    "The best error message is the one that never shows up. — Thomas Fuchs",
    "Why do Java developers wear glasses? Because they can't C#. — Programming Joke",
    "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. — John Woods",
    "Logic is the technique by which the inexpressible is made to appear relevant. — Norman McLaren",
    "I have always wished for my computer to be as easy to use as my telephone; my wish has come true because I can no longer figure out how to use my telephone. — Bjarne Stroustrup",
    "Optimism is an occupational hazard of programming; feedback is the treatment. — Kent Beck",
    "Every software engineer has two jobs: to write code and work on documentation. Most fail at the second part. — Dev Wisdom",
    "The function of good software is to make the complex appear simple. — Grady Booch",
    "In software, perfection is not just about code. Simplicity of use is as important as the code itself. — Jef Raskin",
    "Make it work, make it right, make it fast. In that order. — Kent Beck",
    "Computers are good at following instructions, but not at reading minds. — Donald Knuth",
    "Before software should be reusable, it should be usable. — Ralph Johnson",
    "I'm not a great programmer; I'm just a good programmer with great habits. — Kent Beck",
    "The goal of software engineering is to control complexity, not to create it. — Pamela Zave",
    "Reusable code is based on a simple idea—it's much better to write a function that can do many things, than write many functions that each do one thing. — Jim Weirich",
    "The purpose of abstraction is not to be vague, but to create a new semantic level in which one can be absolutely precise. — E. W. Dijkstra",
    "Nine out of ten developers agree: one out of ten developers lacks basic statistics skills. — Dev Proverb",
    "A good programmer is someone who always looks both ways before crossing a one-way street. — Doug Linder",
    "Writing code is telling the computer what to do. Writing good code is communicating your intent to humans. — Dev Philosophy",
]

# Pool of dev mood combinations (14+ mood tag combinations)
# Each is 3 backtick-wrapped tags joined by ·
MOODS = [
    "`focused` · `caffeine-powered` · `shipping-code`",
    "`debugging` · `determined` · `coffee-fueled`",
    "`creative` · `ambitious` · `energized`",
    "`thoughtful` · `refactoring` · `optimizing`",
    "`exploring` · `learning` · `curious`",
    "`passionate` · `building` · `innovating`",
    "`pragmatic` · `efficient` · `productive`",
    "`collaborative` · `teamwork` · `synergistic`",
    "`persistent` · `problem-solving` · `persistent`",
    "`zealous` · `committed` · `dedicated`",
    "`experimental` · `risk-taking` · `bold`",
    "`meticulous` · `detail-oriented` · `thorough`",
    "`inspired` · `driven` · `motivated`",
    "`flexible` · `adaptive` · `resilient`",
    "`analytical` · `logical` · `systematic`",
    "`excited` · `thrilled` · `pumped`",
]


def get_daily_quote():
    """Get the quote for today using day of year."""
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    index = (day_of_year - 1) % len(QUOTES)
    return QUOTES[index]


def get_daily_mood():
    """Get the mood for today using day of year."""
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    index = (day_of_year - 1) % len(MOODS)
    return MOODS[index]


def update_readme():
    """Update README.md with daily quote and mood."""
    # Read the current README
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("ERROR: README.md not found")
        return False

    # Get today's values
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    daily_quote = get_daily_quote()
    daily_mood = get_daily_mood()

    # Replace the daily quote section
    content = re.sub(
        r"<!-- DAILY-QUOTE-START -->.*?<!-- DAILY-QUOTE-END -->",
        f"<!-- DAILY-QUOTE-START -->\n> {daily_quote}\n<!-- DAILY-QUOTE-END -->",
        content,
        flags=re.DOTALL,
    )

    # Replace the daily mood section
    content = re.sub(
        r"<!-- DAILY-MOOD-START -->.*?<!-- DAILY-MOOD-END -->",
        f"<!-- DAILY-MOOD-START -->\n{daily_mood}\n<!-- DAILY-MOOD-END -->",
        content,
        flags=re.DOTALL,
    )

    # Write the updated README
    try:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(content)
    except IOError as e:
        print(f"ERROR: Could not write README.md: {e}")
        return False

    # Log the update
    print(f"✓ Daily README update successful")
    print(f"  Day: {day_of_year}")
    print(f"  Quote: {daily_quote}")
    print(f"  Mood: {daily_mood}")
    return True


if __name__ == "__main__":
    success = update_readme()
    exit(0 if success else 1)
