# Decision Report

- generated_at: 2026-08-27T07:11:19.374732+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12793**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=12793, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/15 | 60.0% | +2.24% | **+1.34%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.58% | **+0.29%** |
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.79% | **+1.16%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.47% | **+0.96%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.71% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.03** / 初期 $100.00 (+616.03%)
- 確定: 4669件 (Win 1414 / Loss 1532 / Flat 1723) / skip 4685件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2002件 (Win 544 / Loss 483 / Flat 975) / skip 4202件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0589 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.60** / 初期 $100.00 (+15.60%)
- 確定: 1984件 (Win 580 / Loss 758 / Flat 646) / pending 0件 / skip 2282件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000198 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $115.60

## 6. Latest Market Context

- 更新: 2026-08-27T07:11:10.208686+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78762.9
- Funnel: target 1018 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +56.22% | $3,398,692.04 |
| TAC/USDT:USDT | +26.42% | $13,092,824.89 |
| RUNE/USDT:USDT | +25.18% | $1,884,011.97 |
| PROM/USDT:USDT | +20.99% | $4,710,058.97 |
| SPX/USDT:USDT | +19.82% | $6,036,581.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +3.51% | +3.57% |
| MOVR/USDT:USDT | below_1h_threshold | +2.80% | +2.86% |
| BLESS/USDT:USDT | below_1h_threshold | +1.70% | +1.76% |
| SPX/USDT:USDT | below_1h_threshold | +1.62% | +1.68% |
| SNXX/USDT:USDT | below_1h_threshold | +1.44% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
