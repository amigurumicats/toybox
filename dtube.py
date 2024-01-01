"""
ドロステチューブソルバーを作りたい

dir := {"up", "down", "left", "right"}
pipe := {"UL", "UR", "DL", "DR", "UD", "LR", "UL+DR", "UR+DL", "UD+LR"}
tile := pipe + {"?", "*"}

board[a][b]
cell = (a, b)

まず最初にピースとして用意されている色付きブロックの繋がり方を全て仮定する
    blueはstartとgoalが決まっているので、2通りになる
全てのピースと、ボードの繋がり方が決まったので、ピースを仮定しながら置いていく

うう〜〜ん、25が解けない
"""
from typing import Dict, List, Optional, Tuple


board_size = (3, 3)

exit_pos = {
    "up": (0, 1),
    "down": (2, 1),
    "left": (1, 0),
    "right": (1, 2),
}

move = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

all_pipe = {
    "UL": [("up", "left")],
    "UR": [("up", "right")],
    "DL": [("down", "left")],
    "DR": [("down", "right")],
    "UD": [("up", "down")],
    "LR": [("left", "right")],
    "UL+DR": [("up", "left"), ("down", "right")],
    "UR+DL": [("up", "right"), ("down", "left")],
    "UD+LR": [("up", "down"), ("left", "right")],
    "*": [],
}

def reverse_dir(dir: str) -> str:
    if dir == "up": return "down"
    if dir == "down": return "up"
    if dir == "left": return "right"
    if dir == "right": return "left"
    raise


def _through(path: Tuple[str, str], into_dir: str) -> Optional[str]:
    if path[0] == into_dir:
        return path[1]
    if path[1] == into_dir:
        return path[0]
    return None


def through_pipe(pipe_name: str, into_dir: str) -> Optional[str]:
    for path in all_pipe.get(pipe_name, []):
        if into_dir in path:
            return _through(path, into_dir)
    return None


def check_pos(pos: Tuple[int, int], board_size: Tuple[int, int]) -> bool:
    return 0 <= pos[0] < board_size[0] and 0 <= pos[1] < board_size[1]


def check_board(board, expected_pipe) -> bool:
    for start, goal in all_pipe[expected_pipe]:
        if not through_board(board, start) == goal:
            return False
    return True


def through_board(board, into_dir) -> Optional[str]:
    a, b = exit_pos[into_dir]
    dir = into_dir
    while True:
        next_dir = through_pipe(board[a][b], dir)
        if not next_dir: return None
        for goal_dir in exit_pos.keys():
            if (a, b) == exit_pos[goal_dir] and next_dir == goal_dir:
                return goal_dir
        da, db = move[next_dir]
        a, b = a+da, b+db
        if not check_pos((a, b), board_size): return None
        dir = reverse_dir(next_dir)


