function rot13(str) {
    // LBH QVQ VG!
    return str.replace(/[A-Z]/g, L =>
        String.fromCharCode((L.charCodeAt(0) + 13) > 90 ? ((L.charCodeAt(0) + 13) % 90 + 64) : (L.charCodeAt(0) + 13))
    );
}

// 通过取余，再加上一个base number 来进行数值范围的映射。