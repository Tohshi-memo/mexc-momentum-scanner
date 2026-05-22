# Decision Report

- generated_at: 2026-05-22T08:28:49.367097+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4676**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=4676, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.44% | **+0.65%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/9 | 66.7% | +2.77% | **+1.85%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.63% | **+1.55%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.76% | **+1.41%** |
| ASK_LONG | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.21% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 689件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T08:28:47.091356+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77423.0
- Funnel: target 768 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +49.74% | $3,182,464.88 |
| ALT/USDT:USDT | +35.08% | $1,004,832.75 |
| NEAR/USDT:USDT | +26.02% | $83,793,922.76 |
| GRASS/USDT:USDT | +21.79% | $5,125,248.89 |
| OPG/USDT:USDT | +21.44% | $1,156,784.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.78% | +4.71% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.39% | +2.32% |
| ARKM/USDT:USDT | below_1h_threshold | +2.18% | +2.11% |
| PLUME/USDT:USDT | below_1h_threshold | +2.13% | +2.06% |
| OPG/USDT:USDT | below_1h_threshold | +2.05% | +1.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
