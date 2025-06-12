use std::fmt;
use std::ops::{Index, IndexMut};

/// A word is defined to be a tuple of nonnegative integers, which we call letters.
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct Composition(Vec<usize>);


impl Composition {

    /// Returns the degree of the composition, i.e the sum of its parts.
    pub fn deg(&self) -> usize {
        self.0.iter().sum()
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
    pub fn of_deg(deg: usize, n: usize) -> Vec<Self> {
        let total_num = n.pow(deg as u32);
        let mut words = vec![Composition::from(vec![0; deg]); total_num];

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

impl From<Vec<usize>> for Composition {
    fn from(value: Vec<usize>) -> Self {
        Self(value)
    }
}

impl fmt::Display for Composition {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f,"(")?;
        for (i, v) in self.0.iter().enumerate() {
            write!(f, "{}", v)?;
            if i < self.0.len()-1 {
                write!(f, ", ")?;
            }
        }
        write!(f,")")?;

        Ok(())
    }
}

impl Index<usize> for Composition {
    type Output = usize;

    fn index(&self, index: usize) -> &Self::Output {
        self.get(index).expect("Index not found in word")
    }
}

impl IndexMut<usize> for Composition {
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        self.get_mut(index).expect("Index not found in word")
    }
}

#[macro_export]
macro_rules! comp {
    ( $( $x:expr ),* ) => { Composition::from(vec![$($x,)*]) };
}