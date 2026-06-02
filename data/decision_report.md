# Decision Report

- generated_at: 2026-06-02T03:47:19.157809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5398**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=5398, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.60% | **+0.96%** |
| ASK | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.82% | **+0.57%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.60% | **+0.57%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.94% | **+0.52%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.76** / 初期 $100.00 (+31.76%)
- 確定: 910件 (Win 211 / Loss 272 / Flat 427) / skip 1049件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $131.76

## 4. Latest Market Context

- 更新: 2026-06-02T03:47:12.449976+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=70947.3
- Funnel: target 776 → liquid 147 → pre 50 → checked 50 → surge 6 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1, 4h RSI 66.6 >= 65=1, 4h RSI 84.6 >= 65=1, 4h RSI 77.8 >= 65=1, 4h RSI 91.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +22.88% | $1,259,682.07 |
| LAB/USDT:USDT | +22.51% | $199,010,380.55 |
| SKYAI/USDT:USDT | +19.91% | $4,108,282.02 |
| MRVLSTOCK/USDT:USDT | +19.60% | $1,337,335.38 |
| H/USDT:USDT | +19.21% | $56,505,177.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.23% | +4.04% |
| JTO/USDT:USDT | below_1h_threshold | +3.80% | +3.62% |
| STG/USDT:USDT | below_1h_threshold | +3.48% | +3.30% |
| WLD/USDT:USDT | below_1h_threshold | +3.48% | +3.29% |
| ARKM/USDT:USDT | below_1h_threshold | +3.37% | +3.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
