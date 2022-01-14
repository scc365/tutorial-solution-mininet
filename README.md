# Tutorial Solution: Mininet

Solution to the Mininet tutorial for SCC365 that can be found: [here](https://github.com/scc365/tutorial-mininet)

---

This solution completes tasks 1, 2 and 3 and requires the use of the stage 7 information to run.

You can run the solution yourself like so:

```bash
sudo mn --custom ./topology.py --topo tutorialTopology \
--switch ovsk --controller remote,ip=127.0.0.1,port=6633
```

<details>
<summary>Do this with Docker 🐳</summary>
<br>
Build the container image (each time you make a change to the topology code):
<pre>
docker build --rm -t topology:latest .
</pre><br>
Run the container:
<pre>
docker run --rm -it --privileged --network host --name topology topology:latest
</pre><br>
</details>
<br>

> 💡 **Note:** a `ptcp` controller must be running on `localhost:6633`



