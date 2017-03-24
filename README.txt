This program has been created by:-

Tapesh Mandal  M.Tech. CSE (Advanced Networks)

The datasets have to be included in the program manually. And the value of the variable rs has to be set manually to nC3 where n is the number of vertices in the graph.

For example for karate.pickle :-

pg=pg.Read_Pickle("karate.pickle")

for v in pg["karate"].vs():
    g.add_vertex(v)

for e in pg["karate"].es():
    g.add_edge(e.source,e.target)

The datasets in the repository were downloaded from nexus.igraph repository. In case you are not able to download them from the nexus repository, they are available at https://networkdata.ics.uci.edu/index.php , but in .gml format which is much more easier to use.

Example:

g =ig.Graph()

g=g.Read_GML("karate.gml")


For any further queries please contact me at <tapesh.mandal@gmail.com>
