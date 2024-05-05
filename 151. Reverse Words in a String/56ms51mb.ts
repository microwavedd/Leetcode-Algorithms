function reverseWords(s: string): string {
    return s.replace(/\s+/g,' ').trim().split(' ').reverse().join(' ');
    };