def solve(boards, pieces, tasks, now=None):
    """
    boards: 現在のボードの状況
    pieces: 残りピース
    tasks: 残りタスク
    now: {
        board: str,
        pos: Tuple[int, int],
        dir: str,
    }
    """
    # print("[DEBUG]", boards, pieces, tasks, now)
    ks = list(boards.keys())
    # print("\t".join(k for k in ks))
    # for i in range(3):
    #     print("  ".join(str(boards[k][i]) for k in ks))
    # print("pieces: ", pieces)
    # print("tasks: ", tasks)
    # print("now: ", now)
    # input()

    if not tasks:
        # 解けた
        print("\t".join(k for k in ks))
        for i in range(3):
            print("  ".join(str(boards[k][i]) for k in ks))
        return

    task = tasks[0]
    if not now:
        now = {
            "board": task[0],
            "pos": exit_pos[task[1][0]],
            "dir": task[1][0]
        }

    a, b = now["pos"]
    dir = now["dir"]
    board = boards[now["board"]]
    if board[a][b] == "?":
        # 分岐
        for p in pieces.keys():
            if pieces[p] <= 0: continue
            out_dir = through_pipe(p, dir)
            if not out_dir: continue
            pieces[p] -= 1
            board[a][b] = p

            # print("debug")
            # print("piece: ", p)
            # print("\t".join(k for k in ks))
            # for i in range(3):
            #     print("  ".join(str(boards[k][i]) for k in ks))
            # print()

            # 先頭のタスクを達成できてるかどうか
            goal_dir = task[1][1]
            if (a, b) == exit_pos[goal_dir] and out_dir == goal_dir:
                solve(boards, pieces, tasks[1:])
            else:
                da, db = move[out_dir]
                new_now = {
                    "board": now["board"],
                    "pos": (a+da, b+db),
                    "dir": reverse_dir(out_dir),
                }
                if check_pos(new_now["pos"], board_size):
                    solve(boards, pieces, tasks, new_now)
            # 後処理
            pieces[p] += 1
            board[a][b] = "?"
    elif board[a][b] == "*":
        # 行き止まり
        return
    else:
        # 道なりに進む
        out_dir = through_pipe(board[a][b], dir)
        if not out_dir: return

        goal_dir = task[1][1]
        if (a, b) == exit_pos[goal_dir] and out_dir == goal_dir:
            solve(boards, pieces, tasks[1:])
        else:
            da, db = move[out_dir]
            new_now = {
                "board": now["board"],
                "pos": (a+da, b+db),
                "dir": reverse_dir(out_dir),
            }
            if check_pos(new_now["pos"], board_size):
                solve(boards, pieces, tasks, new_now)


def main():
    pieces = {
        "blue": 5,
        "red": 5,
        "green": 3,
        "UL": 3,
        "UR": 1,
        "UL+DR": 1,
    }
    boards = {
        "blue": [["?", "?", "?"], ["blue", "?", "red"], ["?", "?", "?"]],
        "red": [["?", "?", "?"], ["?", "?", "UL+DR"], ["?", "?", "?"]],
        "green": [["?", "?", "?"], ["UR", "?", "blue"], ["?", "green", "?"]],
    }
    start, goal = "left", "right"  # メインはblue固定

    blue_pipes = [p for p in all_pipe.keys() if through_pipe(p, start) == goal]

    for board_pipe_list in pr([blue_pipes if bp == "blue" else all_pipe.keys() for bp in boards.keys()]):
        # 各色ボードの繋がり方を仮定した

        # "blue" => "UL" みたいなdict
        board_pipe_dict = { board_name: pipe_name for board_name, pipe_name in zip(boards.keys(), board_pipe_list)}

        # ピースをまとめる
        now_pieces = {}
        for k, v in pieces.items():
            if k in board_pipe_dict:
                k = board_pipe_dict[k]
            now_pieces[k] = now_pieces.get(k, 0) + v

        # タスク(実現すべき繋がり方)をまとめる
        tasks = []
        for board_name, pipe_name in board_pipe_dict.items():
            tasks += [(board_name, path) for path in all_pipe[pipe_name]]

        # ボード上の色タイルをパイプにする
        # まずディープコピーしてから書き換える
        now_boards = {k: [col[:] for col in v] for k, v in boards.items()}
        for board in now_boards.values():
            for a, b in pr([range(board_size[0]), range(board_size[1])]):
                board[a][b] = board_pipe_dict.get(board[a][b], board[a][b])

        # print(board_pipe_dict, tasks, now_pieces)
        solve(now_boards, now_pieces, tasks)


def pr(ll):
    """
    リストのリストを渡すと、直積(?)をとる
    [[1,2], [3,4]] => [[1,3], [1,4], [2,3], [2,4]]
    """
    if len(ll) == 0: return
    if len(ll) == 1:
        for i in ll[0]:
            yield (i,)
    else:
        for i in ll[0]:
            for j in pr(ll[1:]):
                yield (i, *j)



if __name__ == "__main__":
    main()
