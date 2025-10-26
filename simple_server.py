import http.server
import socketserver
import os

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # 记录所有请求，包括404
        print(f"{self.client_address[0]} - - [{self.log_date_time_string()}] {format % args}")

# 确保在正确的目录启动服务器
os.chdir('D:\\trea\\gundong')

with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"服务器启动在端口 {PORT}")
    print(f"当前目录: {os.getcwd()}")
    print(f"scroll.html 文件存在: {os.path.exists('scroll.html')}")
    print(f"访问地址: http://localhost:{PORT}/scroll.html")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")