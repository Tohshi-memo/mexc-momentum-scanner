# Decision Report

- generated_at: 2026-10-01T11:21:22.668243+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15899**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15899, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.03% | **-2.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.59% | **+0.09%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.05% | **+0.04%** |
| LIMIT_3PCT | 18/20 | 90.0% | -0.46% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/11 | 72.7% | +3.31% | **+2.41%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.51% | **+2.26%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.75% | **+1.65%** |
| MARKET_LONG | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.33% | **+1.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,296.94** / 初期 $100.00 (+1196.94%)
- 確定: 6017件 (Win 1782 / Loss 1935 / Flat 2300) / skip 6443件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACNSTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,296.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$271.66** / 初期 $100.00 (+171.66%)
- 確定: 3552件 (Win 984 / Loss 816 / Flat 1752) / skip 5758件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1293 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACNSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.46% 残高後 $271.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4059件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T11:21:11.515046+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=83789.9
- Funnel: target 1097 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +70.25% | $17,344,882.63 |
| LONGXIA/USDT:USDT | +44.85% | $3,562,560.36 |
| NOM/USDT:USDT | +25.20% | $2,603,203.32 |
| CT/USDT:USDT | +23.39% | $6,498,090.14 |
| NIGHT/USDT:USDT | +19.86% | $8,603,621.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +1.47% | +1.63% |
| MOVR/USDT:USDT | below_1h_threshold | +1.39% | +1.56% |
| SNXX/USDT:USDT | below_1h_threshold | +1.34% | +1.51% |
| TRB/USDT:USDT | below_1h_threshold | +0.87% | +1.04% |
| PHA/USDT:USDT | below_1h_threshold | +0.83% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
