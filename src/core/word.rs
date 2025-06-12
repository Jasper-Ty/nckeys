use std::{fmt, ops::{Index, IndexMut}};

/// A word is defined to be a tuple of nonnegative integers, which we call letters.
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct Word(Vec<usize>);

impl Word {

    /// Returns the length of the word, i.e its number of entries.
    pub fn deg(&self) -> usize {
        self.0.len()
    }

    /// Returns a reference to the letter at `idx`
    pub fn get(&self, idx: usize) -> Option<&usize> {
        self.0.get(idx)
    }

    /// Returns a mutable reference to the letter at `idx`
    pub fn get_mut(&mut self, idx: usize) -> Option<&mut usize> {
        self.0.get_mut(idx)
    }

    /// Returns all words of length `l` in the letters 0, ..., n
    pub fn words_of_deg(deg: usize, n: usize) -> Vec<Self> {
        let total_num = n.pow(deg as u32);
        let mut words = vec![Word::from(vec![0; deg]); total_num];

        let mut p = total_num;
        let mut q = 1;
        for j in 0..deg {
            p /= n;
            q *= n;
            for k in 0..q {
                for t in 0..p {
                    words[k * p + t][j] = k % n;
                }
            }
        }
        words
    }
}

impl From<Vec<usize>> for Word {
    fn from(value: Vec<usize>) -> Self {
        Self(value)
    }
}

impl fmt::Display for Word {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f,"[")?;
        for (i, v) in self.0.iter().enumerate() {
            write!(f, "{}", v)?;
            if i < self.0.len()-1 {
                write!(f, ", ")?;
            }
        }
        write!(f,"]")?;

        Ok(())
    }
}

impl Index<usize> for Word {
    type Output = usize;

    fn index(&self, index: usize) -> &Self::Output {
        self.get(index).expect("Index not found in word")
    }
}

impl IndexMut<usize> for Word {
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        self.get_mut(index).expect("Index not found in word")
    }
}

#[macro_export]
macro_rules! word {
    ( $( $x:expr ),* ) => { Word::from(vec![$($x,)*]) };
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn lex_order() {
        for i in 0..10 {
            for j in i..10{
                assert!(word![i] <= word![j])
            }
        }
        assert!(word![0,0,1] <= word![1,0,0]);
        assert!(word![0,0,1] <= word![0,1,0]);
        assert!(word![0,0,1] <= word![0,0,1]);
    }
}