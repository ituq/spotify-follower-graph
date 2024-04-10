from Session import Session
from pyvis.network import Network
from UserProfile import UserProfile
graph=Network(directed=True,height="1000px")
sesh=Session()
depth_limit=1
starting_id="6rv5h4xn1mo8q0i83b3jcx9g0"
graph.add_node(starting_id,label="Base",shape="dot",color='#f7071f')
visited={id:True}
#breadth-first-search method that's run from the input profile
def bfs(lvl, curr,limit, graph:Network):
    #curr is list of UserProfile
    if(lvl>limit):
        return
    next=[]
    for profile in curr:
        visited[profile]=True
        neighbours=profile.getFollowers()
        for i in range(min(len(neighbours),50)):
            follower=neighbours[i]
            if(follower in visited):
                continue
            next.append(follower)
            graph.add_node(follower.id,label=follower.name,shape="circularImage",image=follower.profile_picture_URL)
            graph.add_edge(follower.id,profile.id)
            visited[follower]=True
    bfs(lvl+1,next,limit,graph)

bfs(0,[UserProfile("base",starting_id,'',sesh)],depth_limit,graph)
graph.show("graph.html")
