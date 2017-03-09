# This Python file uses the following encoding: utf-8

numbers = {
    4: 'The word for 4 sounds like the word for death in some East Asian languages',
    9: 'The word for 9 sounds like the word for torture of suffering in Japanese',
    13: 'Judas, the disciple who betrayed Jesus, was the 13th to sit at the table for the Last Supper',
    17: 'Unlucky in Italian culture because the Roman numeral, XVII, can be changed anagramtically to VIXI, which in the Latin language translates to "I have lived", the perfect tense implying "My life is over"',
    39: 'Many Afghans say that the number 39 translates into morda-gow, which literally means "dead cow" but is also a well-known slang term for a procurer of prostitutes — a pimp',
    43: 'The word for 43 sounds like the word for stillbirth in Japanese',
    666: 'In the Bible\'s apocalyptic Book of Revelation, John the Apostle refers to 666 as "the number of the beast"',
}


def get_majority(n):
    return n / 2 + 1


def contains_unlucky_number(n, unlucky_numbers=None):
    if unlucky_numbers is None:
        unlucky_numbers = numbers
    for unlucky_n in unlucky_numbers:
        if str(n).count(str(unlucky_n)) * len(str(unlucky_n)) >= get_majority(len(str(n))):
            return unlucky_n
    return None


def is_lucky(n, with_explanation=False, unlucky_numbers=None):
    if unlucky_numbers is None:
        unlucky_numbers = numbers
    if with_explanation:
        unlucky_n = contains_unlucky_number(n, unlucky_numbers)
        if unlucky_n is None:
            return (True, None)
        else:
            return (False, unlucky_numbers[unlucky_n])
    else:
        return n not in unlucky_numbers


def get(lucky=True, with_explanation=False, unlucky_numbers=None):
    if unlucky_numbers is None:
        unlucky_numbers = numbers
    current_n = 0
    if with_explanation:
        unlucky_cache = {}
        while True:
            current_n_is_lucky, explanation = is_lucky(current_n, with_explanation, unlucky_numbers)
            if current_n_is_lucky == lucky:
                yield (current_n, dict(unlucky_cache))
                unlucky_cache.clear()
            else:
                unlucky_cache[current_n] = explanation
            current_n += 1
    else:
        while True:
            current_n_is_lucky = is_lucky(current_n, with_explanation, unlucky_numbers)
            if current_n_is_lucky == lucky:
                yield current_n
            current_n += 1


def get_lucky(with_explanation=False, unlucky_numbers=None):
    if unlucky_numbers is None:
        unlucky_numbers = numbers
    return get(True, with_explanation, unlucky_numbers)


def get_unlucky(with_explanation=False, unlucky_numbers=None):
    if unlucky_numbers is None:
        unlucky_numbers = numbers
    return get(False, with_explanation, unlucky_numbers)


if __name__ == '__main__':
    import time
    for n, explanation in get_lucky(with_explanation=True):
        if explanation:
            print n
            for skipped_n in explanation:
                print 'skipped %d: %s' % (skipped_n, explanation[skipped_n])
            print
        else:
            print n
            print
        time.sleep(1)
