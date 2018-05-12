"""
Created on Apr 11, 2016
Last updated on Apr 30, 2018
Copyright (c) 2017-2018 Teodoro Montanaro, Luigi De Russis, Alberto Monge Roffarello

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
@author: Teodoro Montanaro, Luigi De Russis, Alberto Monge Roffarello
"""

import pymysql



def insert_task(text, urgent):
    """
    :param text: text that we want to insert as task in the db
    :param urgent: 0 if the task is not urgent, 1 otherwise

    Insert a task in the database
    """

    # prepare the query
    sql = """INSERT INTO tasks(text, urgent) VALUES (%s, %s)"""

    # connect to the db
    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='tasks', host='localhost')
    cursor = conn.cursor()

    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (text, urgent))
        # commit all pending queries
        conn.commit()
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()


def get_tasks():
    """
    Get existing tasks from the database
    """

    tasks = []
    sql = "SELECT id_task, text, urgent  FROM tasks"
    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='tasks', host='localhost')

    #

    cursor = conn.cursor()
    cursor.execute(sql)

    results = cursor.fetchall()

    for task in results:
        tasks.append(task)

    conn.close()

    return tasks


def get_task(id_task):
    """
    :param id_task: unique identifier for the task we want to retrieve

    Get a specified task from the database
    """

    # prepare the query
    sql = "SELECT id_task, text, urgent FROM tasks WHERE id_task = %s"

    # connect to the db
    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='tasks', host='localhost')

    # to remove u from sqlite3 cursor.fetchall() results


    cursor = conn.cursor()
    cursor.execute(sql, (id_task, ))

    task = cursor.fetchone()

    # close the connection
    conn.close()

    return task


def remove_task_by_id(id_task):
    """
    :param id_task: unique identifier for the task we want to remove

    Remove a specific task from the db
    """

    # prepare the query
    sql = "DELETE FROM tasks WHERE id_task = %s"

    # connect to the db
    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='tasks', host='localhost')
    cursor = conn.cursor()

    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (id_task, ))
        # commit all pending executed queries in the connection
        conn.commit()
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()


def update_task(id_task, text, urgent):
    """
    :param id_task: it represents the task id of the element we want to update
    :param text: text that we want to insert as task in the db
    :param urgent: 0 if the task is not urgent, 1 otherwise

    Update a task in the database
    """

    # prepare the query
    sql = """UPDATE tasks SET text=%s, urgent=%s WHERE id_task = %s"""

    # connect to the db
    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='tasks', host='localhost')
    cursor = conn.cursor()

    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (text, urgent,id_task) )
        # commit all pending queries
        conn.commit()
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()



