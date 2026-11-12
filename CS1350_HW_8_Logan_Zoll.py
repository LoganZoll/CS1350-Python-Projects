
def practice_3_complete_pattern():
    def process_file(filename):
        file = None
        try:
            file = open(filename, 'r')
        except FileNotFoundError:
            return "File was not found"
        except PermissionError:
            return "Insufficient permissions"
        else:
            return file.read()
        finally:
            if file:
                file.close()

    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    print('\n'*3)

    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            if self.resource != None:
                raise RuntimeError('already acquired something')
            else:
                self.resource='acquired'

        def release(self):
            self.resource = None

        def use(self):
            if self.resource:
                print("used")
            else:
                raise RuntimeError('nothing acquired to use')
    rm = ResourceManager("Database")

    try:
        rm.acquire()
    except RuntimeError as e:
        print(e)
    else:
        print("acquired")
    finally:
        rm.release()

    try:
       rm.use()
    except RuntimeError as e:
       print(e)
    else:
        print("Used")
    finally:
        rm.release()

    rm.acquire()
    try:
        rm.acquire()
    except RuntimeError as e:
        print(e)
    else:
        print("acquired")
    finally:
        rm.release()

    

def practice_2_custom_exceptions():
        class GameError(Exception):
            pass

        class InvalidMoveError(GameError):
            def __init__(self, pos, reason):
                super().__init__(f"{pos} was not valid because: {reason}")

        class GameOverError(GameError):
            def __init__(self, winner):
                super().__init__(f"game has ended. Winner: {winner}")

        class TicTacToe:
            def __init__(self):
                self.board = [[' ' for _ in range(3)] for _ in range(3)]
                self.current_player = 'X'
                self.game_over = False

            def make_move(self, row, col):
                if(self.game_over):
                    raise GameOverError(self.current_player)
                if(row > 2 or row < 0 or col > 2 or col < 0):
                    raise InvalidMoveError([row, col], 'Position out of bounds')
                if(self.board[row][col] != ' '):
                    raise InvalidMoveError([row,col], 'Position taken')

                self.board[row][col] = self.current_player
                self.current_player = "O" if self.current_player == "X" else "X"

        game = TicTacToe()

        test_moves = [
                (0, 0),
                (0, 0),
                (5, 5),
                ]
        for row, col in test_moves:
            try:
                game.make_move(row,col)
                print(F"Move ({row}, {col}) successful")
            except InvalidMoveError as e:
                print(f"Invalid move: {e}")
            except GameOverError as e:
                print(f"Game over: {e}")

    

import os

def practice_3_complete_system():
    
    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            file = None

            try:
                file = open(filename, 'r')
            except FileNotFoundError:
                self.failed_files.append(filename)
                return "File was not found"
            except PermissionError:
                self.failed_files.append(filename)
                return "Insufficient permissions"
            except Exception:
                self.failed_files.append(filename)
                return "Something went wrong"
            else:
                self.processed_files.append(filename)
                return "Processed"
            finally:
                if file:
                    file.close()
            

        def process_directory(self, directory):
            files = None
            successes = []
            fails = []
            try:
                files = os.listdir(directory)
            except FileNotFoundError:
                return "Directory not found"
            except PermissionError:
                return "Insufficient permissions"
            except Exception:
                return "Something went wrong"
            else:
                for filename in files:
                    status = self.process_file(filename)
                    print(status)
                    if(status != "Processed"):
                        self.failed_files.append(filename)
                    else:
                        self.processed_files.append(filename)

        def get_report(self):
            report = ''
            report += '\n'
            report += 'Processed Files:'
            for filename in self.processed_files:
                report += '\n\t'+filename
            report += '\nFailed files:'
            for filename in self.failed_files:
                report += '\n\t'+filename
            return report

    processor = FileProcessor()

    test_files = [
            "valid.txt",
            "missing.txt",
            "/root/restricted.txt"
            ]
    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")








practice_3_complete_pattern()
print('\n')
practice_2_custom_exceptions()
print('\n')
practice_3_complete_system()
