
Setup
-----

- Install Python 3 and MondoDB.
- Start mongod server
- use local (default DB)
- Create flexDB Collection (Cmd:- use flexDB)
- pip install -U werkzeug
- pip install -r requirements.txt
- Run `setup.sh` (Linux, OS X, Cygwin) or `setup.bat` (Windows)
- Run `./webhook-server.py` to start the server
- Open `http://localhost:3000/index.html` on your web browser to run the client
=============Server Run in backgurond=================================
sudo nohup python webhook-server.py &
=========================API to be used ====================================
API- To be Use 
Post - http://127.0.0.1:3000/snp/webhooks		-- to to send notification
Get - http://127.0.0.1:3000/snp/webhooks		-- to get list of all notification

Get - http://127.0.0.1:3000/snp/webhooks/{skuId}		-- to get list of all notification based on sku
Delete - http://127.0.0.1:3000/snp/webhooks/{skuId}		-- to Delete list of all notification based on sku