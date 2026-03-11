from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_numeric_comparison_regression_for_hint_direction():
    # Regression: avoid lexicographic/string-style comparisons that invert hints.
    # 9 is less than 10 numerically, so outcome must be "Too Low".
    result = check_guess(9, 10)
    assert result == "Too Low"
