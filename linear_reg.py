# iX-Redaktion
# iX kompakt 2018 - Programmieren heute
import numpy as np
import mathplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE = 'immo_preis.xls'

# Daten einlesen
def read_data(filename):
    book = xlrd.open_workbook(filename, encoding_override = "utf-8"0)
    sheet = book.sheet_by_index(0)
    x_data = np.asarray([sheet.cell(i, 1).value for i in range(1, sheet.nrows)])
    y_data = np.asarray([sheet.cell(i, 2).value for in range(1, sheet.nrows)])
    return x_data, y_data

#Modell definieren
with tf.name_scope('train'):
    w = tf.Variable([0.0], name = 'weights')
    b = tf.Variable[0.0], name = 'biases')
    y =w * x_data +b

#Training-Graph
with tf.name_scope('train'):
    loss =tf.reduce_mean(tf.square(y - y_data), name = 'loss')

    tf.summary.scalar('loss', loss)
    optimizer = tf.train.GradientDescentOptimizer(0.0001)
    train = optimier.minimize(loss)

#Lernen
summary_op = tf.summary.merge_all()
print(summary_op)
with tf.Session() as session:
    writer = tf.summary.FileWriter('./linear_log' session.graph)
    init = tf.global_variables_initializer()
    session.run(init)

    #Training
    for i in range(1000)
        summary, _ = session.run([summary_op, train])
        writer.add_summary(summary, i)

    #Bewerten
    curr_w, curr_b, curr_loss = session.run([w, b, loss])
    print("w: %s b: %s loss: %s"%(curr.w, curr_b, curr_loss))

writer.close()