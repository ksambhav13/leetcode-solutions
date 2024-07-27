import requests
import json

# LeetCode GraphQL API endpoint
API_URL = "https://leetcode.com/graphql"

# GraphQL query to fetch question details
QUERY = """
query questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    titleSlug
    title
    topicTags {
        name
    }
    codeSnippets {
        langSlug
        code
    }
    difficulty
    content
    exampleTestcaseList
    metaData
  }
}
"""


# Function to fetch question details
def fetch_question_details(titleSlug):
    variables = {"titleSlug": titleSlug}
    response = requests.post(API_URL, json={"query": QUERY, "variables": variables})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f"Query failed with status code {response.status_code} and message: {response.text}"
        )


def generate_python_code(question):
    codeSnippets = question["codeSnippets"]
    for code_def in codeSnippets:
        if code_def["langSlug"] == "python3":
            python_code = code_def["code"]
            break

    if not python_code:
        raise Exception("Python code template not found for this question")

    # generate code for testcases
    example_test_cases = question["exampleTestcaseList"]
    testcases_str = ""
    for test_case in example_test_cases:
        test_case = test_case.replace("null", "None")
        test_case = ",\n    ".join(test_case.split("\n"))
        testcases_str += f"    {test_case},\n"
    testcases_code = f"testcases = [\n{testcases_str}]"

    # initialize imports list
    util_import = set()
    typing_import = set()

    # generate code for parameters
    metadata = question["metaData"]
    # print(f"{metadata=}")
    param_count = len(metadata["params"])

    def create_param_str(param, i):
        param_str = "testcase"
        if param_count > 1:
            param_str = f"testcases[i + {i}]" if i > 0 else "testcases[i]"
        if param["type"] == "integer[]":
            typing_import.add("List")
        elif param["type"] == "integer[][]":
            typing_import.add("List")
        elif param["type"] == "ListNode":
            util_import.add("ListNode")
            util_import.add("build_linked_list")
            typing_import.add("Optional")
            param_str = f"build_linked_list({param_str})"
        elif param["type"] == "TreeNode":
            util_import.add("TreeNode")
            util_import.add("build_tree")
            typing_import.add("Optional")
            param_str = f"build_tree({param_str})"
        return param_str

    params_list = []
    for i, param in enumerate(metadata["params"]):
        param_str = create_param_str(param, i)
        params_list.append(param_str)
    parameters = ", ".join(params_list)

    # generate code for display result function
    display_result_func = "print"
    if metadata["return"]["type"] == "list<integer>":
        typing_import.add("List")
    elif metadata["return"]["type"] == "ListNode":
        display_result_func = "display_linked_list"
        util_import.add("ListNode")
        util_import.add("display_linked_list")
        typing_import.add("Optional")
    elif metadata["return"]["type"] == "TreeNode":
        display_result_func = "display_tree"
        util_import.add("TreeNode")
        util_import.add("display_tree")
        typing_import.add("Optional")

    header_comment = f"# [{question["questionId"]}. {question["title"]}](https://leetcode.com/problems/{question["titleSlug"]}/)"
    util_import_code = (
        f"from util import {", ".join(sorted(util_import))}" if util_import else ""
    )
    typing_import_code = (
        f"from typing import {", ".join(sorted(typing_import))}"
        if typing_import
        else ""
    )

    # generate run command
    for_statement = (
        f"for i in range(0, len(testcases), {param_count}):"
        if param_count > 1
        else "for testcase in testcases:"
    )

    run_command = f"""
{for_statement}
    {display_result_func}(Solution().{metadata["name"]}({parameters}))
"""

    file_content = f"""{header_comment}

{util_import_code}
{typing_import_code}

{python_code}
        pass
        
{testcases_code}

{run_command}
"""
    return file_content


def generate_question_file(question_details):
    question = question_details["data"]["question"]

    filename = (
        f"{question['questionId']}_{question['title'].replace(' ', '_').lower()}.html"
    )
    topics = "".join(
        [f"<div class='pill'>{topic["name"]}</div>" for topic in question["topicTags"]]
    )
    file_content = f"""
    <html>
        <head>
            <title>{question["title"]}</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <div class = "container">
                <div class="title">
                    <a href="https://leetcode.com/problems/{question['titleSlug']}/">{question["questionId"]}. {question["title"]}
                    </a>
                </div>
                <div>
                    <div class="pill">{question["difficulty"]}</div>
                </div>
                <div class="description">{question["content"]}</div>
                <div class="topics">{topics}</div>
            </div>
            <div>
                
            <div>
        <body>
    </html>
    """

    with open(filename, "w") as file:
        file.write(file_content)

    print(f"Question file generated: {filename}")


# Function to generate Python file
def generate_python_file(question_details):
    question = question_details["data"]["question"]

    file_content = generate_python_code(question)

    filename = (
        f"{question['questionId']}_{question['title'].replace(' ', '_').lower()}.py"
    )
    with open(filename, "w") as file:
        file.write(file_content)

    print(f"Python file generated: {filename}")


def generate_reponse_file(question_slug, question_details):
    filename = f"{question_slug}.json"
    with open(filename, "w") as f:
        json.dump(question_details, f)


if __name__ == "__main__":
    question_slug = input("Enter LeetCode question slug: ")
    question_slug = question_slug.strip().lower()
    mock = False
    try:
        if mock:
            with open(f"{question_slug}.json", "r") as f:
                question_details = json.load(f)
        else:
            question_details = fetch_question_details(question_slug)
            question_details["data"]["question"]["metaData"] = json.loads(
                question_details["data"]["question"]["metaData"]
            )
            generate_reponse_file(question_slug, question_details)

        generate_question_file(question_details)
        generate_python_file(question_details)
    except Exception as e:
        raise e
