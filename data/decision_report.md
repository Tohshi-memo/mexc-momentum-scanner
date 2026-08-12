# Decision Report

- generated_at: 2026-08-12T08:06:22.739642+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11343**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=11343, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.33% | **+1.07%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.55% | **+0.47%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +4.58% | **+3.05%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.28% | **+0.10%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3940件 (Win 1230 / Loss 1285 / Flat 1425) / skip 3964件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$146.78** / 初期 $100.00 (+46.78%)
- 確定: 1579件 (Win 442 / Loss 365 / Flat 772) / skip 3175件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0795 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $146.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.07** / 初期 $100.00 (+14.07%)
- 確定: 1358件 (Win 409 / Loss 530 / Flat 419) / pending 2件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000035 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $114.07

## 6. Latest Market Context

- 更新: 2026-08-12T08:06:16.233864+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63812.8
- Funnel: target 967 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +64.53% | $2,293,612.86 |
| APR/USDT:USDT | +64.39% | $1,452,653.13 |
| PROM/USDT:USDT | +34.19% | $6,984,867.43 |
| BEAT/USDT:USDT | +20.00% | $87,742,414.28 |
| CRWVSTOCK/USDT:USDT | +18.13% | $4,507,455.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +2.74% | +2.73% |
| BEAT/USDT:USDT | below_1h_threshold | +1.82% | +1.81% |
| HOLO/USDT:USDT | below_1h_threshold | +1.37% | +1.36% |
| BTW/USDT:USDT | below_1h_threshold | +1.03% | +1.02% |
| SNXX/USDT:USDT | below_1h_threshold | +0.96% | +0.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
