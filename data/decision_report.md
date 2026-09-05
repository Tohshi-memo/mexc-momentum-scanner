# Decision Report

- generated_at: 2026-09-05T05:36:16.304609+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13700**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13700, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.88% | **-1.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +4.35% | **+1.74%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.97% | **+0.79%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.40% | **+0.91%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.75% | **+0.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.70% | **+0.60%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.81% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 202件 (TP 75 / SL 122 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.36** / 初期 $100.00 (+755.36%)
- 確定: 5012件 (Win 1516 / Loss 1645 / Flat 1851) / skip 5249件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $855.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.29** / 初期 $100.00 (+88.29%)
- 確定: 2447件 (Win 691 / Loss 585 / Flat 1171) / skip 4664件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0686 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $188.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.20** / 初期 $100.00 (+18.20%)
- 確定: 2333件 (Win 696 / Loss 896 / Flat 741) / pending 6件 / skip 2835件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000292 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $118.20

## 6. Latest Market Context

- 更新: 2026-09-05T05:36:07.980285+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=79558.3
- Funnel: target 1050 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +92.75% | $6,462,493.80 |
| 4/USDT:USDT | +65.50% | $15,370,930.06 |
| DASH/USDT:USDT | +35.77% | $38,823,624.68 |
| ZEN/USDT:USDT | +25.62% | $9,504,683.35 |
| AKE/USDT:USDT | +22.34% | $12,188,702.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +4.82% | +4.70% |
| BASECAT/USDT:USDT | below_1h_threshold | +4.62% | +4.50% |
| DASH/USDT:USDT | below_1h_threshold | +3.01% | +2.89% |
| ZEN/USDT:USDT | below_1h_threshold | +2.94% | +2.82% |
| 4/USDT:USDT | below_1h_threshold | +2.87% | +2.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
