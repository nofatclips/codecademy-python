My recurrent solution. I haven't used recursion explicitly,
because this allowed me to remove some duplicates.

The algorithm is initialized by putting the whole string in
the queue of strings to split and the list of substrings.
For each string in the queue, be `l` its length, I generate
the two substrings of length `l-1`, called `lWord` (all
letters except the last) and `rWord` (all letters except
the first) and if they're not the empty string, they're
added to the queue of strings to split as well as to the
list of substrings. Then another string is extracted from
the queue and the loop restarts.

The optimization is the `l!=previousL` part. The `lWord`
for a particular substring is the same as the `rWord` for
the adjacent substring, so I skip the latter.