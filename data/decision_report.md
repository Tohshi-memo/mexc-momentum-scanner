# Decision Report

- generated_at: 2026-08-25T13:11:22.422622+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12602**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=12602, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.05% | **+0.04%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.03% | **+0.02%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.96% | **+1.08%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.56% | **+1.01%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.70% | **+0.85%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.45% | **+0.34%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.32% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$690.81** / 初期 $100.00 (+590.81%)
- 確定: 4582件 (Win 1392 / Loss 1505 / Flat 1685) / skip 4581件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $690.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4036件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.86** / 初期 $100.00 (+14.86%)
- 確定: 1929件 (Win 564 / Loss 735 / Flat 630) / pending 5件 / skip 2142件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000041 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.86

## 6. Latest Market Context

- 更新: 2026-08-25T13:11:13.408466+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=78861.8
- Funnel: target 1023 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +92.72% | $5,302,178.08 |
| JIMOTHY/USDT:USDT | +74.00% | $1,788,996.87 |
| ONG/USDT:USDT | +44.89% | $9,662,299.61 |
| TAC/USDT:USDT | +35.10% | $6,890,487.45 |
| BR/USDT:USDT | +18.74% | $3,748,776.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONG/USDT:USDT | below_1h_threshold | +2.62% | +2.73% |
| TAC/USDT:USDT | below_1h_threshold | +1.62% | +1.73% |
| BR/USDT:USDT | below_1h_threshold | +1.32% | +1.44% |
| ACE/USDT:USDT | below_1h_threshold | +1.28% | +1.39% |
| AKE/USDT:USDT | below_1h_threshold | +0.76% | +0.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
