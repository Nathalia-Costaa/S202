from neo4j import GraphDatabase, basic_auth
class Neo4jGameDatabase:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))

    def close(self):
        self._driver.close()

    def create_player(self, player_id, name):
        with self._driver.session() as session:
            session.write_transaction(self._create_player, player_id, name)

    def _create_player(self, tx, player_id, name):
        tx.run("CREATE (p:Player {id: $player_id, name: $name})", player_id=player_id, name=name)

    def update_player(self, player_id, new_name):
        with self._driver.session() as session:
            session.write_transaction(self._update_player, player_id, new_name)

    def _update_player(self, tx, player_id, new_name):
        tx.run("MATCH (p:Player {id: $player_id}) SET p.name = $new_name", player_id=player_id, new_name=new_name)

    def delete_player(self, player_id):
        with self._driver.session() as session:
            session.write_transaction(self._delete_player, player_id)

    def _delete_player(self, tx, player_id):
        tx.run("MATCH (p:Player {id: $player_id}) DETACH DELETE p", player_id=player_id)

    def create_match(self, match_id, result, player_ids):
        with self._driver.session() as session:
            session.write_transaction(self._create_match, match_id, result, player_ids)

    def _create_match(self, tx, match_id, result, player_ids):
        tx.run("CREATE (m:Match {id: $match_id, result: $result})", match_id=match_id, result=result)
        for player_id in player_ids:
            tx.run("MATCH (m:Match {id: $match_id}), (p:Player {id: $player_id}) "
                   "CREATE (m)-[:PARTICIPATED_BY]->(p)", match_id=match_id, player_id=player_id)

    def get_players(self):
        with self._driver.session() as session:
            return session.read_transaction(self._get_players)

    def _get_players(self, tx):
        result = tx.run("MATCH (p:Player) RETURN p.id AS id, p.name AS name")
        return [{"id": record["id"], "name": record["name"]} for record in result]

    def get_match(self, match_id):
        with self._driver.session() as session:
            return session.read_transaction(self._get_match, match_id)

    def _get_match(self, tx, match_id):
        result = tx.run("MATCH (m:Match {id: $match_id})-[:PARTICIPATED_BY]->(p:Player) "
                        "RETURN m.id AS id, m.result AS result, COLLECT(p.name) AS players", match_id=match_id)
        record = result.single()
        return {
            "id": record["id"],
            "result": record["result"],
            "players": record["players"]
        }

    def get_player_history(self, player_id):
        with self._driver.session() as session:
            return session.read_transaction(self._get_player_history, player_id)

    def _get_player_history(self, tx, player_id):
        result = tx.run("MATCH (p:Player {id: $player_id})<-[r:PARTICIPATED_BY]-(m:Match) "
                        "RETURN m.id AS id, m.result AS result", player_id=player_id)
        return [{"id": record["id"], "result": record["result"]} for record in result]