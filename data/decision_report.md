# Decision Report

- generated_at: 2026-09-19T21:46:35.091052+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15099**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15099, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/17 | 41.2% | +3.58% | **+1.47%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.53% | **+0.50%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.69% | **+0.52%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.86% | **+0.52%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.75% | **+0.41%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | -0.54% | **-0.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6020件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$242.40** / 初期 $100.00 (+142.40%)
- 確定: 3212件 (Win 889 / Loss 762 / Flat 1561) / skip 5298件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0065 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $242.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定: 2975件 (Win 880 / Loss 1176 / Flat 919) / pending 3件 / skip 3596件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000454 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.01

## 6. Latest Market Context

- 更新: 2026-09-19T21:46:19.898141+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=81025.4
- Funnel: target 1050 → liquid 140 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.9 >= 65=1, 4h RSI 89.4 >= 65=1, 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +55.03% | $37,750,832.09 |
| OFC/USDT:USDT | +45.19% | $1,667,639.79 |
| BANK/USDT:USDT | +16.81% | $2,285,292.20 |
| CATE/USDT:USDT | +12.87% | $1,601,234.81 |
| CNPY/USDT:USDT | +6.39% | $1,571,604.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +2.83% | +2.96% |
| SYN/USDT:USDT | below_1h_threshold | +2.35% | +2.48% |
| AKE/USDT:USDT | below_1h_threshold | +1.41% | +1.54% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.53% | +0.66% |
| CATE/USDT:USDT | below_1h_threshold | +0.48% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
