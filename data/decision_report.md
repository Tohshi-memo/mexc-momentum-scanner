# Decision Report

- generated_at: 2026-05-07T04:22:40.248561+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3562**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3562, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.54% | **-0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.27% | **+0.27%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.04% | **+0.01%** |
| LIMIT_6PCT | 8/20 | 40.0% | -0.29% | **-0.12%** |
| LIMIT_7PCT | 7/20 | 35.0% | -0.34% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +2.36% | **+1.35%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.71% | **+1.28%** |
| ASK_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.36% | **+0.88%** |
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$105.88** / 初期 $100.00 (+5.88%)
- 確定: 57件 (Win 20 / Loss 21 / Flat 16) / skip 66件
- 成長率目線: 平均log +0.001003 / 幾何平均 +0.100% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $105.88

## 4. Latest Market Context

- 更新: 2026-05-07T04:22:36.441859+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=80919.0
- Funnel: target 769 → liquid 186 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.4 >= 65=1, 4h RSI 76.5 >= 65=1, 4h RSI 82.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +248.10% | $1,554,113.52 |
| B3/USDT:USDT | +106.43% | $8,425,633.76 |
| DOGS/USDT:USDT | +76.09% | $10,441,553.70 |
| PENGUIN/USDT:USDT | +57.63% | $1,252,755.13 |
| FHE/USDT:USDT | +38.86% | $16,350,822.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IO/USDT:USDT | below_1h_threshold | +4.26% | +4.11% |
| FHE/USDT:USDT | below_1h_threshold | +3.96% | +3.81% |
| KSM/USDT:USDT | below_1h_threshold | +3.77% | +3.62% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.06% | +2.91% |
| GALA/USDT:USDT | below_1h_threshold | +2.61% | +2.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
