import requests
import math

class FileInfo:
    def __init__(self, url):
        self.url = url

    def get_file_info(self):
        response = self._send_head_request()

        file_size = self._get_file_size(response)
        mime_type = self._get_mime_type(response)
        status_code = response.status_code

        return file_size, mime_type, status_code

    def _send_head_request(self):
        return requests.head(self.url)

    def _get_file_size(self, response):
        file_size = int(response.headers.get('Content-Length'))
        return file_size

    def _get_mime_type(self, response):
        mime_type = response.headers.get('Content-Type')
        return mime_type

    @staticmethod
    def format_file_size(file_size, unit='bytes'):
        if unit == 'bytes':
            return file_size
        elif unit == 'kB':
            return file_size / 1024
        elif unit == 'MB':
            return file_size / (1024 * 1024)
        elif unit == 'GB':
            return file_size / (1024 * 1024 * 1024)
        else:
            raise ValueError(f"Invalid unit: {unit}")

