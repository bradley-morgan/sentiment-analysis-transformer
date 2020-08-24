# sentiment-analysis-transformer
Using transformer architecture only with BERT pre-trained weights to perform sentiment analysis on 29million amazon book reviews

- [x] Data Eng: Create config
- [x] Data Eng: Created InterableDataset stream
- [x] Data Eng: Create Plugin transform system
- [ ] Data Eng: Create and test pre-bert Tokenizer plugin
- [ ] Data Eng: Create and test Stop word removal Plugin
- [ ] Data Eng: Create and test Lemantizer plugin
- [ ] Data Eng: Create and test Punctuation/special charcter with omission removal plugin
- [ ] Data Eng: Create BERT Embedding extractor plugin 
- [ ] Data Eng: Create Glove Embedding extractor plugin 
- [ ] ML:       For Glove Embeddings: Add Vocab handler (max vocab size, min_word frequency)
- [ ] Data Eng: Create and test Statistics plugin 
- [ ] Data Eng: Label Balancer to make sure roughly equal amounts of each label to some threshold (doesnt have to be exact)
- [ ] Data Eng: Label normalizer plugin (normalise values between 0-1)
- [ ] Data Eng: Optmize with multi-threading (check that pytorch uses full cpu capacity all 6 of them)
- [ ] Data Eng: Optional: if multithreading not enough add multiprocessing
- [ ] Data Eng: Optional: Add Cython optimisations where applicable
- [ ] ML:       Create a custom transformer and train it on sentiment data
- [ ] ML:       Use dash to create training metrics and paramters
- [ ] ML:       Implement Basyian optimisation

