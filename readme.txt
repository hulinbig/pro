python，关于数据库的查询语法
1.查询：
查询所有：模型类.query.all()  --->>  select * from user;
如果有条件的查询：
            ---模型类.query.filter_by(字段名 = 查询的值)  --->> select * from user where username = 值; 获取的是符合当前输入的所有数据
            ---模型类.query.filter(字段名 = 查询的值).first() --->>select * from user where username = 值 limit...; 获取的是符合当前输入的所有数据
            ---模型类.query.get(pk)  根据主键查询用户使用get(主键值) 返回值是一个用户对象
            ---模型类.query.filter(模型类.字段名 == 查询的值).all() --->>> 模型类.query.filter(模型类.字段名 == 值)




模型类.query.filter() 里面是布尔的条件   模型类.query.filter(模型类.字段名 == 值)
模型类.query.filter_by() 里面是一个等值  模型类.query.filter_by(字段名 = 值)

***模型类.query.filter() ***
1.模型类.query.filter().all() ------>>> 列表
2.模型类.query.filter().first() ------>>> 对象
3.User.query.filter(User.username.startwith()).all()  ---->>> 类似与模糊查询  like
  User.query.filter(User.username.endwith()).all()
  User.query.filter(User.username.contains()).all()  ---->>> like '%a%'
