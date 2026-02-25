from file_manager import FileManager
from ui_manager import UIManager

if __name__ == "__main__":
    file_manager = FileManager()
    ui_manager = UIManager(file_manager)
    ui_manager.run()