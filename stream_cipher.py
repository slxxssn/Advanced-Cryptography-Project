def lfsr(seed, taps, length):
    state = seed[:]
    output = []

    for _ in range(length):
        output.append(state[-1])

        feedback = 0
        for tap in taps:
            feedback ^= state[tap]

        state = [feedback] + state[:-1]

    return output


def rc4_simulation(text, key):
    result = ""

    for i, char in enumerate(text):
        result += chr(ord(char) ^ ord(key[i % len(key)]))

    return result