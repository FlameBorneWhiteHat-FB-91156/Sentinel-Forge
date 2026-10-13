"""
Rule-Based PC Diagnostic Assistant
Author: David Fulmer

This program demonstrates a simple rule-based AI system.
It does not use machine learning. Instead, it checks the user's
input for predefined keywords and follows IF-ELIF-ELSE rules.
"""

def diagnose_issue(description):
    """Return troubleshooting advice based on predefined rules."""
    problem = description.lower().strip()

    # Rule 1: Power problems
    if any(keyword in problem for keyword in [
        "no power", "won't turn on", "wont turn on", "will not turn on",
        "dead", "not powering", "power issue"
    ]):
        return (
            "POWER DIAGNOSIS:\n"
            "1. Verify the power cable is connected at both ends.\n"
            "2. Check the outlet or surge protector with another device.\n"
            "3. If this is a desktop, confirm the power-supply switch is ON.\n"
            "4. Disconnect unnecessary peripherals and try powering on again.\n"
            "5. If there are still no lights or fans, the power supply or motherboard may need testing."
        )

    # Rule 2: Display problems
    elif any(keyword in problem for keyword in [
        "black screen", "no display", "screen is blank", "blank screen",
        "monitor", "no signal", "display issue"
    ]):
        return (
            "DISPLAY DIAGNOSIS:\n"
            "1. Confirm the monitor has power and the correct input source is selected.\n"
            "2. Reseat the HDMI/DisplayPort cable on both ends.\n"
            "3. If available, test another cable or monitor.\n"
            "4. On a desktop with a graphics card, make sure the display cable is connected to the GPU.\n"
            "5. If the system powers on but never displays an image, RAM or GPU seating may need to be checked."
        )

    # Rule 3: Network problems
    elif any(keyword in problem for keyword in [
        "wifi", "wi-fi", "internet", "network", "offline",
        "can't connect", "cant connect", "no connection"
    ]):
        return (
            "NETWORK DIAGNOSIS:\n"
            "1. Confirm Wi-Fi or Ethernet is enabled and connected.\n"
            "2. Test another device on the same network.\n"
            "3. Restart the computer and router/modem.\n"
            "4. Forget and reconnect to the Wi-Fi network if applicable.\n"
            "5. If other devices work but this computer does not, check its network adapter settings."
        )

    # Rule 4: Performance problems
    elif any(keyword in problem for keyword in [
        "slow", "lag", "lagging", "freeze", "freezing",
        "stutter", "performance", "takes forever"
    ]):
        return (
            "PERFORMANCE DIAGNOSIS:\n"
            "1. Open Task Manager and check CPU, memory, disk, and GPU usage.\n"
            "2. Close unnecessary programs and browser tabs.\n"
            "3. Check available storage space.\n"
            "4. Restart the computer if it has been running for a long time.\n"
            "5. If one resource stays near 100%, investigate the process using that resource."
        )

    # Rule 5: Heat / fan problems
    elif any(keyword in problem for keyword in [
        "overheat", "overheating", "too hot", "hot", "fan loud",
        "fans loud", "thermal", "temperature"
    ]):
        return (
            "THERMAL DIAGNOSIS:\n"
            "1. Make sure air vents are not blocked.\n"
            "2. Check that all cooling fans are spinning.\n"
            "3. Remove dust from filters, fans, and heatsinks.\n"
            "4. Check CPU/GPU temperatures with a monitoring utility.\n"
            "5. If temperatures remain unusually high, inspect cooler mounting and thermal paste."
        )

    # Fallback rule when no known pattern is found
    else:
        return (
            "GENERAL DIAGNOSIS:\n"
            "I do not have a specific rule for that description yet.\n"
            "Start by restarting the computer, checking cables/connections, and noting any error messages.\n"
            "Then describe the symptom more specifically, such as 'black screen,' 'no internet,' 'slow,' or 'overheating.'"
        )


def main():
    print("Rule-Based PC Diagnostic Assistant")
    print("----------------------------------")
    print("Describe a computer problem and I will apply predefined troubleshooting rules.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("Describe the problem: ")

        if user_input.lower().strip() == "quit":
            print("Exiting diagnostic assistant.")
            break

        print()
        print(diagnose_issue(user_input))
        print()


if __name__ == "__main__":
    main()
