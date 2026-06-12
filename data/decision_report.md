# Decision Report

- generated_at: 2026-06-12T09:44:37.906603+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6494**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.06% / filled 20/20。**
- 全期間 MARKET基準: n=6494, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.07% | **+0.96%** |
| LIMIT_BB3S | 5/20 | 25.0% | +2.48% | **+0.62%** |
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.73% | **+0.37%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.27% | **+0.14%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$162.30** / 初期 $100.00 (+62.30%)
- 確定: 1368件 (Win 371 / Loss 441 / Flat 556) / skip 1687件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $162.30

## 4. Latest Market Context

- 更新: 2026-06-12T09:44:34.046975+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.67% price=63863.4
- Funnel: target 769 → liquid 158 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.1 >= 65=1, 4h RSI 85.7 >= 65=1, 4h RSI 68.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +101.28% | $150,934,047.16 |
| ESPORTS/USDT:USDT | +64.02% | $39,692,527.15 |
| NAORIS/USDT:USDT | +50.76% | $3,417,822.73 |
| XPL/USDT:USDT | +41.13% | $10,732,778.32 |
| AIN/USDT:USDT | +29.63% | $1,017,939.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_relative_strength | +5.01% | +4.34% |
| HMSTR/USDT:USDT | below_1h_threshold | +4.22% | +3.55% |
| LIT/USDT:USDT | below_1h_threshold | +3.66% | +2.99% |
| AIN/USDT:USDT | below_1h_threshold | +3.51% | +2.85% |
| SOXL/USDT:USDT | below_1h_threshold | +3.23% | +2.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
