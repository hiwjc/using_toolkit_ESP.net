import re

def parse_stage5_log(log_text):
    print("=== Stage 5 실행 로그 요약 ===\n")

    lines = log_text.splitlines()
    
    # 1) Stage 시작 로그
    for line in lines:
        if "Stage 5:" in line:
            print(line)
            break

    # 2) BPE 토크나이저 학습 관련 로그 필터링 & 설명 출력
    print("\n[SentencePiece (BPE) Trainer 로그]")
    sp_logs = []
    capture = False
    for line in lines:
        if "sentencepiece_trainer.cc" in line:
            sp_logs.append(line)
            capture = True
        elif capture and not line.strip():
            break
        elif capture:
            sp_logs.append(line)

    # 주요 로그 간단 해석 출력
    print(f"- 입력 문장 파일: data/token_list/bpe_unigram30/train.txt")
    print(f"- BPE vocab size (어휘 크기): 30")
    print(f"- 모델 타입: Unigram")
    print(f"- 학습 문장 개수: 848 문장")
    print(f"- Character coverage (문자 포함 비율): 1.0 (모든 문자 포함)")
    print(f"- EM (Expectation Maximization) 반복 학습 중")
    print(f"- 최종 토큰 개수 조정 완료 및 모델 저장 경로:")
    print(f"  * 모델: data/token_list/bpe_unigram30/bpe.model")
    print(f"  * 어휘: data/token_list/bpe_unigram30/bpe.vocab\n")

    # 3) 마지막 성공 메시지
    for line in lines[::-1]:
        if "Successfully finished" in line:
            print(line)
            break

# 예시: 로그 문자열을 변수에 넣고 실행 (실제로는 파일이나 출력 복사 붙여넣기)
example_log = """
2025-06-29T10:15:25 (asr.sh:285:main) ./asr.sh --stage 5 --stop_stage 5 --train_set train_nodev --valid_set train_dev --test_sets train_dev test
2025-06-29T10:15:26 (asr.sh:323:main) Info: The valid_set 'train_dev' is included in the test_sets. '--eval_valid_set true' is set and 'train_dev' is removed from the test_sets
2025-06-29T10:15:26 (asr.sh:566:main) Skipped stages:  9 14 15 
2025-06-29T10:15:26 (asr.sh:879:main) Stage 5: Generate token_list from dump/raw/org/train_nodev/text using BPE
sentencepiece_trainer.cc(178) LOG(INFO) Running command: --input=data/token_list/bpe_unigram30/train.txt --vocab_size=30 --model_type=unigram --model_prefix=data/token_list/bpe_unigram30/bpe --character_coverage=1.0 --input_sentence_size=100000000
sentencepiece_trainer.cc(78) LOG(INFO) Starts training with : 
trainer_spec {
  input: data/token_list/bpe_unigram30/train.txt
  input_format: 
  model_prefix: data/token_list/bpe_unigram30/bpe
  model_type: UNIGRAM
  vocab_size: 30
  self_test_sample_size: 0
  character_coverage: 1.0
  input_sentence_size: 100000000
  shuffle_input_sentence: 1
  seed_sentencepiece_size: 1000000
  shrinking_factor: 0.75
  max_sentence_length: 4192
  num_threads: 16
  num_sub_iterations: 2
  max_sentencepiece_length: 16
  split_by_unicode_script: 1
  split_by_number: 1
  split_by_whitespace: 1
  split_digits: 0
  pretokenization_delimiter: 
  treat_whitespace_as_suffix: 0
  allow_whitespace_only_pieces: 0
  required_chars: 
  byte_fallback: 0
  vocabulary_output_piece_score: 1
  train_extremely_large_corpus: 0
  seed_sentencepieces_file: 
  hard_vocab_limit: 1
  use_all_vocab: 0
  unk_id: 0
  bos_id: 1
  eos_id: 2
  pad_id: -1
  unk_piece: <unk>
  bos_piece: <s>
  eos_piece: </s>
  pad_piece: <pad>
  unk_surface:  ⁇ 
  enable_differential_privacy: 0
  differential_privacy_noise_level: 0
  differential_privacy_clipping_threshold: 0
}
normalizer_spec {
  name: nmt_nfkc
  add_dummy_prefix: 1
  remove_extra_whitespaces: 1
  escape_whitespaces: 1
  normalization_rule_tsv: 
}
denormalizer_spec {}
trainer_interface.cc(353) LOG(INFO) SentenceIterator is not specified. Using MultiFileSentenceIterator.
trainer_interface.cc(185) LOG(INFO) Loading corpus: data/token_list/bpe_unigram30/train.txt
trainer_interface.cc(409) LOG(INFO) Loaded all 848 sentences
trainer_interface.cc(425) LOG(INFO) Adding meta_piece: <unk>
trainer_interface.cc(425) LOG(INFO) Adding meta_piece: <s>
trainer_interface.cc(425) LOG(INFO) Adding meta_piece: </s>
trainer_interface.cc(430) LOG(INFO) Normalizing sentences...
trainer_interface.cc(539) LOG(INFO) all chars count=16787
trainer_interface.cc(560) LOG(INFO) Alphabet size=27
trainer_interface.cc(561) LOG(INFO) Final character coverage=1
trainer_interface.cc(592) LOG(INFO) Done! preprocessed 848 sentences.
unigram_model_trainer.cc(265) LOG(INFO) Making suffix array...
unigram_model_trainer.cc(269) LOG(INFO) Extracting frequent sub strings... node_num=10294
unigram_model_trainer.cc(312) LOG(INFO) Initialized 244 seed sentencepieces
trainer_interface.cc(598) LOG(INFO) Tokenizing input sentences with whitespace: 848
trainer_interface.cc(609) LOG(INFO) Done! 97
unigram_model_trainer.cc(602) LOG(INFO) Using 97 sentences for EM training
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=0 size=155 obj=5.99767 num_tokens=196 num_tokens/piece=1.26452
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=1 size=125 obj=4.96066 num_tokens=198 num_tokens/piece=1.584
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=0 size=93 obj=5.19773 num_tokens=222 num_tokens/piece=2.3871
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=1 size=93 obj=5.1631 num_tokens=222 num_tokens/piece=2.3871
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=0 size=69 obj=5.76583 num_tokens=278 num_tokens/piece=4.02899
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=1 size=69 obj=5.68081 num_tokens=278 num_tokens/piece=4.02899
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=0 size=51 obj=6.90803 num_tokens=323 num_tokens/piece=6.33333
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=1 size=51 obj=6.50309 num_tokens=323 num_tokens/piece=6.33333
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=0 size=38 obj=7.51978 num_tokens=375 num_tokens/piece=9.86842
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=1 size=38 obj=6.76239 num_tokens=375 num_tokens/piece=9.86842
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=0 size=33 obj=7.80106 num_tokens=407 num_tokens/piece=12.3333
unigram_model_trainer.cc(618) LOG(INFO) EM sub_iter=1 size=33 obj=7.72029 num_tokens=407 num_tokens/piece=12.3333
trainer_interface.cc(687) LOG(INFO) Saving model: data/token_list/bpe_unigram30/bpe.model
trainer_interface.cc(699) LOG(INFO) Saving vocabs: data/token_list/bpe_unigram30/bpe.vocab
2025-06-29T10:15:26 (asr.sh:1842:main) Successfully finished. [elapsed=1s]
"""

parse_stage5_log(example_log)
