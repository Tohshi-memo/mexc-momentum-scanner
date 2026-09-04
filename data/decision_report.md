# Decision Report

- generated_at: 2026-09-04T10:56:37.317356+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13612**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.29% / filled 20/20。**
- 全期間 MARKET基準: n=13612, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.29% | **+0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +1.61% | **+1.38%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.20% | **+0.48%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5010件 (Win 1516 / Loss 1644 / Flat 1850) / skip 5163件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.25** / 初期 $100.00 (+85.25%)
- 確定: 2416件 (Win 681 / Loss 577 / Flat 1158) / skip 4607件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0247 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $185.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.50** / 初期 $100.00 (+16.50%)
- 確定: 2261件 (Win 670 / Loss 878 / Flat 713) / pending 6件 / skip 2819件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000136 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.50

## 6. Latest Market Context

- 更新: 2026-09-04T10:56:21.042568+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=81079.9
- Funnel: target 1052 → liquid 163 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.7 >= 65=1, 4h RSI 68.9 >= 65=1, 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +54.16% | $7,375,379.79 |
| TRIA/USDT:USDT | +27.58% | $8,629,768.20 |
| USELESS/USDT:USDT | +24.68% | $40,792,456.57 |
| BASECAT/USDT:USDT | +20.81% | $2,100,068.61 |
| HNT/USDT:USDT | +18.90% | $13,742,072.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +3.18% | +3.10% |
| CAKE/USDT:USDT | below_1h_threshold | +2.17% | +2.09% |
| LIT/USDT:USDT | below_1h_threshold | +1.72% | +1.64% |
| XPL/USDT:USDT | below_1h_threshold | +0.86% | +0.78% |
| ZEN/USDT:USDT | below_1h_threshold | +0.51% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
