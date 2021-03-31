import logging

import src.utils.config as config

from http.server import HTTPServer, SimpleHTTPRequestHandler


class CORSRequestHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(CORSRequestHandler, self).end_headers()

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length).decode()

        dict = {}

        for info in data.split('&'):
            platform, uname = info.split('=')

            if not uname == '':
                logging.info(f'Recognized update: {info}')
                if uname == 'none':
                    dict[platform] = None
                else:
                    dict[platform] = uname

        config.update_keys(dict)


def run():
    with HTTPServer(('', 5001), CORSRequestHandler) as server:
        logging.info('Server started')
        server.serve_forever()
