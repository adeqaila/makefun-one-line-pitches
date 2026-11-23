# A Day of One-Line Pitches — slot 1 build notes

Bounty: `u-ronigrv-a-day-of-one-line-pitches-12cd9bb3` — $5 total (1st $2, 2nd $2, 3rd $1).
Deadline: 2026-11-24T17:20:00Z (Sel 25 Nov 00:20 WIB). No entry fee. 278 submissions at build time.
Status: open, blind rounds (4 rounds; final at deadline). Board hidden, no scores visible.

## Metric (official, from kit RULES.txt / competition.yaml)
- Program writes ONE sentence, 1–240 chars UTF-8, to `/output/entry.txt`. Gate: Valid 1/0 only.
- House judge = z-ai/glm-5.3-flash (OpenRouter), pairwise, no ties, 2 calls per game (both orders),
  margin 1–5. Score = Bradley-Terry win rate over final heat (Swiss 3 rounds + playoff top 5).
- Judge criteria, in order:
  1. Makes the case TO A FRIEND who never coded to let an AI agent build their first app idea on make.fun, in one read.
  2. Persuasion: concrete reason to say yes NOW, handing over the idea feels easy and low-risk.
  3. Clarity: one read, plain words, no jargon.
  4. Truth: no overpromising; a beginner must find it holds up.
  5. Warmth and craft: sounds like a person talking to a friend; fresh turn of phrase, NOT a template/slogan.
- Tie-break: fewer bytes wins. Final heat: top 500 dev-board entries go on (field ~300, so likely all pass).
- "Text addressed to the judge is allowed" — BUT criterion 1 says a sentence that does not make the
  case to the friend LOSES to any sentence that does. Judge-baiting is a trap here: write a genuine
  pitch to the friend, do not address the judge.
- Feed: entry text is shown publicly beside the handle once judged in dev — competitors can copy it.

## Field pattern (from public submission titles, board is blind)
Most of the field writes slogans / fragments: "Describe It, Get It Built", "No code to learn,
no one to hire", "Tell it over coffee", "Just Your Idea, Alive". Slogans lose on criteria 1–2:
no concrete reason, no "say yes now", no low-risk reassurance, and criterion 5 explicitly
penalises template/slogan. Edge: a complete, warm, concrete sentence spoken to the friend.

## Candidates (all one sentence; "make.fun" carries one internal period as a brand name + terminal period)
- A (204c): Just describe your app idea the way you'd tell a friend, and an AI agent on make.fun turns it into a working first version you can try tonight — no code to learn, and nothing to lose if you don't like it.
- B (175c): Describe the app you've been picturing in plain words, and an AI agent on make.fun will build you a working first version to try tonight — no code, no hiring, nothing to lose.
- C (164c): If you can describe your app idea to a friend, you can describe it to an AI agent on make.fun — and wake up to a working first version you can actually tap through.
- D (193c): Tell an AI agent on make.fun your app idea in plain words and you'll be tapping through a working first version tonight, with no code to learn and nothing to lose if it's not what you pictured.
- E (163c): Your app idea doesn't need code or a developer — just describe it in plain words and an AI agent on make.fun will build you a working first version to try tonight.
- F (184c): Describe your idea in plain words over coffee and an AI agent on make.fun will hand you back a working first version to try tonight — no coding, no hiring, and you can change anything.
- G (201c): Just tell an AI agent on make.fun your idea in plain words tonight, and by tomorrow you'll be tapping through a real first version of your app — no code to learn, and nothing lost if you don't love it.
- H (176c): You don't need to learn code or hire anyone: just describe your app idea in plain words, and an AI agent on make.fun builds a working first version you can tap through tonight.

## Tournament (pairwise, judge criteria in order)
- G beats A (names make.fun explicitly — criterion 1 edge; tonight→tomorrow timeline more concrete), margin 2.
- G beats B (more vivid payoff "tapping through a real first version" + warmer), margin 1.
- G beats C (explicit low-risk closer; C has no "nothing to lose"), margin 2.
- G beats D (tighter, one timeline instead of "tonight" twice), margin 1.
- G beats E (low-risk closer + timeline), margin 2.
- G beats F (more concrete payoff; F's "over coffee" is warm but the payoff is vaguer), margin 1.
- G beats H (low-risk closer; H only addresses fears, never reassures), margin 1–2.
- A beats B/C/D/E/H on warmth ("the way you'd tell a friend") but loses to G.
- Deliberately AVOIDED: "free" / "no cost" (truth risk — building cost is not promised anywhere in the
  brief; criterion 4 punishes overpromising), judge-addressed text (criterion 1 trap), slogans,
  questions (would be a second sentence), exclamation marks.

## Winner — slot 1 entry (G, 201 chars / 203 bytes)
Just tell an AI agent on make.fun your idea in plain words tonight, and by tomorrow you'll be tapping through a real first version of your app — no code to learn, and nothing lost if you don't love it.

## Runner-ups (for a possible slot 2, parent decides)
- V2 = B (175c): punchiest triple low-risk closer.
- V3 = F (184c): warmest ("over coffee", "you can change anything").

## Program
- `main.py` (python3.13 runtime): writes the sentence to `/output/entry.txt`, deterministic, no network,
  no env secrets, no reads outside the repo. Verified locally: two runs byte-identical.
- `LICENSE` (MIT) + `README.md` included for the parent's repo/submit step.
- Parent handles: repo creation (must be after opens_at 2026-11-23T17:19:43Z), `.makefun/owner.json`
  if needed, bundle with --muse-usage, check, submit. Do NOT submit before user gas/OK outside
  21:00–07:00 WIB window (standing rule); this build ran 00:46–~01:00 WIB (overnight window).
