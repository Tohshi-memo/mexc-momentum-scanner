# Decision Report

- generated_at: 2026-08-04T09:31:31.754754+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10281**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10281, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.21% | **+0.97%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.06% | **+0.95%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.34% | **+0.87%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.58% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3116件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1284件 (Win 359 / Loss 299 / Flat 626) / skip 2408件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0294 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.35** / 初期 $100.00 (+17.35%)
- 確定: 1048件 (Win 338 / Loss 405 / Flat 305) / pending 3件 / skip 700件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000275 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.35

## 6. Latest Market Context

- 更新: 2026-08-04T09:31:22.242324+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63573.0
- Funnel: target 933 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UNITREE/USDT:USDT | +28.79% | $1,152,862.25 |
| SKYAI/USDT:USDT | +22.57% | $31,764,635.91 |
| PLTRSTOCK/USDT:USDT | +16.93% | $5,247,416.95 |
| MYX/USDT:USDT | +15.37% | $1,905,591.56 |
| BTW/USDT:USDT | +14.95% | $9,283,393.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_relative_strength | +5.01% | +4.99% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.51% | +4.49% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.48% | +2.46% |
| BILL/USDT:USDT | below_1h_threshold | +2.37% | +2.35% |
| NIL/USDT:USDT | below_1h_threshold | +1.89% | +1.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
