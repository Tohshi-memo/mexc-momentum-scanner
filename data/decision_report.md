# Decision Report

- generated_at: 2026-08-04T10:11:18.200279+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10285**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=10285, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +3.58% | **+2.68%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +7.81% | **+0.78%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.22% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3120件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1284件 (Win 359 / Loss 299 / Flat 626) / skip 2412件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0488 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.74** / 初期 $100.00 (+16.74%)
- 確定: 1052件 (Win 338 / Loss 408 / Flat 306) / pending 3件 / skip 700件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.74

## 6. Latest Market Context

- 更新: 2026-08-04T10:11:10.943426+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=63507.0
- Funnel: target 936 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CYS/USDT:USDT | +47.84% | $3,297,789.86 |
| SKYAI/USDT:USDT | +18.26% | $32,525,027.15 |
| PLTRSTOCK/USDT:USDT | +17.29% | $5,362,021.33 |
| UNITREE/USDT:USDT | +17.28% | $1,266,514.25 |
| BTW/USDT:USDT | +15.92% | $9,223,529.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +3.53% | +3.64% |
| COTI/USDT:USDT | below_1h_threshold | +2.29% | +2.40% |
| NIL/USDT:USDT | below_1h_threshold | +1.78% | +1.89% |
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +0.99% |
| VELVET/USDT:USDT | below_1h_threshold | +0.53% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
