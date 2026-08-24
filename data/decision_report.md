# Decision Report

- generated_at: 2026-08-24T00:56:29.869085+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12483**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.75% / filled 20/20。**
- 全期間 MARKET基準: n=12483, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +2.08% | **+1.45%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.16% | **+1.05%** |
| LIMIT_BB3S | 7/17 | 41.2% | +2.53% | **+1.04%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.12% | **+0.89%** |
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.76% | **+2.76%** |
| LIMIT_FIB1272_LONG | 16/20 | 80.0% | +2.12% | **+1.69%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +2.19% | **+1.42%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.05% | **+0.92%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.82% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4509件 (Win 1375 / Loss 1477 / Flat 1657) / skip 4535件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.26** / 初期 $100.00 (+57.26%)
- 確定: 1959件 (Win 536 / Loss 469 / Flat 954) / skip 3935件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0013 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $157.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.75** / 初期 $100.00 (+16.75%)
- 確定: 1873件 (Win 551 / Loss 708 / Flat 614) / pending 2件 / skip 2081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000085 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.75

## 6. Latest Market Context

- 更新: 2026-08-24T00:56:20.874092+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=77496.5
- Funnel: target 1018 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GRASS/USDT:USDT | +12.43% | $2,550,908.02 |
| SPK/USDT:USDT | +11.20% | $7,475,971.93 |
| LIT/USDT:USDT | +8.72% | $9,940,281.72 |
| TUT/USDT:USDT | +8.66% | $54,257,469.09 |
| PENGU/USDT:USDT | +6.99% | $26,104,840.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +2.95% | +3.23% |
| ONG/USDT:USDT | below_1h_threshold | +2.00% | +2.28% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.74% | +2.01% |
| VELVET/USDT:USDT | below_1h_threshold | +1.65% | +1.93% |
| FF/USDT:USDT | below_1h_threshold | +1.11% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
