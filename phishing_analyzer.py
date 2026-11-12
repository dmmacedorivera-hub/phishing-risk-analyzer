# ==============================================================================
# AI DEVELOPMENT LOG
# ==============================================================================
# Copilot Prompt 1:
# Help me create a beginner-friendly Python program that asks a user questions 
# about a suspicious email and gives it a low, medium, or high phishing risk rating.
#
# Copilot Prompt 2:
# How can I store the detected warning signs in a Python list and display them 
# at the end of the analysis?
#
# Copilot Prompt 3:
# Add a loop to ask the user if they want to analyze another message before exiting.
#
# One problem or bug I encountered:
# The program stayed in an infinite loop because the input for analyzing another 
# message was not updating the condition variable correctly.
#
# How I fixed it:
# I formatted the loop condition using .strip().lower() to convert user input to lowercase.
#
# One change I made myself without Copilot:
# I added a personalized cybersecurity tip at the very end of the report to give 
# actionable advice to the user.
# ==============================================================================
# SHORT ANSWERS TO ASSIGNMENT QUESTIONS
# ==============================================================================
# 1. How does your program calculate the phishing risk?
# The program counts the number of "Yes" responses to warning signs. 
# 0-1 signs = LOW RISK, 2-3 signs = MEDIUM RISK, 4+ signs = HIGH RISK.
#
# 2. Why does your program use a list to store warning signs?
# A list allows the program to dynamically collect and store only the warning 
# signs that the user confirmed, making it easy to display them in the final report.
#
# 3. Why can a suspicious link be a sign of phishing?
# Suspicious links often disguise their real destination to trick users into 
# visiting fake, malicious websites designed to steal credentials.
# ==============================================================================

def analyze_phishing_risk():
    """Analyzes a suspicious message based on user answers."""
    print("\n" + "=" * 50)
    print("      PHISHING RISK ANALYZER")
    print("=" * 50)
    print("Answer the following questions with (y/n):\n")

    score = 0
    detected_signs = []

    q1 = input("1. Is this message unexpected or unsolicited? (y/n): ").strip().lower()
    if q1 == 'y':
        score += 1
        detected_signs.append("Unexpected message")

    q2 = input("2. Is the sender unknown or using a suspicious email address? (y/n): ").strip().lower()
    if q2 == 'y':
        score += 1
        detected_signs.append("Unknown or suspicious sender")

    q3 = input("3. Does the message use urgent or threatening language? (y/n): ").strip().lower()
    if q3 == 'y':
        score += 1
        detected_signs.append("Urgent or threatening language")

    q4 = input("4. Does it request passwords, credit card numbers, or personal info? (y/n): ").strip().lower()
    if q4 == 'y':
        score += 1
        detected_signs.append("Request for sensitive information")

    q5 = input("5. Does it contain suspicious or misleading links? (y/n): ").strip().lower()
    if q5 == 'y':
        score += 1
        detected_signs.append("Suspicious or misleading link")

    q6 = input("6. Does it include an unexpected file attachment? (y/n): ").strip().lower()
    if q6 == 'y':
        score += 1
        detected_signs.append("Unexpected attachment")

    if score <= 1:
        risk_level = "LOW RISK"
        recommendation = "This message appears safe, but always double-check the sender before opening links."
    elif score <= 3:
        risk_level = "MEDIUM RISK"
        recommendation = "Exercise caution. Verify the sender through an official channel before taking action."
    else:
        risk_level = "HIGH RISK"
        recommendation = "DANGER! Do not click links, open attachments, or reply. Report and delete this message immediately."

    print("\n" + "-" * 50)
    print("              ANALYSIS RESULTS")
    print("-" * 50)
    print(f"Risk Score  : {score}/6")
    print(f"Risk Level  : {risk_level}")
    print("\nDetected Warning Signs:")
    if detected_signs:
        for sign in detected_signs:
            print(f"  • {sign}")
    else:
        print("  • None detected.")

    print(f"\nRecommendation: {recommendation}")
    print("\nCybersecurity Tip: Always hover over links to inspect the actual destination URL before clicking!")
    print("-" * 50)


def main():
    while True:
        analyze_phishing_risk()
        again = input("\nDo you want to analyze another message? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for using Phishing Risk Analyzer. Stay safe online!\n")
            break


if __name__ == "__main__":
    main()
