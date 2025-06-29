# a few seconds
!./asr.sh --stage 1 --stop_stage 1 --train_set train_nodev --valid_set train_dev --test_sets "train_dev test"


import os

def list_prepared_data():
    print("\n========================")
    print("[Data Summary - data/] directory")
    print("========================")

    data_dir = "data"
    sets = ["train", "train_nodev", "train_dev", "test"]
    for subset in sets:
        subset_path = os.path.join(data_dir, subset)
        if os.path.isdir(subset_path):
            print(f"\n {subset_path}")
            print("  ├─ Contains:")
            for f in sorted(os.listdir(subset_path)):
                print(f"  │   - {f}")
            if "train_nodev" in subset:
                print("  └─  Usage: Training set (no dev)")
            elif "train_dev" in subset:
                print("  └─  Usage: Validation (dev) set")
            elif "test" in subset:
                print("  └─  Usage: Test set")
            elif "train" in subset:
                print("  └─  Usage: Full training set")
        else:
            print(f"\n {subset_path} not found.")

# 실행 예시
list_prepared_data()
