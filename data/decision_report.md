# Decision Report

- generated_at: 2026-06-02T02:43:44.983107+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5391**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.89% / filled 20/20。**
- 全期間 MARKET基準: n=5391, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.89% | **+1.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.47% | **+2.47%** |
| MARKET | 20/20 | 100.0% | +1.89% | **+1.89%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.65% | **+1.46%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.23% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.60% | **+0.33%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.29% | **+0.19%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.77% | **-0.46%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.98** / 初期 $100.00 (+31.98%)
- 確定: 904件 (Win 211 / Loss 271 / Flat 422) / skip 1048件
- 成長率目線: 平均log +0.000307 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.04% 残高後 $131.98

## 4. Latest Market Context

- 更新: 2026-06-02T02:43:41.644708+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=70572.8
- Funnel: target 776 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.4 >= 65=1, 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +27.38% | $10,522,963.70 |
| RIF/USDT:USDT | +14.89% | $1,111,106.42 |
| LAB/USDT:USDT | +14.16% | $196,250,184.30 |
| WLD/USDT:USDT | +12.39% | $137,705,938.51 |
| H/USDT:USDT | +12.00% | $57,769,462.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.95% | +5.02% |
| STG/USDT:USDT | below_1h_threshold | +4.73% | +4.80% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.25% | +4.32% |
| ZEC/USDT:USDT | below_1h_threshold | +2.66% | +2.73% |
| LIT/USDT:USDT | below_1h_threshold | +2.24% | +2.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
