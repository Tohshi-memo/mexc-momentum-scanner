# Decision Report

- generated_at: 2026-07-01T13:59:56.119327+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7990**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=7990, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +4.00% | **+1.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| MARKET_LONG | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +2.99% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$262.78** / 初期 $100.00 (+162.78%)
- 確定: 2389件 (Win 725 / Loss 791 / Flat 873) / skip 2162件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: METASTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $262.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.79** / 初期 $100.00 (+6.79%)
- 確定: 510件 (Win 129 / Loss 122 / Flat 259) / skip 891件
- 成長率目線: 平均log +0.000129 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0378 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: METASTOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.79

## 5. Latest Market Context

- 更新: 2026-07-01T13:59:49.334464+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.52% price=59388.2
- Funnel: target 825 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +109.71% | $14,655,701.12 |
| M/USDT:USDT | +50.07% | $6,808,692.59 |
| BAS/USDT:USDT | +46.72% | $4,102,270.39 |
| BASED/USDT:USDT | +27.70% | $13,781,003.50 |
| ZBT/USDT:USDT | +22.89% | $2,860,298.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +4.98% | +3.46% |
| GRASS/USDT:USDT | below_1h_threshold | +4.92% | +3.40% |
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +4.83% | +3.31% |
| HIGH/USDT:USDT | below_1h_threshold | +3.81% | +2.29% |
| NES/USDT:USDT | below_1h_threshold | +3.78% | +2.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
