# Decision Report

- generated_at: 2026-09-04T04:06:33.170070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13577**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.12% / filled 20/20。**
- 全期間 MARKET基準: n=13577, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.12% | **+2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.12% | **+2.12%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.80% | **+1.62%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.13% | **+1.28%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.63% | **+0.98%** |
| LIMIT_BB3S | 3/19 | 15.8% | +6.15% | **+0.97%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.29% | **-0.03%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -1.08% | **-0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5129件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.51** / 初期 $100.00 (+85.51%)
- 確定: 2393件 (Win 678 / Loss 576 / Flat 1139) / skip 4595件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0617 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.51** / 初期 $100.00 (+16.51%)
- 確定: 2232件 (Win 664 / Loss 875 / Flat 693) / pending 5件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.51

## 6. Latest Market Context

- 更新: 2026-09-04T04:06:20.993105+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=80835.4
- Funnel: target 1046 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +32.92% | $11,247,725.63 |
| TRIA/USDT:USDT | +27.18% | $1,520,923.65 |
| BASECAT/USDT:USDT | +21.17% | $2,020,344.83 |
| PONS/USDT:USDT | +16.16% | $9,478,766.85 |
| MARSCOIN/USDT:USDT | +14.75% | $9,980,396.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +2.55% | +2.52% |
| TRIA/USDT:USDT | below_1h_threshold | +2.23% | +2.20% |
| BTR/USDT:USDT | below_1h_threshold | +2.02% | +1.98% |
| ONG/USDT:USDT | below_1h_threshold | +1.86% | +1.83% |
| DASH/USDT:USDT | below_1h_threshold | +1.63% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
