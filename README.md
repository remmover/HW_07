# clean_folder

Clean_folder is a Python script that helps organize files in a specified directory by categorizing them into different folders based on their file extensions. It provides a simple and convenient way to keep your files organized and easily accessible.

## Installation

You can install clean_folder using pip:

```bash
pip install clean_folder
```

## Usage

Once installed, you can run clean_folder from the command line:

```bash
clean-folder <path_to_folder>
```

Replace `<path_to_folder>` with the path to the folder you want to organize. The script will categorize the files in that folder and move them into respective subfolders based on their file extensions.

The following categories are supported:

- Audio files: .mp3, .ogg, .wav, .amr
- Image files: .jpeg, .png, .jpg, .svg
- Video files: .avi, .mp4, .mov, .mkv
- Document files: .doc, .docx, .txt, .pdf, .xlsx, .pptx
- Archive files: .zip, .gz, .tar

Files with unrecognized extensions will be moved to an "unknown" folder.

**Note:** The script assumes that the target folder and its subfolders are writable. Please make sure you have the necessary permissions before running the script.

## Example

Suppose you have a folder called "Downloads" with the following files:

```
Downloads
├── audio.mp3
├── image.png
├── document.docx
├── video.mp4
├── script.py
└── README.txt
```

To organize the files in the "Downloads" folder, you can run:

```bash
clean-folder Downloads
```

After running the script, the folder structure will be updated as follows:

```
Downloads
├── audio
│   └── audio.mp3
├── image
│   └── image.png
├── document
│   └── document.docx
├── video
│   └── video.mp4
├── unknown
│   ├── script.py
│   └── README.txt
└── clean_folder
    ├── clean.py
    └── README.md
```

The files are now organized into separate folders based on their categories. The "unknown" folder contains files with unrecognized extensions, and the "clean_folder" folder contains the clean_folder script files.

## License

clean_folder is licensed under the MIT License. See [LICENSE](https://github.com/remmover/HW_07_goit/blob/main/LICENSE) for more information.

## Contact

If you have any questions, suggestions, or issues, please feel free to contact the author at igorm.200323@gmail.com.
