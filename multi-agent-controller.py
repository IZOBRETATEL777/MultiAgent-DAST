import threading
import dast
import time

# Shared list
shared_list = []

base_url = 'http://localhost:3000/'

# Lock for thread-safe operations
list_lock = threading.Lock()

def manage_list(thread_id):
    while True:
        with list_lock:
            # Calculate share based on bidding (50:50)
            num_items = len(shared_list) // 2
            personal_list = []
            if num_items > 0:
                # Take 50% of the list
                personal_list = shared_list[:num_items]
                del shared_list[:num_items]
                new_personal_list = []
                for url in personal_list:
                    new_personal_list.extend(dast.run(url))
            else:
                personal_list = [base_url]
        
        with list_lock:
            shared_list.extend(personal_list)
            print(thread_id, shared_list, '\n\n')
        time.sleep(1)
        
# Create and start agents (2)
threads = []
for i in range(1, 2):
    thread = threading.Thread(target=manage_list, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

