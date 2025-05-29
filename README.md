# 🧠 ThreadRaceRNG

A fun Python project that uses multithreading and a bit of chaos to generate a randomized array based on physical execution timing.

## ⚙️ How it works

We spawn one thread per item in a list (e.g. digits 0 to 9), but none of them start executing until we flip a global switch. Once we say “GO”, all threads race to grab the first item in the array. Because of how threads are scheduled by the OS—and subtle physical realities of your CPU—the order in which they succeed is unpredictable.

In short: **The race *is* the randomness.**

## 🚀 Usage

```bash
python main.py
```

### Example Output:
```commandline
Starting the thread race...
Thread-5 got number: 0
Thread-2 got number: 1
Thread-8 got number: 2
...

Final randomized result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
> The order of the array will change every time you run it :)

## 🎲 What Makes This “Truly” Random?
Most traditional random number generators are deterministic, based on pseudorandom algorithms—great 
for general use but ultimately predictable if you know the seed. What makes ThreadRaceRNG unique is 
that it taps into actual entropy from your computer's hardware.

When the threads race to pop values from the array, their success order depends on real-world factors: 
CPU load, thread scheduling by the OS, current state of CPU caches, background processes, and more. 
These are not predictable in any useful way, and they’re practically impossible to simulate or reproduce 
across runs—even on the same machine.

So while it’s not “quantum random,” it’s rooted in the kind of chaotic physical unpredictability that 
makes this method feel a lot closer to true randomness than any math-based RNG can provide.

## 🤯 Why this matters
This isn’t cryptographically secure randomness, but it is a fun and interesting way to 
generate non-deterministic output using real-world timing variance. Plus, it demonstrates 
how concurrency and entropy can play together in neat ways.


