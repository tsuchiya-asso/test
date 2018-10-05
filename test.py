



class Prediction :
    def __init__(
        self
        input_dim,
        time_steps,
        latent_dim_list,
        # データが一つしかないので1しか選べない
        batch_size,
        model_option,
        optimizer,
    ):
        self.input_dim = input_dim
        self.time_steps = time_steps
        self.latent_dim_list = latent_dim_list
        self.batch_size = batch_size
        self.model_option = model_option
        self.optimizer = optimizer

    def create_model
        with tf.name_scope('Model'):
            for i in range(input_dim):
                with tf.name_scope('Input' + str(i)):
                    x = Input(shape=(time_steps, 1,))

                if model_option == 'lstm':
                    with tf.name_scope('LSTM' + str(i)):
                        h = LSTM(latent_dim_list[i], stateful=False, return_sequences=True)(x)
                elif model_option == 'gru':
                    with tf.name_scope('GRU' + str(i)):
                        h = GRU(latent_dim_list[i], stateful=False, return_sequences=True)(x)

                with tf.name_scope('Dense' + str(i)):
                    out = Dense(1)(h)
                input_list.append(x)
                output_list.append(out)

            model = Model(inputs=input_list, outputs=output_list)
            model.summary()
            with tf.name_scope('ModelCompile'):
                model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mse'])

        return model

class Prediction2 :
  def __init__(self, maxlen, n_hidden, n_in, n_out):
    self.maxlen = maxlen
    self.n_hidden = n_hidden
    self.n_in = n_in
    self.n_out = n_out

  def create_model(self):
    model = Sequential()
    model.add(LSTM(self.n_hidden, batch_input_shape = (None, self.maxlen, self.n_in),
             kernel_initializer = glorot_uniform(seed=20170719),
             recurrent_initializer = orthogonal(gain=1.0, seed=20170719),
             dropout = 0.5,
             recurrent_dropout = 0.5))
    model.add(Dropout(0.5))
    model.add(Dense(self.n_out,
            kernel_initializer = glorot_uniform(seed=20170719)))
    model.add(Activation("softmax"))
    model.compile(loss="categorical_crossentropy", optimizer = "RMSprop", metrics = ['categorical_accuracy'])
    return model

  # 学習
  def train(self, x_train, t_train, batch_size, epochs) :
    early_stopping = EarlyStopping(patience=0, verbose=1)
    model = self.create_model()
    model.fit(x_train, t_train, batch_size = batch_size, epochs = epochs, verbose = 1,
          shuffle = True, callbacks = [early_stopping], validation_split = 0.1)
    return model
