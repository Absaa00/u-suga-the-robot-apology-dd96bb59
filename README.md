# The Robot Apology

[![Built with make.fun](https://make.fun/badge.svg)](https://make.fun)

An entry for the [make.fun](https://make.fun) competition
**u-suga-the-robot-apology-dd96bb59** ("The Robot Apology").

## What it does

`main.py` is a small deterministic program — no network, no input — that
writes a two-line apology to `/output/entry.txt`:

1. **Line 1:** one sentence in which a household robot apologises for one
   specific, concrete mistake.
2. **Line 2:** one sentence stating what the robot learned from that exact
   mistake and what it will do differently.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
