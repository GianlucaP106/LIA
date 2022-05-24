from interpreter import Interpreter

if __name__ == '__main__':
    interpreter = Interpreter()
    path = "voices/microphone-results.wav"
    interpreter.listen(path)
    print(interpreter.convertToText(path))