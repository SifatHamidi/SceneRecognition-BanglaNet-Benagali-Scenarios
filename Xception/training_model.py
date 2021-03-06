# -*- coding: utf-8 -*-
"""Training Model


"""

model = Sequential()
xception = Xception(include_top=False, 
               weights='imagenet' , 
               input_shape = (Dim, Dim, 3), 
               pooling='avg')
model.add(xception)
model.add(Dense(64, kernel_regularizer = l2(0.001), activation = 'sigmoid'))
model.add(Dropout(0.25))
model.add(Dense(64, kernel_regularizer = l2(0.001),activation = 'sigmoid'))
model.add(Dropout(0.25))
model.add(Dense(Num_class, activation = 'softmax'))


print('finished loading model.')

model.compile(optimizer = Adam(lr=3e-4),
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'])

model.summary()

cb_early_stopper = EarlyStopping(monitor = 'val_loss',patience = 10)

cb_checkpointer=ModelCheckpoint(filepath='/content/drive/My Drive/BanglaNet/xception.hdf5',
                               monitor = 'val_loss',
                               save_best_only = True,
                               mode = 'auto')

reducelr=ReduceLROnPlateau(monitor = 'val_loss', 
                           factor = 0.2, 
                           patience = 5, 
                           min_lr = 5e-4)
csv_logger = CSVLogger('xception.csv', append=True, separator=',') #csv file creating of training accuracies

logdir = os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir, histogram_freq=1)

fit_history=model.fit(train_gen,steps_per_epoch = train_steps_per_epoch,
                      epochs = 50, validation_data=val_gen,
                      validation_steps = val_steps_per_epoch,
                      callbacks = [cb_checkpointer,cb_early_stopper,reducelr, tensorboard_callback, csv_logger])


%tensorboard --logdir logs
