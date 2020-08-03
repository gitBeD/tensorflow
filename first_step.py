import tensorflow as tf

# graphen erzeugen
node_cons_1 = tf.constant(3.0, tf.float32, name = 'constant_1')
node_cons_2 = tf.constant(4.0, tf.float32, name = 'constant_2')

node_add = tf.add(node_const1, node_const2)

a = tf.placeholder(tf.float32, name= 'a')
node_mul = node_a * a

b = tf.Variable(1,0, tf.float32, name = 'b')
node_sub = node_mul - b

#ausführen
with tf.Session() as session:
    writer = tf.summary.FileWriter('./first_step', session.graph)
    init = tf.global_variables_initializer()
    #quelltext hat ein Leerzeichen vor initializer()
    print(session.run(node_sub, {a:2.0}))

writer.close()