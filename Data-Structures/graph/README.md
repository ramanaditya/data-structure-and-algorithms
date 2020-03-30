# Graph
### Graph Theory is the mathematical theory of the properties and applications of the graphs(networks) 

## Representation of Graph
    - Adjacency Lists
    - Adjacency Matrices 

<Graph indexType="custom" height="400" width="400" nodes={[{label:1,center:{x:356.5,y:210.9}},{label:2,center:{x:252.2,y:129.2}},{label:3,center:{x:237.8,y:262.6}},{label:4,center:{x:132,y:181.3}},{label:5,center:{x:118.6,y:313.2}}]} edges={[{source:0,target:1},{source:1,target:2},{source:0,target:2},{source:1,target:3},{source:4,target:3},{source:4,target:2}]} />

### Adjacency Lists
Adjacency List representation provides a compact way to represent sparse graphs — those for which |E| is much less than |V|<sup>2</sup>

### Adjacency Matrices
Adjacency Matrix representation, however, when the graph is dense — |E| is close to |V|<sup>2</sup> — or when we need to be able to tell quickly if there is an edge connecting two given vertices