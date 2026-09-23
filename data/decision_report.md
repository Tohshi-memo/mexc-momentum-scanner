# Decision Report

- generated_at: 2026-09-23T23:01:28.391525+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15445**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=15445, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.75% | **+1.40%** |
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_5PCT | 4/20 | 20.0% | +6.24% | **+1.25%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.49% | **+1.05%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.10% | **+0.99%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.33% | **+0.73%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | -0.30% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5896件 (Win 1739 / Loss 1890 / Flat 2267) / skip 6110件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.56** / 初期 $100.00 (+152.56%)
- 確定: 3392件 (Win 934 / Loss 790 / Flat 1668) / skip 5464件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0652 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $252.56

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.35** / 初期 $100.00 (+21.35%)
- 確定: 3137件 (Win 923 / Loss 1235 / Flat 979) / pending 2件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000238 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $121.35

## 6. Latest Market Context

- 更新: 2026-09-23T23:01:16.676703+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=84482.5
- Funnel: target 1061 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +20.84% | $9,537,068.21 |
| LSK/USDT:USDT | +14.60% | $3,929,480.31 |
| BTW/USDT:USDT | +9.42% | $3,668,347.67 |
| MARSCOIN/USDT:USDT | +8.11% | $3,344,128.20 |
| UAI/USDT:USDT | +6.18% | $2,523,732.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZRO/USDT:USDT | below_1h_threshold | +0.23% | +0.28% |
| KERNEL/USDT:USDT | below_1h_threshold | +0.20% | +0.25% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.18% | +0.23% |
| SOXL/USDT:USDT | below_1h_threshold | +0.16% | +0.21% |
| NEAR/USDT:USDT | below_1h_threshold | +0.12% | +0.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
