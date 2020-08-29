# -*- encoding: utf-8 -*-
import logging
import jieba
from conf import substitution_words, DEBUG

# global set
jieba.setLogLevel(log_level=logging.INFO)
for word, _ in substitution_words.items():
    jieba.add_word(word, freq=10000)


def substitute_statement(statement, substitution_dict):
    """
    replace word in input statement
    :param str statement: input statement
    :param dict[str, str] substitution_dict: replace key with value
    :return: replaced statement
    """
    statement_words = jieba.lcut(statement)
    if DEBUG:
        print(list(statement_words))
    substituted_words = [substitution_dict.get(word, word) for word in statement_words]
    return ''.join(substituted_words)


def main():
    statement = input("\033[34m>>> \033[0m")
    statement = substitute_statement(statement, substitution_words)
    print(statement)


if __name__ == "__main__":
    print("\033[31m===== anti-gangjing =====\n一个可以把反进化论杠精怼死的 Python 脚本")
    while True:
        main()
