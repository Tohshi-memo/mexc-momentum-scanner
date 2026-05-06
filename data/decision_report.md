# Decision Report

- generated_at: 2026-05-06T15:58:02.885089+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3479**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=3479, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.49% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| ASK_LONG | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.98% | **+0.74%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.24% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 31件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T15:57:57.257970+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=81667.2
- Funnel: target 770 → liquid 198 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1, 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +120.85% | $5,951,556.66 |
| LAB/USDT:USDT | +51.51% | $187,159,007.38 |
| BILL/USDT:USDT | +37.89% | $6,214,288.84 |
| ZEC/USDT:USDT | +35.83% | $777,470,305.83 |
| IO/USDT:USDT | +33.07% | $15,774,425.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.01% | +3.77% |
| AR/USDT:USDT | below_1h_threshold | +3.44% | +3.20% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +3.33% | +3.09% |
| VVV/USDT:USDT | below_1h_threshold | +2.63% | +2.39% |
| XPL/USDT:USDT | below_1h_threshold | +2.61% | +2.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
