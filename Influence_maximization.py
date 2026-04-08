import networkx as nx
import random

def simulate_spread(G, seed_set, p=0.3):
    active_nodes = set(seed_set)
    newly_active = set(seed_set)
    while newly_active:
        next_active = set()
        for node in newly_active:
            for neighbor in G.neighbors(node):
                if neighbor not in active_nodes:
                    if random.random() < p:
                        next_active.add(neighbor)
        active_nodes.update(next_active)
        newly_active = next_active
    return len(active_nodes)

def run_case_one():
    print("\n--- Scenario 1 Analysis ---")
    G = nx.Graph()
    G.add_edges_from([
        ('Luma', 'Ghasaq'), ('Luma', 'Zainab'), ('Ghasaq', 'Zahraa'),
        ('Zainab', 'Zahraa'), ('Zahraa', 'Luma'), ('Ghasaq', 'Rawaa')
    ])
    process_results(G)

def run_case_two():
    print("\n--- Scenario 2 Analysis ---")
    G = nx.DiGraph() 
    source = "Public_Figure"
    subs = [f"Sub_{i}" for i in range(1, 20)]
    for s in subs:
        G.add_edge(source, s)
    
    G.add_edge("Sub_1", "Sub_3")
    G.add_edge("Sub_5", "Sub_8")
    G.add_edge("Sub_10", "Sub_12")
    
    process_results(G)

def process_results(G):
    metrics = nx.degree_centrality(G)
    top_node = max(metrics, key=metrics.get)
    avg_reach = sum(simulate_spread(G, [top_node]) for _ in range(5)) / 5
    print(f"Target Node: {top_node}")
    print(f"Spread Impact: {avg_reach}")

if __name__ == "__main__":
    run_case_one()
    run_case_two()
