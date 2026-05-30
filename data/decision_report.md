# Decision Report

- generated_at: 2026-05-30T11:00:14.461644+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5119**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.66% / filled 20/20。**
- 全期間 MARKET基準: n=5119, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.69% | **+1.69%** |
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.55% | **+1.32%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.48% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.57% | **+0.51%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.32% | **+0.24%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.09% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.28** / 初期 $100.00 (+27.28%)
- 確定: 774件 (Win 182 / Loss 233 / Flat 359) / skip 906件
- 成長率目線: 平均log +0.000312 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $127.28

## 4. Latest Market Context

- 更新: 2026-05-30T11:00:11.706156+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=73605.0
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.8 >= 65=1, 4h RSI 81.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NFP/USDT:USDT | +48.69% | $2,870,900.94 |
| HEI/USDT:USDT | +30.67% | $17,953,152.78 |
| LAB/USDT:USDT | +27.12% | $132,547,002.28 |
| H/USDT:USDT | +24.23% | $2,433,260.74 |
| VTHO/USDT:USDT | +21.31% | $1,530,623.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +3.80% | +3.76% |
| XLM/USDT:USDT | below_1h_threshold | +3.78% | +3.75% |
| BILL/USDT:USDT | below_1h_threshold | +3.69% | +3.65% |
| GRASS/USDT:USDT | below_1h_threshold | +2.96% | +2.92% |
| LAB/USDT:USDT | below_1h_threshold | +2.52% | +2.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
