# Decision Report

- generated_at: 2026-05-30T10:30:22.805212+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5117**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.06% / filled 20/20。**
- 全期間 MARKET基準: n=5117, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.09% | **+1.09%** |
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.84% | **+0.72%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.63% | **+0.44%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.09% | **+0.22%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.47% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.12** / 初期 $100.00 (+27.12%)
- 確定: 772件 (Win 181 / Loss 232 / Flat 359) / skip 906件
- 成長率目線: 平均log +0.000311 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $127.12

## 4. Latest Market Context

- 更新: 2026-05-30T10:30:20.396191+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=73597.2
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NFP/USDT:USDT | +53.82% | $2,554,669.56 |
| HEI/USDT:USDT | +28.82% | $17,564,143.26 |
| LAB/USDT:USDT | +26.43% | $127,873,557.57 |
| VTHO/USDT:USDT | +22.55% | $1,473,960.75 |
| H/USDT:USDT | +18.62% | $1,801,390.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.07% | +4.04% |
| XLM/USDT:USDT | below_1h_threshold | +3.42% | +3.39% |
| LIT/USDT:USDT | below_1h_threshold | +2.27% | +2.24% |
| LAB/USDT:USDT | below_1h_threshold | +2.18% | +2.15% |
| BASED/USDT:USDT | below_1h_threshold | +1.89% | +1.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
