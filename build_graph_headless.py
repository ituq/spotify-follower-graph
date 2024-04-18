from Session import Session
from pyvis.network import Network
from UserProfile import UserProfile
import shutil
def build_graph(depth_limit,starting_id):
    print(f"id: {starting_id},{type(starting_id)} depth: {depth_limit},{type(depth_limit)}")
    graph=Network(directed=True,height="1080px")
    sesh=Session()
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
    graph.show(starting_id+".html",notebook=False)
    # html is now in top level directory so we move it to the graphs folder
    shutil.move(starting_id+".html","static/graphs/"+starting_id+".html")
