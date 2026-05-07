# Decision Report

- generated_at: 2026-05-07T01:27:36.846881+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3521**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3521, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -1.76% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.51% | **+2.38%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.73% | **+1.82%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.27% | **+1.70%** |
| ASK_LONG | 20/20 | 100.0% | +1.63% | **+1.63%** |
| MARKET_LONG | 20/20 | 100.0% | +1.61% | **+1.61%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$100.24** / 初期 $100.00 (+0.24%)
- 確定: 16件 (Win 4 / Loss 6 / Flat 6) / skip 66件
- 成長率目線: 平均log +0.000151 / 幾何平均 +0.015% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $100.24

## 4. Latest Market Context

- 更新: 2026-05-07T01:27:33.171975+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=81099.4
- Funnel: target 766 → liquid 189 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.9 >= 65=1, 4h RSI 75.3 >= 65=1, 4h RSI 75.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +130.26% | $1,011,201.63 |
| DOGS/USDT:USDT | +49.55% | $6,076,817.53 |
| PENGUIN/USDT:USDT | +22.43% | $1,031,889.38 |
| FHE/USDT:USDT | +21.73% | $15,715,663.27 |
| LAB/USDT:USDT | +12.08% | $255,432,364.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +2.95% | +2.79% |
| NOT/USDT:USDT | below_1h_threshold | +2.79% | +2.63% |
| UB/USDT:USDT | below_1h_threshold | +1.46% | +1.30% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.41% | +1.25% |
| VVV/USDT:USDT | below_1h_threshold | +1.34% | +1.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
