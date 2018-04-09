import os

# CLUSTERING

min_df = 2
max_df = 1.0

max_tfidf_vocab = 300

kmeans_n_init = 10
kmeans_max_iter = 10000

clustering = "question"
n_clusters = 5 if clustering == "context" else 6


# TRAINING


num_epochs = 10
batch_size = 30
val_batch_size = 500

max_question_length = 30
max_context_length = 400

embedding_size = 300

encoding_size = 64

clustering = True

data_dir = "data/squad/"
train_dir = "model/k-match-lstm"

if not os.path.exists(train_dir):
    os.makedirs(train_dir)

vocab_path = data_dir + "/vocab.dat"
embed_path = data_dir + "/glove.npz"

dropout_keep_prob = 0.9
regularization_constant = 0.001

train_embeddings = False

optimizer = "adam"

learning_rate = 0.001
decay_steps = 1000
decay_rate = 0.96

max_gradient = 10.0

load_model = False


def get_paths(mode):
    questions = data_dir + "/%s.ids.questions" % mode
    contexts = data_dir + "/%s.ids.contexts" % mode
    answers = data_dir + "/%s.spans" % mode
    labels = data_dir + "/%s.labels" % mode

    return questions, contexts, answers, labels


questions_train, contexts_train, answers_train, labels_train = \
    get_paths("train")

questions_val, contexts_val, answers_val, labels_val = \
    get_paths("val")
