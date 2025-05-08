def get_user_input():
    try:
        runs = int(input("🏏 Enter runs at the fall of the first wicket: "))
        over = float(input("⏱️ Enter current over (e.g., 7.2 for 7 overs 2 balls): "))
        total_overs = int(input("📋 Enter total number of overs in the match: "))
        if over <= 0 or total_overs <= 0 or runs < 0 or over > total_overs:
            raise ValueError
        return runs, over, total_overs
    except ValueError:
        print("❌ Invalid input! Please enter realistic cricket match values.\n")
        return get_user_input()


def calculate_predictions(runs, over, total_overs):
    current_run_rate = runs / over
    run_rate_projection = current_run_rate * total_overs
    wicket_projection = (10 - 1) * runs
    predicted_score = (run_rate_projection + wicket_projection) / 2
    return current_run_rate, predicted_score


def display_results(current_rr, predicted_score):
    print("\n📊 Match Analysis:")
    print(f"🔹 Current Run Rate: {current_rr:.2f} runs/over")
    print(f"🔮 Predicted Final Score: {predicted_score:.2f} runs\n")


def cricket_score_predictor():
    print("🏟️ Welcome to the Cricket Score Predictor!\n")
    runs, over, total_overs = get_user_input()
    current_rr, predicted = calculate_predictions(runs, over, total_overs)
    display_results(current_rr, predicted)


if __name__ == "__main__":
    cricket_score_predictor()
