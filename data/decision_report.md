# Decision Report

- generated_at: 2026-09-25T12:51:21.950017+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15528**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15528, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +1.82% | **+1.46%** |
| LIMIT_4PCT | 14/20 | 70.0% | +1.71% | **+1.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +3.30% | **+0.99%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.66% | **+0.56%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.24% | **+0.87%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.64% | **+0.82%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.98% | **+0.74%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.50% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 220件 (TP 80 / SL 135 / EXP 5)
- 最新: MYX/USDT:USDT TP_HIT PnL +7.62% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,200.90** / 初期 $100.00 (+1100.90%)
- 確定: 5902件 (Win 1740 / Loss 1891 / Flat 2271) / skip 6187件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,200.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.32** / 初期 $100.00 (+156.32%)
- 確定: 3461件 (Win 952 / Loss 793 / Flat 1716) / skip 5478件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0590 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $256.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 0件 / skip 3831件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000246 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T12:51:12.180130+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=84392.5
- Funnel: target 1069 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +43.33% | $4,034,952.81 |
| ARK/USDT:USDT | +33.01% | $2,119,757.72 |
| BP/USDT:USDT | +32.66% | $1,042,069.02 |
| B3/USDT:USDT | +20.75% | $1,040,352.15 |
| QNT/USDT:USDT | +15.47% | $16,444,926.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CFX/USDT:USDT | below_1h_threshold | +2.68% | +2.84% |
| XAI/USDT:USDT | below_1h_threshold | +1.84% | +2.01% |
| POL/USDT:USDT | below_1h_threshold | +1.78% | +1.95% |
| ONDO/USDT:USDT | below_1h_threshold | +1.71% | +1.87% |
| SEI/USDT:USDT | below_1h_threshold | +1.55% | +1.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
