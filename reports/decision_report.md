# Decision Report

- generated_at: 2026-06-03T16:58:17.664727+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5561**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=5561, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.83% | **+1.83%** |
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.53% | **+1.07%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.64% | **+1.06%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.69% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.92% | **+0.38%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +0.71% | **+0.36%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.44% | **+0.24%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1118件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T16:52:58.575479+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=65936.8
- Funnel: target 771 → liquid 150 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.2 >= 65=1, 4h RSI 70.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +19.20% | $3,230,712.72 |
| EDEN/USDT:USDT | +11.76% | $1,124,810.95 |
| BP/USDT:USDT | +7.45% | $1,284,455.74 |
| HEI/USDT:USDT | +7.01% | $1,027,058.47 |
| LAB/USDT:USDT | +4.99% | $283,777,542.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.94% | +5.10% |
| PLAY/USDT:USDT | below_1h_threshold | +4.49% | +4.64% |
| EPIC/USDT:USDT | below_1h_threshold | +3.51% | +3.67% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.81% | +2.97% |
| US/USDT:USDT | below_1h_threshold | +2.61% | +2.77% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
