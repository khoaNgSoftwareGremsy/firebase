# FIBASE DATA PUSH
	Ứng dụng đẩy dữ liệu từ file excel lên trên server của firestore 
	
## PREREQUISITE

### INSTALL PANDAS 
* Pandas là một module mở rộng được viết bằng python dùng để cung cấp các cấu trúc dạng bảng, giao tiếp với file excel
* Để chạy trên các hệ điều hành hoặc môi trường giả lập cần có có cài đặt python 3. Ưu tiên >= 3.8
- INSTALL pandas in Ubuntu by pip: sudo pip install pandas
### INSTALL ADMIN SDK 
* Admin SDK có hỗ trợ nhiều nền tảng ngôn ngữ khác nhau: Node.js , java, python, Go, C#
* Trong dự án này sẽ sử dụng python để đẩy dữ liệu lên bằng SDK
- Install Admin sdk: $ sudo pip install firebase-admin
- Khởi tạo SDK:
	+ Tạo project trong firebase 
	+ Trong console của project sau khi được tạo, vào Project settings > Service Account
	+ Click Generate New Private Key -> Generate Key 
	+ Lưu file JSON vừa tải về vào chung thư mục của file code 
		
## HOW TO RUN AND UPLOAD DATA
- Trong mục "add credentials to app" đổi dường dần thành đường dẫn đến file JSON vừa tải
- Đổi đường dẫn đến mục data thành dường dẫn đến file excel muốn đẩy lên trên firestore
- Thay đổi các thuộc tính (cột) theo file muốn gửi
- Ở ngoài terminal nhập lệnh: python3 adminSDK.py

## Reference

https://pandas.pydata.org/pandas-docs/stable/reference/index.html
https://firebase.google.com/docs/admin/setup




