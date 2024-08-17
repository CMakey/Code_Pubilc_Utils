def sort_corners(corners, cols, rows):
    corners = corners.reshape(-1, 2)

    # 首先，按 y 对所有角点进行排序以保持行完整性
    sorted_by_y = corners[np.argsort(corners[:, 1])]

    # 然后按 x 对每行进行排序
    sorted_by_y_x = sorted_by_y.reshape(rows, cols, 2)
    for i in range(rows):
        sorted_by_y_x[i] = sorted_by_y_x[i][np.argsort(sorted_by_y_x[i][:, 0])]

    return sorted_by_y_x.reshape(-1, 1, 2).astype(np.float32)  # 使用(-1, 1, 2)以保持数组列表格式
