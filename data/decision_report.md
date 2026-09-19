# Decision Report

- generated_at: 2026-09-19T17:21:29.789121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15071**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15071, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.70% | **-1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +3.63% | **+1.27%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.16% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.43% | **+2.40%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.44% | **+1.95%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.83% | **+1.42%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 5992件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$241.29** / 初期 $100.00 (+141.29%)
- 確定: 3187件 (Win 882 / Loss 760 / Flat 1545) / skip 5295件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1463 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $241.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定: 2974件 (Win 880 / Loss 1176 / Flat 918) / pending 0件 / skip 3573件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000354 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ENA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.01

## 6. Latest Market Context

- 更新: 2026-09-19T17:21:17.559204+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=81632.6
- Funnel: target 1050 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OFC/USDT:USDT | +41.86% | $1,222,223.56 |
| BANK/USDT:USDT | +15.99% | $1,170,685.79 |
| PEPE/USDT:USDT | +9.46% | $131,753,878.73 |
| FILECOIN/USDT:USDT | +8.72% | $8,838,377.96 |
| PIEVERSE/USDT:USDT | +6.38% | $1,325,393.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.59% | +4.79% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +3.92% | +4.11% |
| PEPE/USDT:USDT | below_1h_threshold | +3.75% | +3.94% |
| PENGU/USDT:USDT | below_1h_threshold | +3.20% | +3.40% |
| ORDI/USDT:USDT | below_1h_threshold | +3.00% | +3.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
