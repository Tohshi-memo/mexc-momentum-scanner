# Decision Report

- generated_at: 2026-08-12T10:21:35.593152+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11358**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11358, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +3.32% | **+1.16%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.94% | **+0.78%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.68% | **+1.52%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +4.55% | **+1.36%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +6.56% | **+1.31%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$618.35** / 初期 $100.00 (+518.35%)
- 確定: 3944件 (Win 1232 / Loss 1287 / Flat 1425) / skip 3975件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $618.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$148.34** / 初期 $100.00 (+48.34%)
- 確定: 1594件 (Win 449 / Loss 372 / Flat 773) / skip 3175件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0862 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $148.34

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.31** / 初期 $100.00 (+14.31%)
- 確定: 1373件 (Win 413 / Loss 534 / Flat 426) / pending 4件 / skip 1453件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000140 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.31

## 6. Latest Market Context

- 更新: 2026-08-12T10:21:21.524330+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64078.3
- Funnel: target 967 → liquid 183 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +77.88% | $3,567,429.30 |
| PROM/USDT:USDT | +54.33% | $8,692,529.93 |
| JIMOTHY/USDT:USDT | +52.87% | $2,694,391.02 |
| BR/USDT:USDT | +45.52% | $2,840,973.20 |
| STORJ/USDT:USDT | +25.84% | $1,238,045.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +4.23% | +4.23% |
| AKE/USDT:USDT | below_1h_threshold | +3.35% | +3.35% |
| NIL/USDT:USDT | below_1h_threshold | +2.22% | +2.21% |
| HOLO/USDT:USDT | below_1h_threshold | +1.73% | +1.73% |
| SOXL/USDT:USDT | below_1h_threshold | +0.77% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
