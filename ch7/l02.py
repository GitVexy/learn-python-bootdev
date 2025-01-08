def compare_heights(e_height, a_height, w_height, m_height):
    return (
        m_height == e_height,
        a_height == e_height,
        w_height == a_height
    )