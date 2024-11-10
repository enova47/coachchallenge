# 2019-2020 Coach's Challenge Review
**Background**

The NBA instituted the coach’s challenge on a one-year trial basis for the 2019-2020 NBA season. The coach’s challenge allows instant replay review of personal foul calls (offensive and defensive) to the challenging team, out-of-bounds, and goaltending/basket interference. Challenges of out-of-bounds and goaltending/basket interference in the last two minutes of the fourth quarter and any overtime periods are not allowed.

Each team is given one challenge per game. If the challenge is successful, the call is corrected at the time of the violation and possession is determined. If the challenge is unsuccessful, the call stands and the challenger is charged one of their full timeouts. Challenges cannot be initiated if there are no full timeouts remaining.

**Process**

Challenge data was extracted from the list of coach’s challenges listed on the NBA site (sources below). Play-by-play data was matched to these challenges using the nba_api Python library to identify the players and play descriptions for each challenge from October 22, 2019 to March 11, 2020 until the regular season was suspended. Additional datasets were sourced for coach and referee information. I have linked the combined dataset in a .csv file in this repository.

**Analysis**

I had a few questions on how the coach’s challenge has been used which I thought could be answered with the data available. I have listed my findings to those questions below.

- What was the frequency of challenges and the challenge success rate?

    567 challenges were placed in the season up to March 11, 2020. The challenge success rate was 241/567 (43%).

- Which coaches were more or less likely to use the challenge? What was the average success rate for challenges?
  
    Nick Nurse (TOR) made the most challenges at 39. Taylor Jenkins (MEM) made the least for the full season at 3. Rick Carlisle (DAL), Dwane Casey (NOP) and Kenny
    Atkinson (BKN) had the highest success rate for full-season.

- Any opportunities missed out from using the challenge when timeouts remained (check L2M reports).

    I checked for any challenges that would be reviewed post-game by the NBA referees in the last two minute reports. Last two minute reports are only made for plays in
    the last two minutes of fourth quarter or overtime games only where the score differential is within three points.

- How often were the challenges confirmed by L2M report?

    55 challenges were confirmed by L2M report. 13 successful and 42 unsuccessful.

- Were certain players more or less likely to be involved in coach’s challenges? What were the overturn percentages for these players? Did their performance that night/season correlate with better chance of overturned calls?

    Most challenges for committed players: Kyle Lowry (10), Pascal Siakam (10), James Harden (9) and Jarrett Allen (9). The highest successful challenge rates (for
    players above 5 challenges), was Myles Turner (100% successful for 6 challenges), Cory Joseph and Nerlens Noel (80% success for 5 challenges). The lowest rates were
    Aron Baynes (0% success for 5 challenges) and 20% for 5 challenges each for Anthony Davis, Ben McLemore, and Nikola Jokic. Most frequently disadvantaged players in
    challenge calls: Jimmy Butler (11), Trae Young (11), Bam Adebayo (9), and Damian Lillard (9). Best disadvantaged player rates (unsuccessful above 5 challenges) –
    James Harden (0% success at 6 challenges), Jimmy Butler (0.09%), Damian Lillard (0.1%). Worst rates for disadvantaged players: Julius Randle (0.83% at 6
    challenges), Joel Embiid (0.6% at 5 challenges), Jaylen Brown (100% for 4 challenges).

- Which officiating crew/officials were more or less likely to overturn calls? Who was the crew chief, referee, and umpire?

    Officials with most calls challenged: Sean Wright (19), Brian Forte (16), and Josh Tiven (15). Officials with least calls challenged: B.Adair, B.Adams, S.Jelks (1).
    Officials who had greatest unsuccessful calls (call was correct): D.Taylor (100% at 5 challenges); DeRosa (89% at 9 challenges); Petraitis (88% at 8); Goldenberg
    (80% at 10). Worst: J.Butler (0.2 at 5 challenges); John Goble (0.22 at 9); S.Wall and T. Maddox (0.25 at 8).

- Were coach’s challenges more successful for the home or visiting team?

    There was only a slight difference in success with the coach’s challenge if the challenger was the home or visiting team. Visiting teams won challenges on average
    38.2% of the time, compared to a 37.1% success rate for the home teams.

- What specific types of calls were more likely to see challenges and calls overturned?

    Teams had the most success in challenges for out-of-bounds calls (73.4% overturned) and goaltending (72.7%). Conversely, teams had the least success with
    overturning defensive foul calls (31.8%).
