import time
import random
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed

def execute_test_case(params):
    # Simulate some computational workload
    random.randint(0, 100)
    return True

def generate_tests_with_process_pool(num_test_cases, desc):
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(execute_test_case, _) for _ in range(num_test_cases)]
        for future in tqdm(as_completed(futures), total=num_test_cases, desc=desc):
            future.result()

def brute_force_test_generation(num_params, values_per_param):
    start_time = time.time()
    num_test_cases = (values_per_param ** num_params) * ((num_params * (num_params - 1)) // 2)
    generate_tests_with_process_pool(num_test_cases, "Brute-force Test Generation")
    end_time = time.time()
    return end_time - start_time

def optimized_bias_detection(num_params, values_per_param):
    start_time = time.time()
    num_test_cases = num_params * values_per_param * ((num_params - 1) // 2)
    generate_tests_with_process_pool(num_test_cases, "Optimized Bias Detection")
    end_time = time.time()
    return end_time - start_time

def random_selection_strategy(num_params, values_per_param):
    start_time = time.time()
    num_test_cases = num_params * ((num_params - 1) // 2)
    generate_tests_with_process_pool(num_test_cases, "Random Selection Strategy")
    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    num_params, values_per_param = 6, 6  # Example setup based on the question description

    brute_force_time = brute_force_test_generation(num_params, values_per_param)
    optimized_bias_detection_time = optimized_bias_detection(num_params, values_per_param)
    random_selection_strategy_time = random_selection_strategy(num_params, values_per_param)

    print(f"Brute-force method time: {brute_force_time} seconds")
    print(f"Optimized bias detection time: {optimized_bias_detection_time} seconds")
    print(f"Random selection strategy time: {random_selection_strategy_time} seconds")



# (base) dong@MacBook-Pro Downloads % python process_dataset.py
# Brute-force Test Generation: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████| 699840/699840 [01:22<00:00, 8454.41it/s]
# Optimized Bias Detection: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 72/72 [00:00<00:00, 7496.15it/s]
# Random Selection Strategy: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 12/12 [00:00<00:00, 7977.75it/s]
# Brute-force method time: 97.89599084854126 seconds
# Optimized bias detection time: 0.5807149410247803 seconds
# Random selection strategy time: 0.5198347568511963 seconds
# (base) dong@MacBook-Pro Downloads % 