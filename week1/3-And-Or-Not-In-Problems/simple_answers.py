while True:
    text = input("Please write down some text: ")
    
    if "hello" in text or "Hello" in text:
        print("Hello there, good stranger")
    elif "how are you" in text:
        print("I am fine,thanks. How are you?")
    elif "feelings" in text:
        print(" am a machine.I have no feelings")
    elif "age" in text:
        print("I have no age. Only current timestamp")
    else:
        print("Sorry, I dont't understand you.Try hello,feelings or age.")
