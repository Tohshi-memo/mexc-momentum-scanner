# Decision Report

- generated_at: 2026-09-01T03:51:30.234141+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13223**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.61% / filled 20/20。**
- 全期間 MARKET基準: n=13223, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.24% | **+1.12%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.20% | **+0.99%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.88% | **+0.71%** |
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.87% | **+0.79%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.41% | **+0.29%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.36% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4878件 (Win 1485 / Loss 1609 / Flat 1784) / skip 4906件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.14** / 初期 $100.00 (+75.14%)
- 確定: 2204件 (Win 612 / Loss 531 / Flat 1061) / skip 4430件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0663 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $175.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.48** / 初期 $100.00 (+15.48%)
- 確定: 2086件 (Win 610 / Loss 814 / Flat 662) / pending 1件 / skip 2611件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000145 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.48

## 6. Latest Market Context

- 更新: 2026-09-01T03:51:18.938409+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=78683.0
- Funnel: target 1031 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +57.21% | $7,827,404.84 |
| USELESS/USDT:USDT | +27.32% | $18,985,306.96 |
| ARB/USDT:USDT | +27.24% | $58,279,877.27 |
| 0G/USDT:USDT | +14.42% | $27,095,315.24 |
| CRV/USDT:USDT | +13.94% | $4,818,458.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.64% | +4.30% |
| BTW/USDT:USDT | below_1h_threshold | +4.22% | +3.88% |
| UNI/USDT:USDT | below_1h_threshold | +3.03% | +2.69% |
| JASMY/USDT:USDT | below_1h_threshold | +2.89% | +2.56% |
| USELESS/USDT:USDT | below_1h_threshold | +2.63% | +2.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
