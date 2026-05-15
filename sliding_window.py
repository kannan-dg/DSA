# Fixed window

def fixed_size_sliding_window(arr, k):
    low = 0
    # 'high' acts as the right pointer of your window
    for high in range(len(arr)):
        
        # Step 1: Process the current element at 'high' 
        # (e.g., add to window sum, update frequencies, etc.)
        
        # Calculate current window size: (high - low + 1)
        window_size = high - low + 1
        
        # Step 2: Once the window reaches the desired size 'k'
        if window_size == k:
            # Step 2a: Calculate/update the answer based on the current window
            
            # Step 2b: Prepare to slide the window.
            # Remove or subtract the element at 'low' before moving it
            
            # Slide the left pointer forward
            low += 1
            
    return  # your final answer
