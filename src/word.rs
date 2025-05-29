use crate::Degree;

#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct Word(pub Vec<usize>);

impl Degree for Word {
    fn degree(&self) -> usize {
        self.0.len()
    }
}

#[macro_export]
macro_rules! word {
    ( $( $x:expr ),* ) => { Word(vec![$($x,)*]) };
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