
## Scope and Platform
We test primarily on **OpenMoHAA (OPM)** because it's open-source, actively developed, and runs on modern systems. When we find issues on OPM that don't occur on vanilla, we report them upstream to the OPM project so that OPM becomes fully backwards-compatible with existing vanilla mods, including this one.

- **Environment:** OpenMoHAA, development builds, not release.
- Bugs found on OPM that don't reproduce on vanilla are fixed by pushing PRs upstream to OPM, not by adding OPM-specific workarounds to this mod.
- **Future direction:** Once the codebase is stabilized and cleaned up, the mod will adopt OPM-specific functions, events, and features (bots, cleaner APIs). At that point, vanilla compatibility will be dropped. Until then, the mod must work on vanilla MOHAA.

## Reporting Bugs

### Required Information

Every bug report **must** include:

- **OPM Version** - What version of OpenMoHAA are you running? Include the full version string from console (type `version` in console).
- **Mod version** - From changelog header or the version number shown on connect (e.g., 2.05).
- **Map** - Exact map filename (ex. `m1l2a`).
- **Player count** - How many players were on the server when the bug occurred.
- **Steps to reproduce** - Include what was done to introduce the bug or conditions under which it appears.
- **qconsole.log** — Attach the full log for the session. At minimum, include 50 lines before and after the error.
- **Crash backtrace** - If the server or client crashed, attach the OPM crash dump or GDB backtrace if you know how.

### What Gets Closed

- **OPM upstream** - Bugs that only reproduce on OPM. These get reported to the OPM project as issues or PRs.
- **Cannot reproduce** - If nobody can reproduce after going through provided steps, issue will be closed if you don't clarify or include better ones.
- **Duplicate** - Linked to the existing issue.
- **Won't fix** - Working as intended.

If reproduction requires specific timing, player count, or prior sequences being finished, say so explicitly. Vague bug reports dont help, narrow it down before filing.



## Proposing Changes

| Type                                                                     | Where                                                       |
| ------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Bug report with repro steps                                              | GitHub Issue                                                |
| Concrete code change proposal (specific files, specific behavior change) | GitHub Issue                                                |
| Ready-to-review code                                                     | Pull Request                                                |
| Idea, question, or brainstorm                                            | GitHub Discussions (if enabled) or Discord `#ideas` channel |
| Architecture debate                                                      | GitHub Issue with a written proposal, or nowhere            |

### No Endless Debates

Decisions happen in this repository, not in Discord. If a discussion in Discord runs past 15 messages without producing a concrete proposal redirect it here.

Architecture discussions are welcome only when:
- They reference specific code and specific problems.
- They propose a concrete alternative with a realistic scope.
- They acknowledge what they'd break and how to test it.
- They don't make life of only maintainer a nightmare.
- They do not interfere with project's current scope, ex. make mod vanilla compatible again when we moved on into **Future direction**.

## Pull Request Rules

### Structure

1. **One fix per PR.** 
   
   Do not mix a bugfix with a cleanup with a feature. If you're fixing a spawn bug, the PR touches the spawn code and nothing else.

1. **Small changes.** 
   
   Prefer changing 1 file over 5. If you need to change 5, explain exactly why in the PR description.
   
1. **No random refactors with fixes** 
   
   If you're in a file to fix a bug and notice messy formatting elsewhere, fix the bug in this PR and submit the cleanup separately.

### Engine Workarounds

All engine-level workarounds (broken Vanilla compatibility) must live in `coop_mod/opm_comp.scr` Not in map scripts. Not scattered across `main.scr`.

- If you're working around a vanilla engine limitation, put the workaround in `opm_comp.scr` and call it from there.
- If a future engine fix eliminates the need, we delete the function from `opm_comp.scr` and update callers. 
- If you're not sure whether something is an engine limitation or a mod bug, ask in the issue before coding.

**For now, do not add OPM-specific code.** 

While the mod is in its vanilla compatible phase, all code must work on the original engine OPM-specific features (bots, OPM provided events, etc.) will come later once the codebase is clean and ready.

### Comment Policy

Comments explain **why**, not **what**. The code shows what.

**Acceptable:**
```scr
// Engine requires gametype 0 to accept the fov command in MP
waitthread coop_mod/compat.scr::changeGameType 0 0
```

**Not acceptable:**
```scr
// set fov for player
// this sets the fov, without it fov would not be set
// fov needs to be above 10 or its bad
waitthread coop_mod/compat.scr::changeGameType 0 0 // change game type to 0
```

Specifically:
- No version tags (`[200]`, `[202]`, `[204]`). Use `git log`.
- No meme markers, jokes, or editorial commentary in code.
- No commented-out code blocks unless absolutely necessary. They're in git history. Delete them.

### Naming Conventions

- **Functions:** camelCase - `manageSpectator`, `playerPlaceAtSpawn`.

### Maintainer Boundaries

This project is maintained by volunteers with limited time. That means:

- Not every bug gets fixed immediately. 
- Not every feature request is accepted.
- Responses may take days, that's normal for a volunteer project.
- If you need something urgently, fork the repo and fix it yourself, then send a PR.

### Questions?

Open a GitHub issue with the `question` label. Or ask in the Discord channel.
