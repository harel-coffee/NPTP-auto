
basicArchitecture=hyperParams.iloc[paramNr].basicArchitecture
currentLR=hyperParams.iloc[paramNr].learningRate
dropout=hyperParams.iloc[paramNr].dropout
graphLayers=hyperParams.iloc[paramNr].graphLayers
denseLayers=hyperParams.iloc[paramNr].denseLayers





import deepchem.feat
import deepchem.feat.mol_graphs
import deepchem.metrics




exec(open(scrip_path+'graphModels.py').read(), globals())



seed=123
if basicArchitecture=="GraphConv":
  model=MyGraphConvTensorGraph(n_tasks=nrOutputTargets, graph_conv_layers=graphLayers, dense_layer_size=denseLayers, batch_size=batchSize, dropout=dropout, learning_rate=currentLR, use_queue=True, random_seed=seed, mode='classification', configproto=gpu_options, verbose=False, mycapacity=5)
  singleFunc=convFunc
  batchFunc=convInput

if not model.built:
  model.build()
  with model._get_tf("Graph").as_default():
    updateOps=tf.get_collection(tf.GraphKeys.UPDATE_OPS)

