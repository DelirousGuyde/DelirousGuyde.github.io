# devserver.py
from livereload import Server

server = Server()

# Watch common frontend file types
server.watch('*.html')
server.watch('assets/css/*.css')
server.watch('assets/js/*.js')

# Serve from current directory
server.serve(root='.', port=8888, host='0.0.0.0')
