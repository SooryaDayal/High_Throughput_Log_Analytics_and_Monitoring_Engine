from dask.distributed import LocalCluster, Client

def start_dask():

  cluster= LocalCluster(
    n_workers=2,      
    threads_per_worker=2, 
    memory_limit="1GB",
    dashboard_address=":8790"
    )
  client=Client(cluster)
  print(f"Dashboard available at: {client.dashboard_link}")
  return client

  