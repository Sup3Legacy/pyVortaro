from neo4j import GraphDatabase

url = "neo4j+ssc://cgiga.Fr:7687"
username = "neo4j"


class Interface:
    def __init__(self, mdp):
        self.driver = GraphDatabase.driver(url, auth=(username, mdp))

    def checkNode(self, string):
        """returns whether exits a node where 'str' field contaisn string"""
        with self.driver.session() as session:
            query = ("MATCH (n) "
                "WHERE n.str = $str "
                "RETURN n AS n" )
            result = session.run(query, str=string)
            return not(self.nullResult(result))

    def nullResult(self, result):
        return (result.peek() is None)

    def addNode(self, type, value, trad):
        with self.driver.session() as session:
            query = ("Create (n : {type} {{str : $value, trad : $trad}})".format(type=type))
            session.run(query, value=value, trad=trad)

    def addRelation(self, node1, node2, name, value):
        with self.driver.session() as session:
            query = ("Match (n), (m) "
                     "Where n.str = $value1 AND m.str = $value2 "
                     "Create (n)-[r : {champ} {{str : $value}}]->(m)".format(champ=name))
            session.run(query, value1=node1, value2=node2, value = value)

    def deleteNode(self, value):
        with self.driver.session() as session:
            query = ("Match (n)-[r]-> (m) "
                     "WHERE n.str = $str OR m.str = $str "
                     "Delete r")
            session.run(query, str=value)
            query = ("Match (n) "
                     "Where n.str = $str "
                     "Delete n")
            session.run(query, str=value)
