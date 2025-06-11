use std::fmt;

use crate::Degree;

#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct Word(Vec<usize>);
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

impl Degree for Word {
    fn degree(&self) -> usize {
        self.0.len()
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