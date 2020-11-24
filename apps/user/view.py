#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'
from flask import Blueprint,request, render_template,redirect,url_for
from apps.user.models import User
from exts import db
import hashlib
user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            #与模型结合,拿取属性的值
            #1.找到模型类并创建对象
            user = User()
            #2.给对象的属性赋值
            user.username = username
            user.password = hashlib.md5(password.encode('utf-8')).hexdigest()
            user.phone = phone
            #添加数据至数据库
            #3.将user对象添加到session（）中【缓存】
            db.session.add(user)
            #4.将缓存的数据插入到数据库里，提交数据
            db.session.commit()
            return redirect(url_for('user.user_center'))
        else:
            return "二次密码不一致"
    return render_template('user/register.html')


@user_bp.route('/', methods=['GET', 'POST'])
def user_center():
    #查询数据库中的数据
    users = User.query.all() #select * from user;
    print(users) #[user_objA, user_objB] 返回的是数据对象
    return render_template('user/center.html', users=users)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    #获取输入的用户名和密码
    if request.method == 'POST':
        username = request.form.get('username')
        password = hashlib.md5(request.form.get('password').encode('utf-8')).hexdigest()
        #获取数据库里的数据，与账号密码匹配
        users = User.query.all()
        for user in users:
            if username == user.username and password == user.password:
                return redirect(url_for('user.user_center'))
            else:
                print("账号或密码错误")
    return render_template('user/login.html')