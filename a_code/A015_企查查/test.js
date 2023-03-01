// var i = n(849356)
//   , o = n(641605)
//   , a = n(983026)
  var c = Object.prototype.hasOwnProperty
  , s = {
    brackets: function(t) {
        return t + "[]"
    },
    comma: "comma",
    indices: function(t, e) {
        return t + "[" + e + "]"
    },
    repeat: function(t) {
        return t
    }
}
  , u = Array.isArray
  , l = String.prototype.split
  , f = Array.prototype.push
  , h = function(t, e) {
    f.apply(t, u(e) ? e : [e])
}
  , p = Date.prototype.toISOString
  // , d = a.default
  , v = {
    addQueryPrefix: !1,
    allowDots: !1,
    charset: "utf-8",
    charsetSentinel: !1,
    delimiter: "&",
    encode: !0,
    // encoder: o.encode,
    encodeValuesOnly: !1,
    // format: d,
    formatter: a.formatters[d],
    indices: !1,
    serializeDate: function(t) {
        return p.call(t)
    },
    skipNulls: !1,
    strictNullHandling: !1
}
  , y = function(t) {
    return "string" == typeof t || "number" == typeof t || "boolean" == typeof t || "symbol" === (0,
    e.default)(t) || "bigint" == typeof t
}
  , g = {}
  , m = function t(n, r, a, c, s, f, p, d, m, b, _, w, x, z, T, M) {
    for (var S = n, C = M, O = 0, H = !1; void 0 !== (C = C.get(g)) && !H; ) {
        var A = C.get(n);
        if (O += 1,
        void 0 !== A) {
            if (A === O)
                throw new RangeError("Cyclic object value");
            H = !0
        }
        void 0 === C.get(g) && (O = 0)
    }
    if ("function" == typeof d ? S = d(r, S) : S instanceof Date ? S = _(S) : "comma" === a && u(S) && (S = o.maybeMap(S, (function(t) {
        return t instanceof Date ? _(t) : t
    }
    ))),
    null === S) {
        if (s)
            return p && !z ? p(r, v.encoder, T, "key", w) : r;
        S = ""
    }
    if (y(S) || o.isBuffer(S)) {
        if (p) {
            var E = z ? r : p(r, v.encoder, T, "key", w);
            if ("comma" === a && z) {
                for (var k = l.call(String(S), ","), L = "", V = 0; V < k.length; ++V)
                    L += (0 === V ? "" : ",") + x(p(k[V], v.encoder, T, "value", w));
                return [x(E) + (c && u(S) && 1 === k.length ? "[]" : "") + "=" + L]
            }
            return [x(E) + "=" + x(p(S, v.encoder, T, "value", w))]
        }
        return [x(r) + "=" + x(String(S))]
    }
    var j, P = [];
    if (void 0 === S)
        return P;
    if ("comma" === a && u(S))
        j = [{
            value: S.length > 0 ? S.join(",") || null : void 0
        }];
    else if (u(d))
        j = d;
    else {
        var R = Object.keys(S);
        j = m ? R.sort(m) : R
    }
    for (var F = c && u(S) && 1 === S.length ? r + "[]" : r, D = 0; D < j.length; ++D) {
        var N = j[D]
          , I = "object" === (0,
        e.default)(N) && void 0 !== N.value ? N.value : S[N];
        if (!f || null !== I) {
            var B = u(S) ? "function" == typeof a ? a(F, N) : F : F + (b ? "." + N : "[" + N + "]");
            M.set(n, O);
            var $ = i();
            $.set(g, M),
            h(P, t(I, B, a, c, s, f, p, d, m, b, _, w, x, z, T, $))
        }
    }
    return P
}
  , b = function(t) {
    if (!t)
        return v;
    if (null !== t.encoder && void 0 !== t.encoder && "function" != typeof t.encoder)
        throw new TypeError("Encoder has to be a function.");
    var e = t.charset || v.charset;
    if (void 0 !== t.charset && "utf-8" !== t.charset && "iso-8859-1" !== t.charset)
        throw new TypeError("The charset option must be either utf-8, iso-8859-1, or undefined");
    var n = a.default;
    if (void 0 !== t.format) {
        if (!c.call(a.formatters, t.format))
            throw new TypeError("Unknown format option provided.");
        n = t.format
    }
    var r = a.formatters[n]
      , i = v.filter;
    return ("function" == typeof t.filter || u(t.filter)) && (i = t.filter),
    {
        addQueryPrefix: "boolean" == typeof t.addQueryPrefix ? t.addQueryPrefix : v.addQueryPrefix,
        allowDots: void 0 === t.allowDots ? v.allowDots : !!t.allowDots,
        charset: e,
        charsetSentinel: "boolean" == typeof t.charsetSentinel ? t.charsetSentinel : v.charsetSentinel,
        delimiter: void 0 === t.delimiter ? v.delimiter : t.delimiter,
        encode: "boolean" == typeof t.encode ? t.encode : v.encode,
        encoder: "function" == typeof t.encoder ? t.encoder : v.encoder,
        encodeValuesOnly: "boolean" == typeof t.encodeValuesOnly ? t.encodeValuesOnly : v.encodeValuesOnly,
        filter: i,
        format: n,
        formatter: r,
        serializeDate: "function" == typeof t.serializeDate ? t.serializeDate : v.serializeDate,
        skipNulls: "boolean" == typeof t.skipNulls ? t.skipNulls : v.skipNulls,
        sort: "function" == typeof t.sort ? t.sort : null,
        strictNullHandling: "boolean" == typeof t.strictNullHandling ? t.strictNullHandling : v.strictNullHandling
    }
};

// function(t, n) {
function stringfiy(t, n) {
    var r, o = t, a = b(n);
    "function" == typeof a.filter ? o = (0,
    a.filter)("", o) : u(a.filter) && (r = a.filter);
    var c, l = [];
    if ("object" !== (0,
    e.default)(o) || null === o)
        return "";
    c = n && n.arrayFormat in s ? n.arrayFormat : n && "indices"in n ? n.indices ? "indices" : "repeat" : "indices";
    var f = s[c];
    if (n && "commaRoundTrip"in n && "boolean" != typeof n.commaRoundTrip)
        throw new TypeError("`commaRoundTrip` must be a boolean, or absent");
    var p = "comma" === f && n && n.commaRoundTrip;
    r || (r = Object.keys(o)),
    a.sort && r.sort(a.sort);
    for (var d = i(), v = 0; v < r.length; ++v) {
        var y = r[v];
        a.skipNulls && null === o[y] || h(l, m(o[y], y, f, p, a.strictNullHandling, a.skipNulls, a.encode ? a.encoder : null, a.filter, a.sort, a.allowDots, a.serializeDate, a.format, a.formatter, a.encodeValuesOnly, a.charset, d))
    }
    var g = l.join(a.delimiter)
      , _ = !0 === a.addQueryPrefix ? "?" : "";
    return a.charsetSentinel && ("iso-8859-1" === a.charset ? _ += "utf8=%26%2310003%3B&" : _ += "utf8=%E2%9C%93&"),
    g.length > 0 ? _ + g : ""
}



// t = '/api/datalist/touzilist';
//
// t = t.toLowerCase();
// var i = a.default(t, e.data),
//     l = r.default(t, e.data, s.default());
// e.headers[i] = l


params = {keyNo: '5dffb644394922f9073544a08f38be9f', pageIndex: 2};
var _o = {
    allowPrototypes: !0,
    encodeValuesOnly: !0,
    sort: function(e, t) {
        return e.localeCompare(t)
    },
    allowDots: !0,
    arrayFormat: "brackets"
};
stringfiy(params, _o);