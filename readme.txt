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
  User.query.filter((User.username.like('z%')).all() #单个模糊条件
  from sqlalchemy  import and_,or_,not_
  多条件： and_ ,  or_, not_
  User.query.filter(or_(User.username.like('z%'), User.username.like('%i%')).all() #多个条件模糊检索取并集,或条件
  User.query.filter(and_(User.username.like('z%'), User.username.like('%i%')).all() #多个条件模糊检索取交集,且条件
  User.query.filter(not_(User.username.like('z%'), User.username.like('%i%')).all() #表示非条件的
  补充 ： __gt__. __lt__, __ge__(gt equal),__le__ (le equal) --->>>通常应用在范围（整型，日期）
        也可以用< > <= >= !=
        User.age__lt__(18)或 User.age>18
         User.age.between(18, 30)

   User.query.filter(User.phone.in_(['1','2'])).all()  #

   #排序 order_by
   user6 = User.query.filter(User.username.contains('%s%')).order_by('rdatatime').all()#升序
   user6 = User.query.filter(User.username.contains('%s%')).order_by(-User.ratatime).all()#降序
   #限制 limit
   user8 = User.query.limit(2).all() #默认获取二条记录
   user8 = User.query.offset(2).limit(2).all()#跳过二条记录在获取二条












