# Decision Report

- generated_at: 2026-08-05T00:11:28.624176+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10327**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.01% / filled 20/20。**
- 全期間 MARKET基準: n=10327, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +2.01% | **+1.31%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.23% | **+1.11%** |
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.58% | **+1.11%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.26% | **+0.75%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.66%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.88% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3162件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2453件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0543 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.68** / 初期 $100.00 (+16.68%)
- 確定: 1084件 (Win 348 / Loss 422 / Flat 314) / pending 1件 / skip 714件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.68

## 6. Latest Market Context

- 更新: 2026-08-05T00:11:19.754046+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=64012.3
- Funnel: target 937 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +33.50% | $3,971,166.22 |
| TAKE/USDT:USDT | +23.42% | $1,268,725.61 |
| CASHCAT/USDT:USDT | +20.10% | $1,054,576.47 |
| HFT/USDT:USDT | +15.28% | $1,394,920.69 |
| MARSCOIN/USDT:USDT | +12.84% | $1,010,473.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +3.45% | +3.55% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.61% | +2.71% |
| BLESS/USDT:USDT | below_1h_threshold | +2.12% | +2.22% |
| NIL/USDT:USDT | below_1h_threshold | +1.70% | +1.80% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.24% | +1.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
