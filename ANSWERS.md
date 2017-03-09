Questions and Answers to Scaling
================================


**How would you measure the performance of your service?**

- Performance can be measured with benchmarking tools such as wrk ( https://github.com/wg/wrk )


- Example test : 

	./wrk -t12 -c400 -d30s http://127.0.0.1:8000/                                                                                                                                              ⏎ [32d11h41m]
	Running 30s test @ http://127.0.0.1:8000/
	  12 threads and 400 connections
	  Thread Stats   Avg      Stdev     Max   +/- Stdev
	    Latency    25.37ms    3.29ms 252.88ms   89.92%
	    Req/Sec     1.30k   195.09     9.89k    87.56%
	  466344 requests in 30.10s, 58.26MB read
	Requests/sec:  15494.99
	Transfer/sec:      1.94MB


- Requires a lua script to post the image data. TODO



**What are some strategies you would employ to make your service more scalable?**


- Use more processes for the application. Also use a asyncio compatible application server. ( http://uwsgi-docs.readthedocs.io/en/latest/asyncio.html )

- To become more scalable I would move to ascii_to_art task into a celery function, which would require settings up a broker for celery. Once we have a broker it would make the API stop blocking with the numpy operations and we would have an incredibly fast API with distributed processing workers in the backend. 

- A load balancer with multiple applications in different regions could also scale out the application. Either HAProxy or Elastic Load Balancer (Amazon only).



**How would your design change if you needed to store the uploaded images?**

- I would add another task in asciify/tasks.py for storing the image into S3 or another storage space. This would also need to be added as a celery task to stop the API from blocking.



**What are the cost factors of your scaling choices? Which parts of your solution would grow in cost the fastest?**

- Scaling out would require additional cloud instances for the applications, as well as server for the load balancer. 

- The costs required for implementing celery would require a broker either in a single server, or multiple servers if we want the broker distributed. Either RabbitMQ or Redis.



**Where are your critical points of failure and how would you mitigate them?**

- Points of failure would be the single application that is currently running. You can mitigate this with multiple application servers behind a load balancer. 

- Another point of failure would be the broker with celery. This could be mitigated by making sure the broker is distributed such as a RabbitMQ cluster.



**How given a change to the algorithm what issues do you foresee when upgrading your scaled-out solution?**

- If the algorithm were to change I would need to implement different versions in the API that can all be callable from a single endpoint. This way we can compare the speed and accuracy of each algorithm by merely providing a query paramter or endpoint specification for the specific version we want to test.

- I would also want to include documentation for the API available via a UI so I would want to use something like sanic-openapi ( https://github.com/channelcat/sanic-openapi ) for easy inline code documentation that could be automatically tranformed into a web UI.



**If you wanted to migrate your scaled-out solution to another cloud provider (with comparable offerings but different API’s) how would you envision this happening? How would deal with data consistency during the transition and rollbacks in the event of failures?**

- Make a checklist of all application components. 
- Evaluate costs for transition to comparable cloud flavors.
- Build configuration management / provisioning solutions to quickly deploy your application to any environment, preferable with tools such as Terraform. 
- Test with a staging environment to ensure successful migration.
- Build rollback solutions into the terraform execution plans.
