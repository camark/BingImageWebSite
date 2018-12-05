from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from randombing import RandomBingimage
from rosnode import RosNode
from rosservice import RosService
from rostopic import RosTopic

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    bing=RandomBingimage()
    url = bing.getRandomImage()
    return render_template('home.html',url=url)

@app.route('/hello/<name>')
def hello(name):
    return '<h1>Hello %s!</h1>' % (name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def server_internal_error(e):
    return render_template('500'),500

@app.route('/rosnode')
def node_index():
    rosnode=RosNode()
    (status,list)=rosnode.list()
    return render_template('nodelist.html',nodes=list)

@app.route('/rosnode/<nodename>')
def node_detail(nodename):
    rosNode=RosNode()
    (status,nodeDetail)=rosNode.getDetail(nodename)
    return render_template('node_detail.html',detail=nodeDetail,nodename=nodename)

@app.route('/rosservice')
def service_index():
    rosnode=RosService()
    (status,list)=rosnode.list()
    return render_template('servicelist.html',nodes=list)

@app.route('/rosservicedetail')
def service_detail():
    servicename=request.args.get('servicename')
    rosService=RosService()
    (status,serviceDetail)=rosService.detail(servicename)
    return render_template('service_detail.html',detail=serviceDetail,servicename=servicename)

@app.route('/rostopic')
def topic_index():
    rosnode=RosTopic()
    (status,list)=rosnode.list()
    return render_template('topiclist.html',nodes=list)

@app.route('/rostopicdetail')
def topic_detail():
    topic_name = request.args.get('topicname')
    rostopic=RosTopic()
    (status,topicDetail) = rostopic.detail(topic_name)
    return render_template('topic_detail.html',detail=topicDetail,topicname=topic_name)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
