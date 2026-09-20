# Decision Report

- generated_at: 2026-09-20T20:56:28.003528+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15213**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15213, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.84% | **-0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.07%** |
| LIMIT_1PCT | 20/20 | 100.0% | -0.27% | **-0.27%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.05% | **-0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.51% | **+1.13%** |
| MARKET_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.80% | **+0.81%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,173.63** / 初期 $100.00 (+1073.63%)
- 確定: 5717件 (Win 1705 / Loss 1845 / Flat 2167) / skip 6057件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OFC/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,173.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.68** / 初期 $100.00 (+147.68%)
- 確定: 3295件 (Win 911 / Loss 764 / Flat 1620) / skip 5329件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0131 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $247.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定: 2996件 (Win 885 / Loss 1184 / Flat 927) / pending 6件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000169 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $121.61

## 6. Latest Market Context

- 更新: 2026-09-20T20:56:16.684795+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=81043.7
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +25.22% | $3,219,211.95 |
| S/USDT:USDT | +16.06% | $3,102,884.80 |
| LUNANEW/USDT:USDT | +14.10% | $2,075,576.56 |
| SAGA/USDT:USDT | +12.11% | $6,680,321.61 |
| SEI/USDT:USDT | +10.53% | $14,836,564.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SEI/USDT:USDT | below_1h_threshold | +4.04% | +4.16% |
| STX/USDT:USDT | below_1h_threshold | +3.18% | +3.30% |
| ALLO/USDT:USDT | below_1h_threshold | +2.91% | +3.03% |
| CAKE/USDT:USDT | below_1h_threshold | +2.33% | +2.46% |
| SUI/USDT:USDT | below_1h_threshold | +1.43% | +1.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
