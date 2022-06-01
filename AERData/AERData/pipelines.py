from .items import Problem, User, Category


class AerdataPipeline(object):

    # Process and manage the item when it was scrapped from the database
    def process_item(self, item, spider):

        # Some if to manage the data according to Object type
        if isinstance(item, Problem):
            try:
                # Insert problems on database or updated if exist
                query = "INSERT INTO problems(id_problem,title,no_repeated_accepteds," \
                        "wrong_answer,accepteds,shipments,time_limit,memory_limit,presentation_error," \
                        "attempts,other,restricted_function,compilation_error,c_shipments,cpp_shipments," \
                        "java_shipments) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" \
                        "ON CONFLICT (id_problem) DO UPDATE SET id_problem = %s,title = %s,no_repeated_accepteds = %s," \
                        "wrong_answer = %s,accepteds = %s,shipments = %s,time_limit = %s,memory_limit = %s," \
                        "presentation_error = %s, attempts = %s,other = %s,restricted_function = %s,compilation_error = %s," \
                        "c_shipments = %s,cpp_shipments = %s, java_shipments = %s"
                # values for query
                values = (
                    item["number"], item["title"], item["no_repeated_accepteds"], item["wrong_answer"],
                    item["accepteds"], item["shipments"], item["time_limit"], item["memory_limit"],
                    item["presentation_error"], item["attempts"], item["other"], item["restricted_function"],
                    item["compilation_error"], item["c_shipments"], item["cpp_shipments"], item["java_shipments"],
                    item["number"], item["title"], item["no_repeated_accepteds"], item["wrong_answer"],
                    item["accepteds"], item["shipments"], item["time_limit"], item["memory_limit"],
                    item["presentation_error"], item["attempts"], item["other"], item["restricted_function"],
                    item["compilation_error"], item["c_shipments"], item["cpp_shipments"], item["java_shipments"])

                # execute and commit
                spider.cur.execute(query, values)
                spider.connection.commit()

                # Relation between problems and categories
                if item["category"] != None:
                    query = "INSERT INTO problems_categories(problems_id, categories_id) VALUES (%s,%s)" \
                            "ON CONFLICT (problems_id,categories_id) DO UPDATE SET problems_id = %s, categories_id = %s"

                    values = (item["number"], item["category"], item["number"], item["category"])

                    # execute and commit
                    spider.cur.execute(query, values)
                    spider.connection.commit()

                return f"{item} Inserted"
            except Exception as e:
                print("Fallo insertando Problemas")
                print(e)
        # Some if to manage the data according to Object type
        elif isinstance(item, User):
            try:
                # Insert problems on database or updated if exist
                query = "INSERT INTO users(id_user,nick,name,country,institution,logo_src,shipments,total_accepteds,intents,accepteds) " \
                        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" \
                        "ON CONFLICT (id_user) DO UPDATE SET id_user = %s, nick = %s,name = %s,country = %s," \
                        "institution = %s,logo_src = %s,shipments = %s,total_accepteds = %s,intents = %s," \
                        "accepteds = %s"
                # values for query
                values = (
                    item['id_user'], item["nick"], item["name"], item["country"], item["institution"],
                    item["image_urls"], item["shipments"], item["total_accepteds"], item['intents'],
                    item['accepteds'], item['id_user'],
                    item["nick"], item["name"], item["country"], item["institution"],
                    item["image_urls"], item["shipments"], item["total_accepteds"], item['intents'],
                    item['accepteds']
                )

                # execute and commit
                spider.cur.execute(query, values)

                contador = 0
                for problema, valor in item['array_problems_accepted'].items():
                    query = "INSERT INTO users_problems_attempted(resolved,id_problem,id_user) " \
                            "VALUES (%s,%s,%s) " \
                            "ON CONFLICT (id_user, id_problem) DO UPDATE SET resolved = %s, id_problem = %s, id_user = %s"

                    splited_valor = valor.split(" ")

                    id_problem_splited = splited_valor[0]

                    values = (
                        True, id_problem_splited, item['id_user'], True, id_problem_splited, item['id_user']
                    )

                    contador += 1

                    spider.cur.execute(query, values)

                for problema, valor in item['array_problems_attempted'].items():
                    query = "INSERT INTO users_problems_attempted(resolved,id_problem,id_user) " \
                            "VALUES (%s,%s,%s) " \
                            "ON CONFLICT (id_user, id_problem) DO UPDATE SET resolved = %s, id_problem = %s, id_user = %s"

                    splited_valor = valor.split(" ")

                    id_problem_splited = splited_valor[0]

                    values = (
                        False, id_problem_splited, item['id_user'], False, id_problem_splited, item['id_user']
                    )

                    contador += 1

                    spider.cur.execute(query, values)

                spider.connection.commit()
                return f"{item} Inserted"
            except Exception as e:
                print("Fallo insertando usuarios")
                print(e)
        # Some if to manage the data according to Object type
        elif isinstance(item, Category):
            try:
                print("INSERTANDO CATEGORIA: " + str(item["id"]))
                print(item["name"])
                # Insert problems on database or updated if exist
                query = "INSERT INTO categories(id_category,name,related_category) VALUES (%s,%s,%s)" \
                        "ON CONFLICT (id_category) DO UPDATE SET id_category = %s, name = %s, related_category = %s"

                # Values for query
                values = (
                    item['id'], item['name'], item['related_category'],
                    item['id'], item['name'], item['related_category'])

                spider.cur.execute(query, values)
                spider.connection.commit()
                return f"{item} Inserted"
            except Exception as e:
                print("Fallo insertando categorias")
                print(e)
        else:
            return f" ------ {item} FAILED -----"
