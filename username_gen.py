#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║     UserHawk - Username Wordlist Gen    ║
║     Made by muhammed95rafi-arch          ║
╚══════════════════════════════════════════╝
"""

import sys
import itertools

RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
BOLD    = "\033[1m"
RESET   = "\033[0m"
MAGENTA = "\033[95m"

def print_banner():
    print(f"""
{CYAN}{BOLD}
 _   _                 _  _     _
| | | | ___  ___ _ __ | || |   (_)___  _ __
| | | |/ __|/ _ \\ '__|| || |_  | / __|| '_ \\
| |_| |\\__ \\  __/ |   |__   _| | \\__ \\| | | |
 \\___/ |___/\\___|_|      |_|   |_|___/|_| |_|
{RESET}
{YELLOW}   [ Username Wordlist Generator ] [ v1.0 ]{RESET}
    """)

def generate_usernames(full_name: str, birth_year: str = "") -> list:
    parts = full_name.lower().strip().split()

    if len(parts) == 0:
        return []

    first = parts[0]
    last  = parts[-1] if len(parts) > 1 else ""
    mid   = parts[1] if len(parts) > 2 else ""

    f  = first
    l  = last
    fi = first[0] if first else ""
    li = last[0]  if last  else ""
    mi = mid[0]   if mid   else ""

    year     = birth_year.strip()
    year2    = year[-2:] if len(year) >= 2 else year
    numbers  = ["1", "12", "123", "007", "99", "01", year2, year] if year else ["1", "12", "123", "007", "99", "01"]

    separators = ["", "_", ".", "-"]

    raw = set()

    # ── Basic combos ──────────────────────────────────────────
    if l:
        for sep in separators:
            raw.add(f"{f}{sep}{l}")
            raw.add(f"{l}{sep}{f}")
            raw.add(f"{fi}{sep}{l}")
            raw.add(f"{f}{sep}{li}")
            raw.add(f"{li}{sep}{f}")
            if mi:
                raw.add(f"{fi}{sep}{mi}{sep}{l}")
                raw.add(f"{f}{sep}{mi}{sep}{l}")
    else:
        raw.add(f)

    # ── With numbers ──────────────────────────────────────────
    base_list = list(raw.copy())
    for base in base_list:
        for num in numbers:
            if num:
                raw.add(f"{base}{num}")
                raw.add(f"{num}{base}")

    # ── Common patterns ───────────────────────────────────────
    if l:
        raw.add(f"the{f}")
        raw.add(f"real{f}")
        raw.add(f"i_am_{f}")
        raw.add(f"official_{f}")
        raw.add(f"{f}official")
        raw.add(f"{f}_{l[0:3]}")
        raw.add(f"{f[0:4]}{l[0:4]}")
        raw.add(f"{f}{l[0:3]}")

    # ── Leet speak variants ───────────────────────────────────
    leet_map = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "t": "7"}
    for base in list(raw.copy()):
        leet = ""
        for ch in base:
            leet += leet_map.get(ch, ch)
        if leet != base:
            raw.add(leet)

    # ── Clean & sort ──────────────────────────────────────────
    result = sorted([u for u in raw if u and len(u) >= 3 and len(u) <= 30])
    return result


def main():
    print_banner()

    print(f"{YELLOW}[*] Enter target's full name (e.g: Muhammed Rafi):{RESET} ", end="")
    full_name = input().strip()

    if not full_name:
        print(f"{RED}[!] Name cannot be empty!{RESET}")
        sys.exit(1)

    print(f"{YELLOW}[*] Enter birth year (optional, press Enter to skip):{RESET} ", end="")
    birth_year = input().strip()

    print(f"\n{BOLD}{CYAN}[*] Generating usernames for: {full_name}{RESET}\n")

    usernames = generate_usernames(full_name, birth_year)

    print(f"{BOLD}{'─'*40}{RESET}")
    for i, u in enumerate(usernames, 1):
        print(f"  {GREEN}{i:>3}.{RESET} {u}")
    print(f"{BOLD}{'─'*40}{RESET}")

    print(f"\n{YELLOW}[+] Total generated: {BOLD}{len(usernames)}{RESET} usernames\n")

    # ── Save to file option ───────────────────────────────────
    print(f"{YELLOW}[?] Save to file? (y/n):{RESET} ", end="")
    save = input().strip().lower()

    if save == "y":
        filename = full_name.replace(" ", "_").lower() + "_usernames.txt"
        with open(filename, "w") as f:
            for u in usernames:
                f.write(u + "\n")
        print(f"\n{GREEN}[✓] Saved to: {filename}{RESET}\n")

    # ── Search with UserHawk option ───────────────────────────
    print(f"{YELLOW}[?] Search a username with UserHawk now? (y/n):{RESET} ", end="")
    search = input().strip().lower()

    if search == "y":
        print(f"{YELLOW}[?] Enter username to search:{RESET} ", end="")
        target = input().strip()
        print(f"\n{CYAN}[*] Run this command:{RESET}")
        print(f"  {BOLD}python3 userhawk.py {target}{RESET}\n")


if __name__ == "__main__":
    main()