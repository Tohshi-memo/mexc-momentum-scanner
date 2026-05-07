# Decision Report

- generated_at: 2026-05-07T04:52:47.890654+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3568**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3568, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.30% | **+0.28%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.34% | **+0.24%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.10% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.54% | **+1.31%** |
| ASK_LONG | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.86% | **+0.47%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.71% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.16** / 初期 $100.00 (+6.16%)
- 確定: 62件 (Win 22 / Loss 23 / Flat 17) / skip 67件
- 成長率目線: 平均log +0.000963 / 幾何平均 +0.096% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.16

## 4. Latest Market Context

- 更新: 2026-05-07T04:52:38.401114+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=80933.0
- Funnel: target 769 → liquid 187 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1, 4h RSI 83.6 >= 65=1, 4h RSI 82.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +220.48% | $1,635,690.18 |
| B3/USDT:USDT | +118.82% | $8,667,548.86 |
| DOGS/USDT:USDT | +75.28% | $11,078,074.39 |
| PENGUIN/USDT:USDT | +45.77% | $1,305,111.10 |
| FHE/USDT:USDT | +35.10% | $16,664,440.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FARTCOIN/USDT:USDT | below_1h_threshold | +4.46% | +4.29% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.90% | +3.74% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +3.89% | +3.73% |
| STX/USDT:USDT | below_1h_threshold | +3.71% | +3.54% |
| GALA/USDT:USDT | below_1h_threshold | +3.67% | +3.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
