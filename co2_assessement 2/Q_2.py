def verify_otp_simulation(simulated_inputs):
    attempts = 0
    max_attempts = 3
    
    for otp in simulated_inputs:
        if attempts >= max_attempts:
            break
            
        print(f"Entered OTP: '{otp}'")
        if otp == "":
            print("-> Blank entry detected. Attempt does not count.")
            pass
            continue
            
        if otp == "1234":
            print("-> OTP Verified Successfully!")
            break
        else:
            print("-> Incorrect OTP.")
            attempts += 1
    else:
        print("-> Account is locked for 30 minutes due to 3 failed attempts.")
print("--- Q2 Outputs ---")
# Simulating: Blank (ignored), Wrong OTP, Wrong OTP, Correct OTP
verify_otp_simulation(["", "9999", "5555", "1234"])