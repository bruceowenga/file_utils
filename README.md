# FileUtils Python Module

The FileUtils module is a lightweight Python module that provides convenient functions to retrieve file information from a given URL. It allows you to obtain the file size, MIME type, and status code without actually downloading the entire file. This module is designed to be simple, efficient, and easy to integrate into your projects.

## Features

- Retrieve file size, MIME type, and status code from a URL
- Supports retrieval in different units: bytes, kB, MB, and GB
- Encapsulated class structure for modular usage
- Integration-ready for larger Python projects
- Utilizes the requests library for making HTTP requests

## Installation

To use the FileUtils module, you need to have Python 3.x installed on your system. Additionally, you will need to install the `requests` library, which can be installed using `pip`:

```shell
pip install requests
```

## Usage

1. Import the `FileInfo` class from the `fileUtils` module into your Python project.
2. Create an instance of the `FileInfo` class with a file URL as the input.
3. Call the appropriate methods to retrieve the desired file information, such as `get_file_size`, `get_mime_type`, or `get_status_code`.
4. Optionally, use the `format_file_size` static method to format the file size in different units.

Example usage:

```shell
from fileUtils import FileInfo

url = 'https://example.com/file.txt'
file_info = FileInfo(url)

file_size, mime_type, status_code = file_info.get_file_info()

print(f"File Size: {file_size} bytes")
print(f"MIME Type: {mime_type}")
print(f"Status Code: {status_code}")

```

## Contributing

Contributions, bug reports, and feature requests are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

## License

The FileUtils module is licensed under the [MIT License](LICENSE).

Feel free to explore and utilize the FileUtils module to simplify file information retrieval in your Python projects.
