# Decision Report

- generated_at: 2026-07-17T07:26:13.454557+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8827**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.93% / filled 20/20。**
- 全期間 MARKET基準: n=8827, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.93% | **+1.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.37% | **+1.17%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.11% | **+0.63%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.04% | **+0.61%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.32% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.59% | **+0.78%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.79% | **+0.42%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.91% | **+0.41%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.07% | **-0.31%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.47% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$111.26** / 初期 $100.00 (+11.26%)
- 確定トレード: 109件 (TP 41 / SL 64 / EXP 4)
- 最新: EVAA/USDT:USDT TP_HIT PnL +8.00% 残高後 $111.26
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.01** / 初期 $100.00 (+242.01%)
- 確定: 2942件 (Win 916 / Loss 947 / Flat 1079) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $342.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.06** / 初期 $100.00 (+7.06%)
- 確定: 789件 (Win 181 / Loss 171 / Flat 437) / skip 1449件
- 成長率目線: 平均log +0.000086 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0044 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 94件 (Win 30 / Loss 60 / Flat 4) / pending 4件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000332 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.00

## 6. Latest Market Context

- 更新: 2026-07-17T07:26:07.114936+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=62846.3
- Funnel: target 885 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUMIA/USDT:USDT | +30.23% | $1,920,394.43 |
| TAC/USDT:USDT | +16.44% | $3,326,272.14 |
| KAITO/USDT:USDT | +15.12% | $3,884,725.16 |
| T/USDT:USDT | +14.71% | $1,879,089.76 |
| SOXS/USDT:USDT | +12.30% | $1,588,470.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUMIA/USDT:USDT | below_1h_threshold | +4.08% | +4.18% |
| APDSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.91% |
| TAC/USDT:USDT | below_1h_threshold | +1.96% | +2.06% |
| ENS/USDT:USDT | below_1h_threshold | +1.53% | +1.64% |
| AKE/USDT:USDT | below_1h_threshold | +1.38% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
