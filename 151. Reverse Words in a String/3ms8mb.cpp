class Solution {
public:
    void reverseStr(string &s, int i, int j){
        while(i<=j){
            swap(s[i],s[j]);
            i++;
            j--;
        }
    }
    string reverseWords(string s) {
        int n = s.size();

        reverseStr(s,0,n-1);

        int i=0;
        for(int j=0;j<n;j++){
            if(s[j]==' '){
                reverseStr(s,i,j-1);
                i=j+1;
            }
            if(j==n-1){
                reverseStr(s,i,j); 
            }
        }

        int p =0,flag=0;
        i=n-1;
        //removing last spaces
        while(i>=0 && s[i]==' '){
            i--;
        }
        int last = i;

        i=0;
        while(i<n && s[i]==' '){
            i++;
        }

        while(i<=last){
            if(s[i]!=' '){
                s[p++] = s[i];
                flag=true;
            }
            if(s[i]==' ' && flag){
                s[p++] = ' ';
                flag=false;
            }
            i++;
        }
        s.resize(p);
        return s;
    }
};