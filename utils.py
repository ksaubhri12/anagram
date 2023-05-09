from itertools import islice


def chunk_map_keys(data, batch_size):
    it = iter(data)
    for i in range(0, len(data), batch_size):
        yield {k: data[k] for k in islice(it, batch_size)}
