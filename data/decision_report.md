# Decision Report

- generated_at: 2026-06-15T03:07:15.808641+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6728**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.72% / filled 20/20。**
- 全期間 MARKET基準: n=6728, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.29% | **+1.22%** |
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.62% | **+0.53%** |
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.64% | **+1.09%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.06% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$174.41** / 初期 $100.00 (+74.41%)
- 確定: 1601件 (Win 423 / Loss 500 / Flat 678) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $174.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.53** / 初期 $100.00 (-0.47%)
- 確定: 96件 (Win 22 / Loss 15 / Flat 59) / skip 43件
- 成長率目線: 平均log -0.000049 / 幾何平均 -0.005% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0508 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $99.53

## 5. Latest Market Context

- 更新: 2026-06-15T03:07:10.909053+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=65539.1
- Funnel: target 770 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLO/USDT:USDT | +33.90% | $1,961,654.38 |
| EVAA/USDT:USDT | +28.14% | $17,424,314.56 |
| RIF/USDT:USDT | +25.39% | $4,280,781.25 |
| UAI/USDT:USDT | +18.53% | $1,229,399.56 |
| WLD/USDT:USDT | +16.82% | $94,509,868.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +1.46% | +1.30% |
| UAI/USDT:USDT | below_1h_threshold | +1.32% | +1.16% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.71% | +0.55% |
| CHIP/USDT:USDT | below_1h_threshold | +0.62% | +0.45% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +0.61% | +0.44% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
