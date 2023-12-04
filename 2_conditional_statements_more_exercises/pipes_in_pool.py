pool_volume = float(input())
first_pipe_debit_h = float(input())
second_pipe_debit_h = float(input())
hours_worker_gone = float(input())

pipe_1 = first_pipe_debit_h * hours_worker_gone
pipe_2 = second_pipe_debit_h * hours_worker_gone
pool_filled_while_worker_is_gone = pipe_2 + pipe_1

percentage_filled = pool_filled_while_worker_is_gone / pool_volume
pipe_1_percentage = pipe_1 / (pipe_2 + pipe_1)
pipe_2_percentage = pipe_2 / (pipe_2 + pipe_1)

if pool_volume >= pool_filled_while_worker_is_gone:
    print(f"The pool is {percentage_filled * 100:.2f}% full."
          f" Pipe 1: {pipe_1_percentage * 100:.2f}%. Pipe 2: "
          f"{pipe_2_percentage * 100:.2f}%.")
else:
    print(f"For {hours_worker_gone:.2f} hours the pool overflows "
          f"with {pool_filled_while_worker_is_gone - pool_volume:.2f} liters.")
