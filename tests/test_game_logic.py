from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug 1: Hints were backwards — too high said "Go HIGHER" instead of "Go LOWER"
def test_too_high_message_says_go_lower():
    # Guessing 60 when secret is 50 should tell the player to go lower, not higher
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    # Guessing 40 when secret is 50 should tell the player to go higher, not lower
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# Bug 2: Easy mode gave fewer attempts than Normal mode
def test_easy_range_is_smaller_than_normal():
    # Easy should have a smaller number range than Normal so it's actually easier
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    assert (easy_high - easy_low) < (normal_high - normal_low)
